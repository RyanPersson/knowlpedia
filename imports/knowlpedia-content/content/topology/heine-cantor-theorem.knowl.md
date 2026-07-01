+++
id = "topology/heine-cantor-theorem"
title = "Heine-Cantor theorem"
kind = "knowl"
summary = "A continuous function on a compact metric space is uniformly continuous."
aliases = ["heine-cantor-theorem", "Heine-Cantor theorem"]
domains = ["topology"]
legacy_source_path = "topology/heine-cantor-theorem.md"
+++

The **Heine-Cantor theorem** states: if \(f: K \to Y\) is a [[topology/continuous-map|continuous function]] from a [[topology/compact-set|compact]] [[topology/metric-space|metric space]] \(K\) to a metric space \(Y\), then \(f\) is [[real-analysis/uniform-continuity|uniformly continuous]].

## Statement
For every \(\varepsilon > 0\), there exists \(\delta > 0\) such that for all \(x, y \in K\):
$$
d_K(x, y) < \delta \implies d_Y(f(x), f(y)) < \varepsilon.
$$

The key point is that \(\delta\) depends only on \(\varepsilon\), not on the choice of points \(x, y\).

## Classical version
A continuous function \(f: [a,b] \to \mathbb{R}\) is uniformly continuous.

## Counterexample
\(f(x) = 1/x\) on \((0,1]\) is continuous but not uniformly continuous (domain not compact).
