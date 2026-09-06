#!/usr/bin/env python3
"""Validate full-corpus review packets against source and audit their combined graph."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'packages/compiler'))
from graph_algorithms import cycle_witnesses


REQUIRED_PACKET_KEYS = {'id', 'path', 'before', 'review_count_before', 'sha256'}


def _read_json(path, errors):
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f'{path.name}: invalid JSON: {exc}')
        return None


def _validate_source(row, label, errors):
    missing = REQUIRED_PACKET_KEYS - row.keys()
    if missing:
        errors.append(f'{label}: missing source keys: {sorted(missing)}')
        return False
    source = Path(row['path'])
    try:
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
    except OSError as exc:
        errors.append(f'{label}: cannot read source: {exc}')
        return False
    if digest != row['sha256']:
        errors.append(f'{label}: source hash mismatch')
        return False
    return True


def audit(directory):
    errors = []
    registry = _read_json(directory / 'registry.json', errors) or []
    if not isinstance(registry, list):
        errors.append('registry.json must contain a list')
        registry = []
    registry_ids = [row.get('id') for row in registry if isinstance(row, dict)]
    nodes = {row['id']: row for row in registry if isinstance(row, dict) and 'id' in row}
    if len(nodes) != len(registry_ids):
        errors.append('Duplicate registry IDs')
    for row in registry:
        if isinstance(row, dict):
            missing = REQUIRED_PACKET_KEYS - row.keys()
            if missing:
                errors.append(f"registry {row.get('id', '<missing>')}: missing source keys: {sorted(missing)}")
        else:
            errors.append('registry: malformed row')
    graph = {node: row.get('before', []) for node, row in nodes.items()}
    new_path = directory / 'new_knowls.json'
    new_rows = []
    if new_path.exists():
        loaded = _read_json(new_path, errors)
        if not isinstance(loaded, list):
            errors.append('new_knowls.json must contain a list')
        else:
            new_rows = loaded
    new_ids = [row.get('id') for row in new_rows if isinstance(row, dict)]
    if len(set(new_ids)) != len(new_ids):
        errors.append('Duplicate new knowl IDs')
    for row in new_rows:
        label = f"new_knowls: {row.get('id', '<missing>')}" if isinstance(row, dict) else 'new_knowls: <malformed>'
        if not isinstance(row, dict):
            errors.append(f'{label}: row must be an object')
            continue
        if not _validate_source(row, label, errors):
            continue
        if not isinstance(row['review_count_before'], int) or row['review_count_before'] < 1:
            errors.append(f'{label}: new knowl must already have a positive review count')
        if row['id'] in nodes:
            errors.append(f'{label}: overlaps registry ID')
        if not isinstance(row['before'], list):
            errors.append(f'{label}: before must be a list')
            continue
        nodes[row['id']] = row
        graph[row['id']] = row['before']
    for node, prerequisites in list(graph.items()):
        if not isinstance(prerequisites, list):
            errors.append(f'{node}: before must be a list')
            graph[node] = []
    reviews = {}
    unresolved = []
    corrections = []
    cross_batch = []
    pending = []
    batches = []
    packet_id_counts = Counter()
    packet_files = sorted((directory / 'packets').glob('*.json'))
    packet_stems = {p.stem for p in packet_files}
    for packet in packet_files:
        packet_rows = _read_json(packet, errors)
        if not isinstance(packet_rows, list):
            errors.append(f'{packet.stem}: packet must contain a list')
            continue
        packet_ids = [row.get('id') for row in packet_rows if isinstance(row, dict)]
        packet_id_counts.update(packet_ids)
        if len(set(packet_ids)) != len(packet_ids):
            errors.append(f'{packet.stem}: duplicate packet IDs')
        assigned = {row['id']: row for row in packet_rows if isinstance(row, dict) and 'id' in row}
        for node in assigned:
            if node not in registry_ids:
                errors.append(f'{packet.stem}: packet ID is not in registry: {node}')
        for row in packet_rows:
            if isinstance(row, dict):
                _validate_source(row, f'{packet.stem}: packet source {row.get("id", "<missing>")}', errors)
            else:
                errors.append(f'{packet.stem}: malformed packet row')
        proposal = directory / 'proposals' / packet.name
        if not proposal.exists():
            pending.append(packet.stem)
            continue
        data = _read_json(proposal, errors)
        if not isinstance(data, dict):
            continue
        completed = data.get('reviews')
        if not isinstance(completed, list):
            errors.append(f'{packet.stem}: proposal reviews must be a list')
            completed = []
        deferred = data.get('unresolved', [])
        if not isinstance(deferred, list):
            errors.append(f'{packet.stem}: proposal unresolved must be a list')
            deferred = []
        reported = [row.get('id') for row in completed + deferred if isinstance(row, dict)]
        duplicates = [node for node, count in Counter(reported).items() if count > 1]
        if duplicates:
            errors.append(f'{packet.stem}: both reviewed/unresolved or duplicate IDs: {duplicates}')
        if set(reported) != set(assigned):
            errors.append(f'{packet.stem}: packet coverage mismatch; missing={sorted(set(assigned)-set(reported))}, extra={sorted(set(reported)-set(assigned))}')
        for row in completed:
            node = row.get('id') if isinstance(row, dict) else None
            if node is None:
                errors.append(f'{packet.stem}: malformed review row')
                continue
            if node not in assigned:
                continue
            original = assigned[node]
            if not isinstance(row, dict):
                errors.append(f'{packet.stem}: malformed review row for {node}')
                continue
            for key in ['before', 'review_count_before', 'sha256']:
                if key not in row or key not in original or row.get(key) != original[key]:
                    errors.append(f'{packet.stem}: {node}: incorrect {key}')
            _validate_source(original, f'{packet.stem}: {node}', errors)
            if node in reviews:
                errors.append(f'{node}: reviewed by multiple batches')
            if not isinstance(row.get('after'), list):
                errors.append(f'{node}: after must be a list')
                continue
            if len(row['after']) != len(set(row['after'])):
                errors.append(f'{node}: duplicate prerequisites')
            for prerequisite in row['after']:
                if prerequisite not in nodes:
                    errors.append(f'{node}: missing prerequisite {prerequisite}')
            if not row.get('rationale') or not row.get('core_summary'):
                errors.append(f'{node}: missing semantic review explanation')
            reviews[node] = row
            graph[node] = row['after']
        unresolved.extend(dict(row, batch=packet.stem) for row in deferred if isinstance(row, dict))
        corrections.extend(dict(row, batch=packet.stem) for row in data.get('content_corrections', []) if isinstance(row, dict))
        cross_batch.extend(dict(row, batch=packet.stem) for row in data.get('cross_batch_dependencies', []) if isinstance(row, dict))
        batches.append({'batch': packet.stem, 'reviews': len(completed), 'unresolved': len(deferred)})
    for suggestion in cross_batch:
        node = suggestion.get('id')
        targets = suggestion.get('suggested_after')
        if node not in graph or not isinstance(targets, list):
            errors.append(f"{suggestion.get('batch', '?')}: invalid cross-batch dependency")
            continue
        for target in targets:
            if target not in nodes:
                errors.append(f'{node}: missing cross-batch prerequisite {target}')
        # Cross-batch records are advisory historical recommendations.  They
        # are validated for shape and targets, but only completed reviews and
        # already-reviewed new knowls define the audited dependency graph.
    cycles = cycle_witnesses(graph)
    expected_unreviewed = {row['id'] for row in registry
                           if isinstance(row, dict) and row.get('review_count_before') == 0}
    assigned_unreviewed = {node for node, count in packet_id_counts.items()
                           if node in expected_unreviewed and count == 1}
    missing_assignments = sorted(expected_unreviewed - assigned_unreviewed)
    duplicate_assignments = sorted(node for node in expected_unreviewed
                                   if packet_id_counts[node] > 1)
    if missing_assignments:
        errors.append(f'missing packet coverage for unreviewed registry IDs: {missing_assignments}')
    if duplicate_assignments:
        errors.append(f'duplicate packet coverage for unreviewed registry IDs: {duplicate_assignments}')
    for row in new_rows:
        if isinstance(row, dict) and isinstance(row.get('before'), list):
            for target in row['before']:
                if target not in nodes:
                    errors.append(f"new_knowls: {row.get('id')}: missing prerequisite {target}")
    # A proposal file without an assigned packet can otherwise disappear from
    # the review accounting silently.
    proposal_dir = directory / 'proposals'
    for extra in proposal_dir.glob('*.json'):
        if re.fullmatch(r'\d{2}', extra.stem) and extra.stem not in packet_stems:
            errors.append(f'proposal without packet: {extra.stem}')
    return {'ok': not errors and not cycles and not pending and not unresolved,
            'nodes': len(nodes), 'new_knowls': len(new_rows),
            'originally_reviewed': sum(row.get('review_count_before', 0) > 0
                                       for row in registry if isinstance(row, dict)),
            'proposed_reviews': len(reviews), 'changed_lists': sum(row.get('before') != row['after'] for row in reviews.values()),
            'edges': sum(len(set(ps)) for ps in graph.values()), 'pending_batches': pending,
            'batches': batches, 'errors': errors, 'cycles': cycles, 'unresolved': unresolved,
            'content_corrections': corrections, 'cross_batch_dependencies': cross_batch}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, default=Path(__file__).resolve().parents[1] / 'tmp/full-review')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    result = audit(args.directory)
    output = json.dumps(result, indent=2) + '\n'
    if args.report:
        args.report.write_text(output)
        print(json.dumps({k: result[k] for k in ['ok', 'nodes', 'originally_reviewed', 'proposed_reviews', 'changed_lists', 'edges', 'pending_batches']}, indent=2))
        print(f"Errors: {len(result['errors'])}; cycles: {len(result['cycles'])}; unresolved: {len(result['unresolved'])}")
    else:
        print(output, end='')
    return 0 if result['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
