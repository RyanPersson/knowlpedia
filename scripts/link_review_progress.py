#!/usr/bin/env python3
"""Count source-hash-verified linking reviews separately from audit discovery."""
import argparse
from collections import Counter
import json
from pathlib import Path


def summarize(audit, ledger, *, include_containers=False):
    inventory = {i['id']: i for i in audit['inventory'] if include_containers or i['kind'] not in {'document', 'index', 'page', 'section'}}
    latest = {}
    for entry in ledger['reviews']:
        if entry.get('outcome') not in {'corrected', 'reviewed_unchanged', 'blocked'}:
            raise ValueError('review outcome must be corrected, reviewed_unchanged, or blocked')
        if not entry.get('evidence', '').strip() or not entry.get('source_sha256'):
            raise ValueError('each review needs evidence and the post-review source_sha256')
        if entry['id'] not in inventory:
            raise ValueError(f"unknown or ineligible knowl: {entry['id']}")
        latest[entry['id']] = entry
    current = {key: e for key, e in latest.items() if inventory[key]['source_sha256'] == e['source_sha256']}
    outcomes = Counter(e['outcome'] for e in current.values())
    completed = outcomes['corrected'] + outcomes['reviewed_unchanged']
    return dict(eligible_knowls=len(inventory), reviewed_current=completed,
                corrected_current=outcomes['corrected'], reviewed_unchanged_current=outcomes['reviewed_unchanged'],
                blocked_current=outcomes['blocked'], stale_reviews=len(latest)-len(current),
                remaining_review=len(inventory)-completed, automated_findings=audit['counts'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--audit', type=Path, required=True, help='Fresh audit of the current working tree.')
    parser.add_argument('--ledger', type=Path, required=True)
    parser.add_argument('--report', type=Path)
    parser.add_argument('--include-containers', action='store_true', help='Include production documents, indexes, pages and sections in the review scope.')
    args = parser.parse_args()
    result = summarize(json.loads(args.audit.read_text()), json.loads(args.ledger.read_text()), include_containers=args.include_containers)
    text = json.dumps(result, indent=2)+'\n'
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
