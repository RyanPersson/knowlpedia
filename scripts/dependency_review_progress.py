#!/usr/bin/env python3
"""Report current semantic reviews; never infer correctness from graph structure."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from packages.compiler import knowl_compile as compiler


def summarize(package, review_dir):
    knowls, _ = compiler.discover_package_knowls(package, compiler.read_toml(package / 'knowlpack.toml'), compiler.BUILD_PROFILES['production'])
    registry, _ = compiler.build_registry(knowls)
    registry = dict(registry)  # Count canonical IDs, not compatibility aliases.
    entries = {}
    for path in sorted(review_dir.glob('*.json')):
        if path.name == 'progress.json':
            continue
        data = json.loads(path.read_text())
        for entry in data.get('reviews', []):
            kid = entry['id']
            if entry['outcome'] not in {'corrected', 'reviewed_unchanged', 'blocked'} or not entry.get('evidence'):
                raise ValueError(f'{path}: invalid review for {kid}')
            entries.setdefault(kid, []).append(entry)
    counts = dict(canonical_entries=len(registry), corrected=0, reviewed_unchanged=0, blocked=0, stale=0, retired=0)
    stale_ids = []
    for kid, records in entries.items():
        if kid not in registry:
            counts['retired'] += 1
            continue
        digest = hashlib.sha256(registry[kid].source_path.read_bytes()).hexdigest()
        current = [record for record in records if record.get('source_sha256') == digest]
        if not current:
            counts['stale'] += 1
            stale_ids.append(kid)
            continue
        # Repeated checks of the same version must not erase a recorded repair.
        # An unresolved finding takes precedence over a successful review.
        outcomes = {record['outcome'] for record in current}
        outcome = next(value for value in ('blocked', 'corrected', 'reviewed_unchanged') if value in outcomes)
        counts[outcome] += 1
    counts['reviewed_current'] = counts['corrected'] + counts['reviewed_unchanged']
    counts['remaining_review'] = counts['canonical_entries'] - counts['reviewed_current']
    return {'counts': counts, 'stale_ids': stale_ids,
            'note': 'Only explicit current-hash semantic reviews count. Graph validity is reported separately.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--content-package', type=Path, required=True)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    result = summarize(args.content_package.resolve(), args.content_package / 'reviews/dependency-structure')
    output = json.dumps(result, indent=2) + '\n'
    if args.report:
        args.report.write_text(output)
    print(output)


if __name__ == '__main__':
    main()
