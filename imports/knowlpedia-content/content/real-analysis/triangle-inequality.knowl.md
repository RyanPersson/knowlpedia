+++
id = "real-analysis/triangle-inequality"
title = "Triangle inequality"
kind = "knowl"
summary = "The fundamental inequality relating the distance between three points in a metric space."
aliases = ["triangle-inequality", "Triangle inequality"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/triangle-inequality.md"
+++

The **triangle inequality** states that for any three points \(x, y, z\) in a [[topology/metric-space|metric space]] \((X, d)\):
$$
d(x, z) \leq d(x, y) + d(y, z).
$$

This is one of the defining axioms of a metric.

## Equivalent forms
For vectors in a [[linear-algebra/normed-vector-space|normed space]]:
$$
\|x + y\| \leq \|x\| + \|y\|.
$$

For real or complex numbers:
$$
|a + b| \leq |a| + |b|.
$$

## Consequences
- **Reverse triangle inequality**: \(\bigl| d(x,y) - d(y,z) \bigr| \leq d(x,z)\).
- **Polygon inequality**: \(d(x_1, x_n) \leq \sum_{i=1}^{n-1} d(x_i, x_{i+1})\).

The name comes from Euclidean geometry: the length of one side of a triangle is at most the sum of the other two sides.
