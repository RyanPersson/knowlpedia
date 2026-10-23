#!/usr/bin/env python3
"""Check that a reading page opens its knowls in prerequisite order.

A reading page (for example a ``knowls_open`` learning path) is a sequence of
knowl links. The page respects the dependency graph when every linked knowl
appears after each linked knowl in its prerequisite closure, including
prerequisites reached through knowls the page does not link. Direct
prerequisites that the page never links are reported as entry assumptions.
"""
from __future__ import annotations

import argparse
import heapq
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'packages/compiler'))
import knowl_compile as compiler


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


def check_reading_order(graph, sequence):
    """Return order violations, repeated links and entry assumptions.

    ``graph`` maps each knowl to its direct prerequisites. ``sequence`` lists
    the page's link targets in reading order, repeats included.
    """
    position = {}
    repeated = []
    for index, node in enumerate(sequence):
        if node in position:
            repeated.append(node)
        else:
            position[node] = index
    linked = list(position)
    closures = {node: prerequisite_closure(graph, node) for node in linked}
    violations = [
        {'knowl': node, 'prerequisite': prerequisite,
         'position': position[node], 'prerequisite_position': position[prerequisite]}
        for node in linked
        for prerequisite in sorted(closures[node] & position.keys())
        if position[prerequisite] > position[node]
    ]
    assumptions = {}
    for node in linked:
        for prerequisite in graph.get(node, []):
            if prerequisite not in position:
                assumptions.setdefault(prerequisite, []).append(node)
    return {
        'ok': not violations,
        'linked': len(linked),
        'violations': violations,
        'repeated': sorted(set(repeated)),
        'missing': sorted(node for node in linked if node not in graph),
        'entry_assumptions': {node: sorted(users) for node, users in sorted(assumptions.items())},
    }


def suggested_order(graph, sequence):
    """Return the prerequisite-respecting order closest to the page's order.

    Each step takes the earliest-written knowl whose linked prerequisites have
    all been placed, so a page that already respects the graph is unchanged.
    """
    position = {}
    for index, node in enumerate(sequence):
        position.setdefault(node, index)
    before = {node: prerequisite_closure(graph, node) & position.keys() for node in position}
    after = {node: [] for node in position}
    for node, prerequisites in before.items():
        for prerequisite in prerequisites:
            after[prerequisite].append(node)
    waiting = {node: len(prerequisites) for node, prerequisites in before.items()}
    ready = [(position[node], node) for node, count in waiting.items() if count == 0]
    heapq.heapify(ready)
    order = []
    while ready:
        _, node = heapq.heappop(ready)
        order.append(node)
        for dependent in after[node]:
            waiting[dependent] -= 1
            if waiting[dependent] == 0:
                heapq.heappush(ready, (position[dependent], dependent))
    return order if len(order) == len(position) else None


def page_sequence(knowl, registry):
    """Knowl link targets of a page in reading order, as canonical IDs."""
    sequence = []
    for target in compiler.wikilinks_in_text(knowl.core_markdown):
        base, _ = compiler.split_target(target)
        sequence.append(registry.canonical_id(base) if base in registry else base)
    return sequence


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('page', help='Knowl ID of the reading page')
    parser.add_argument('--content-package', type=Path,
                        default=Path(__file__).resolve().parents[2] / 'knowlpedia-content')
    parser.add_argument('--profile', default='development', choices=sorted(compiler.BUILD_PROFILES))
    parser.add_argument('--suggest', action='store_true',
                        help='Also print the closest prerequisite-respecting order of the linked knowls.')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    package = compiler.read_toml(args.content_package / 'knowlpack.toml')
    knowls, _ = compiler.discover_package_knowls(
        args.content_package, package, compiler.BUILD_PROFILES[args.profile])
    registry, _ = compiler.build_registry(knowls)
    if args.page not in registry:
        print(f'Unknown page: {args.page}', file=sys.stderr)
        return 2
    graph = {k.id: [compiler.split_target(p)[0] for p in k.prerequisites] for k in knowls}
    sequence = page_sequence(registry[args.page], registry)
    result = check_reading_order(graph, sequence)
    result['page'] = args.page
    if args.suggest:
        result['suggested_order'] = suggested_order(graph, sequence)
    output = json.dumps(result, indent=2) + '\n'
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(output)
    else:
        print(output, end='')
    return 0 if result['ok'] and not result['missing'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
