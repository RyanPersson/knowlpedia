#!/usr/bin/env python3
"""Check reviewed prerequisite paths and excluded advanced dependencies against source."""
from __future__ import annotations
import argparse
from collections import Counter
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'packages/compiler'))
import knowl_compile as compiler
from graph_algorithms import cycle_witnesses


def prerequisite_closure(graph, start):
    seen = set()
    pending = list(graph.get(start, []))
    while pending:
        node = pending.pop()
        if node in seen:
            continue
        seen.add(node)
        pending.extend(graph.get(node, []))
    return seen


def merge_contracts(contracts):
    """Keep historical batches while checking the latest recorded review of each node."""
    reviews = {}
    paths = []
    forbidden = {}
    require_full_review = False
    for contract in contracts:
        require_full_review = require_full_review or contract.get('require_full_review', False)
        for entry in contract['reviews']:
            previous = reviews.get(entry['id'])
            if previous is None or entry['review_count_before'] >= previous['review_count_before']:
                reviews[entry['id']] = entry
        paths.extend(contract.get('learning_paths', []))
        for node, ancestors in contract.get('forbidden_prerequisite_ancestors', {}).items():
            forbidden.setdefault(node, set()).update(ancestors)
    return {'reviews': list(reviews.values()), 'learning_paths': paths,
            'forbidden_prerequisite_ancestors': forbidden,
            'require_full_review': require_full_review}


def review_coverage(graph, review_counts):
    """Report metadata review coverage, not mathematical correctness of unreviewed content."""
    dependents = {node: set() for node in graph}
    for node, prerequisites in graph.items():
        for prerequisite in prerequisites:
            if prerequisite in dependents:
                dependents[prerequisite].add(node)
    reviewed = {node for node in graph if review_counts.get(node, 0) > 0}
    domains = {}
    for node in graph:
        domain = domains.setdefault(node.split('/')[0], {'total': 0, 'reviewed': 0})
        domain['total'] += 1
        domain['reviewed'] += node in reviewed
    candidates = [{'id': node, 'direct_dependents': len(dependents[node]),
                   'reviewed_direct_dependents': len(dependents[node] & reviewed)}
                  for node in graph if node not in reviewed]
    candidates.sort(key=lambda row: (-row['reviewed_direct_dependents'], -row['direct_dependents'], row['id']))
    return {'total_concepts': len(graph), 'reviewed_concepts': len(reviewed),
            'reviewed_with_all_prerequisites_reviewed': sum(
                prerequisite_closure(graph, node) <= reviewed for node in reviewed),
            'by_domain': dict(sorted(domains.items())), 'next_candidates': candidates[:25]}


def check_contract(graph, review_counts, contract):
    errors = []
    cycles = cycle_witnesses(graph)
    if cycles:
        errors.append(f'Prerequisite graph has {len(cycles)} cyclic components')
    for node, prerequisites in graph.items():
        for prerequisite in prerequisites:
            if prerequisite not in graph:
                errors.append(f'{node}: missing prerequisite {prerequisite}')
    if contract.get('require_full_review', False):
        unreviewed = sorted(node for node in graph if review_counts.get(node, 0) <= 0)
        if unreviewed:
            errors.append(f'Full review required; unreviewed concepts remain: {unreviewed}')
    for entry in contract['reviews']:
        node = entry['id']
        if node not in graph:
            errors.append(f'Reviewed concept is missing: {node}')
        elif review_counts.get(node, 0) < entry['review_count_before'] + 1:
            errors.append(f'{node}: completed review is not recorded')
        if node in graph and 'after' in entry:
            expected = set(entry['after'])
            actual = set(graph[node])
            if actual != expected:
                errors.append(f'{node}: latest review prerequisite list drifted')
    paths = []
    for path in contract['learning_paths']:
        concepts = path['concepts']
        if not concepts:
            errors.append(f"{path['name']}: learning path is empty")
            continue
        for node in concepts:
            if node not in graph:
                errors.append(f"{path['name']}: missing concept {node}")
        for prerequisite, dependent in zip(concepts, concepts[1:]):
            if prerequisite not in prerequisite_closure(graph, dependent):
                errors.append(f"{path['name']}: no prerequisite path from {prerequisite} to {dependent}")
        endpoint = concepts[-1]
        closure = prerequisite_closure(graph, endpoint)
        unreviewed = sorted(node for node in closure if review_counts.get(node, 0) == 0)
        if len(unreviewed) > path.get('max_unreviewed_prerequisites', len(unreviewed)):
            errors.append(f"{path['name']}: unreviewed prerequisites exceed the recorded limit: {unreviewed}")
        paths.append({'name': path['name'], 'endpoint': endpoint,
                      'prerequisite_count': len(closure),
                      'unreviewed_prerequisite_count': len(unreviewed),
                      'unreviewed_prerequisites': unreviewed})
    for node, forbidden in contract['forbidden_prerequisite_ancestors'].items():
        if node not in graph:
            errors.append(f'Excluded-ancestor target is missing: {node}')
        closure = prerequisite_closure(graph, node)
        for advanced in forbidden:
            if advanced in closure:
                errors.append(f'{node}: advanced dependency reintroduced: {advanced}')
    return {'ok': not errors, 'reviewed_concepts': len(contract['reviews']),
            'paths': paths, 'errors': errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--content-package', type=Path, default=Path(__file__).resolve().parents[2] / 'knowlpedia-content')
    parser.add_argument('--review', type=Path, action='append', help='Review contract; repeat for several batches. Defaults to all dependency-*-review.json files in the package.')
    parser.add_argument('--report', type=Path)
    parser.add_argument('--coverage', action='store_true', help='Include corpus review coverage and the next unreviewed dependency candidates.')
    args = parser.parse_args()
    try:
        reviews = args.review or sorted(args.content_package.glob('dependency-*-review.json'))
        if not reviews:
            raise ValueError('No dependency review contracts found')
        contract = merge_contracts([json.loads(review.read_text()) for review in reviews])
        package = compiler.read_toml(args.content_package / 'knowlpack.toml')
        knowls, _ = compiler.discover_package_knowls(args.content_package, package, compiler.BUILD_PROFILES['development'])
        duplicates = [node for node, count in Counter(k.id for k in knowls).items() if count > 1]
        if duplicates:
            raise ValueError(f'Duplicate knowl IDs: {duplicates}')
        graph = {k.id: [compiler.split_target(p)[0] for p in k.prerequisites] for k in knowls}
        counts = {k.id: k.dependency_review_count for k in knowls}
        result = check_contract(graph, counts, contract)
        result['review_batches'] = [review.name for review in reviews]
        if args.coverage:
            result['coverage'] = review_coverage(graph, counts)
    except (OSError, ValueError, KeyError) as error:
        print(str(error), file=sys.stderr)
        return 2
    output = json.dumps(result, indent=2) + '\n'
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(output)
    else:
        print(output, end='')
    return 0 if result['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
