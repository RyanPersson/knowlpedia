+++
id = "discrete-structures/graph-vertex-edge"
title = "Graph: vertices and edges"
kind = "knowl"
summary = "Defines vertices and edges in a graph, along with incidence and adjacency."
aliases = ["graph-vertex-edge", "Graph: vertices and edges"]
domains = ["discrete-structures"]
legacy_source_path = "discrete-structures/graph-vertex-edge.md"
+++

A **(simple, undirected) graph** is an ordered pair \(G=(V,E)\) where:

- \(V\) is a [[shared-foundations/set|set]] of **vertices** (or **nodes**).
- \(E\) is a set of **edges**, where each edge is a 2-element subset \(\{u,v\}\subseteq V\).

If \(\{u,v\}\in E\), then:

- \(u\) and \(v\) are the **endpoints** of the edge,
- \(u\) and \(v\) are **adjacent** (neighbors), and
- the edge is **incident** to each of its endpoints.

**Common notation.** In a simple undirected graph, the edge \(\{u,v\}\) is often written as \(uv\).

**Degree.** The **degree** of a vertex \(u\) is
\[
\deg(u)=\bigl|\{v\in V : \{u,v\}\in E\}\bigr|.
\]

**Variants.** Depending on context, one may also allow:
- **Directed edges** \((u,v)\) (a directed graph),
- **loops** \(\{u,u\}\), and/or
- **multiple edges** between the same pair of vertices (a multigraph).

Unless stated otherwise, “graph” typically means **simple, undirected**.

A graph is called [[discrete-structures/finite-graph|finite-graph]] if it has finitely many vertices (and hence finitely many edges in the simple case).
