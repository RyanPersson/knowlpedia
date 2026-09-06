"""Deterministic, iterative algorithms for the authored prerequisite graph.

The compiler keeps prerequisite edges in the learner-facing direction
(``prerequisite -> dependent``).  The public helpers accept a mapping in the
metadata direction (``node -> prerequisites``), which is convenient when
checking source records.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
import heapq


def normalized_adjacency(
    prerequisites: Mapping[str, Iterable[str]],
) -> dict[str, tuple[str, ...]]:
    """Return a stable prerequisite adjacency map, including self edges."""
    materialized = {node: tuple(values) for node, values in prerequisites.items()}
    nodes = set(materialized)
    for values in materialized.values():
        nodes.update(values)
    return {
        node: tuple(sorted(set(materialized.get(node, ()))))
        for node in sorted(nodes)
    }


def strongly_connected_components(
    prerequisites: Mapping[str, Iterable[str]],
) -> list[tuple[str, ...]]:
    """Find all SCCs without recursion (including isolated nodes)."""
    graph = normalized_adjacency(prerequisites)
    reverse: dict[str, list[str]] = {node: [] for node in graph}
    for node, targets in graph.items():
        for target in targets:
            reverse[target].append(node)
    reverse = {node: sorted(values) for node, values in reverse.items()}

    # Iterative postorder DFS (Kosaraju), with an explicit iterator index.
    seen: set[str] = set()
    order: list[str] = []
    for start in graph:
        if start in seen:
            continue
        seen.add(start)
        stack: list[tuple[str, int]] = [(start, 0)]
        while stack:
            node, index = stack[-1]
            if index < len(graph[node]):
                target = graph[node][index]
                stack[-1] = (node, index + 1)
                if target not in seen:
                    seen.add(target)
                    stack.append((target, 0))
            else:
                order.append(node)
                stack.pop()

    components: list[tuple[str, ...]] = []
    seen.clear()
    for start in reversed(order):
        if start in seen:
            continue
        seen.add(start)
        component: list[str] = []
        stack = [start]
        while stack:
            node = stack.pop()
            component.append(node)
            for target in reverse[node]:
                if target not in seen:
                    seen.add(target)
                    stack.append(target)
        components.append(tuple(sorted(component)))
    return sorted(components)


def cycle_components(
    prerequisites: Mapping[str, Iterable[str]],
) -> list[tuple[str, ...]]:
    """Return cyclic SCCs in deterministic order; self loops count as cycles."""
    graph = normalized_adjacency(prerequisites)
    return [
        component
        for component in strongly_connected_components(graph)
        if len(component) > 1 or component[0] in graph[component[0]]
    ]


def cycle_witnesses(
    prerequisites: Mapping[str, Iterable[str]],
) -> list[tuple[str, ...]]:
    """Return one real, deterministic closed walk for each cyclic SCC."""
    graph = normalized_adjacency(prerequisites)
    witnesses: list[tuple[str, ...]] = []
    for component in cycle_components(graph):
        allowed = set(component)
        start = component[0]
        if len(component) == 1:
            witnesses.append((start, start))
            continue
        # Every vertex in a nontrivial SCC can reach the chosen start. Find a
        # stable path from the start back to itself through one outgoing edge.
        for first in graph[start]:
            if first not in allowed:
                continue
            predecessor: dict[str, str | None] = {first: None}
            stack = [first]
            while stack and start not in predecessor:
                node = stack.pop()
                for target in reversed(graph[node]):
                    if target in allowed and target not in predecessor:
                        predecessor[target] = node
                        stack.append(target)
            if start in predecessor:
                reverse_path = [start]
                node = start
                while predecessor[node] is not None:
                    node = predecessor[node]  # type: ignore[assignment]
                    reverse_path.append(node)
                witnesses.append(tuple([start] + list(reversed(reverse_path))))
                break
    return witnesses


def topological_order(
    prerequisites: Mapping[str, Iterable[str]],
) -> tuple[str, ...] | None:
    """Return a stable order, or ``None`` when any cycle exists."""
    graph = normalized_adjacency(prerequisites)
    # Convert metadata direction to prerequisite -> dependent.
    dependents: dict[str, list[str]] = {node: [] for node in graph}
    indegree = {node: len(values) for node, values in graph.items()}
    for node, values in graph.items():
        for prerequisite in values:
            dependents[prerequisite].append(node)
    for values in dependents.values():
        values.sort()
    ready = [node for node, degree in indegree.items() if degree == 0]
    heapq.heapify(ready)
    result: list[str] = []
    while ready:
        node = heapq.heappop(ready)
        result.append(node)
        for dependent in dependents[node]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                heapq.heappush(ready, dependent)
    return tuple(result) if len(result) == len(graph) else None
