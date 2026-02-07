---
title: "Triangle inequality"
description: "The fundamental inequality relating the distance between three points in a metric space."
---

The **triangle inequality** states that for any three points \(x, y, z\) in a {{< knowl id="metric-space" section="topology" text="metric space" >}} \((X, d)\):
$$
d(x, z) \leq d(x, y) + d(y, z).
$$

This is one of the defining axioms of a metric.

## Equivalent forms
For vectors in a {{< knowl id="normed-vector-space" section="linear-algebra" text="normed space" >}}:
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
