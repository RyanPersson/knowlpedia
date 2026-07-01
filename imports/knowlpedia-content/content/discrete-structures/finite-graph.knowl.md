+++
id = "discrete-structures/finite-graph"
title = "Finite graph"
kind = "knowl"
summary = "A graph with finitely many vertices (and edges)."
aliases = ["finite-graph", "Finite graph"]
domains = ["discrete-structures"]
legacy_source_path = "discrete-structures/finite-graph.md"
+++

A [[discrete-structures/graph-vertex-edge|graph-vertex-edge]] \(G=(V,E)\) is **finite** if its vertex set \(V\) is finite. For a simple graph, this implies \(E\) is finite as well.

If \(|V|=n\) and \(|E|=m\), then for a simple undirected graph,
\[
0 \le m \le \binom{n}{2}.
\]

**Handshaking identity (useful fact).** For a finite simple undirected graph,
\[
\sum_{v\in V}\deg(v)=2|E|.
\]

Finite graphs are the basic setting for many combinatorial arguments and algorithms, and they often arise as finite subgraphs of infinite graphs (for example, finite regions of the lattice [[discrete-structures/lattice-zd|lattice-zd]]).
