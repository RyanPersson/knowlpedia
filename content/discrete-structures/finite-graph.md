---
title: "Finite graph"
description: "A graph with finitely many vertices (and edges)."
---

A {{< knowl id="graph-vertex-edge" >}} \(G=(V,E)\) is **finite** if its vertex set \(V\) is finite. For a simple graph, this implies \(E\) is finite as well.

If \(|V|=n\) and \(|E|=m\), then for a simple undirected graph,
\[
0 \le m \le \binom{n}{2}.
\]

**Handshaking identity (useful fact).** For a finite simple undirected graph,
\[
\sum_{v\in V}\deg(v)=2|E|.
\]

Finite graphs are the basic setting for many combinatorial arguments and algorithms, and they often arise as finite subgraphs of infinite graphs (for example, finite regions of the lattice {{< knowl id="lattice-zd" >}}).
