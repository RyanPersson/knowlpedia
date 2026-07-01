+++
id = "lie-groups/logarithm-map"
title = "Logarithm map"
kind = "knowl"
summary = "A local inverse to the exponential map near the identity of a Lie group."
aliases = ["logarithm-map", "Logarithm map"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/logarithm-map.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] with Lie algebra $\mathfrak g$.

A **logarithm map** on $G$ is a smooth map
$$
\log:U\to \mathfrak g
$$

defined on an open neighborhood $U$ of the identity element $e\in G$ such that
$$
\exp(\log(g))=g \quad \text{for all } g\in U,
$$

where $\exp:\mathfrak g\to G$ is the [[lie-groups/exponential-map-lie-group|exponential map]].

Equivalently, $\log$ is a (chosen) smooth local inverse to $\exp$ near $0\in\mathfrak g$. Existence follows from [[lie-groups/exponential-local-diffeomorphism|the fact that $\exp$ is a local diffeomorphism at $0$]].

## Basic properties
- $\log(e)=0$ and $d(\log)_e$ is the inverse of $d(\exp)_0=\mathrm{id}_{\mathfrak g}$.
- $\log$ is generally **not** globally defined or single-valued on all of $G$ (even for compact groups).

## Concrete calculation (matrix groups)
If $G\subset \mathrm{GL}(n,\Bbb R)$ is a matrix Lie group and $A$ is sufficiently close to $I$, one has the convergent power series
$$
\log(I+X)=\sum_{k=1}^\infty \frac{(-1)^{k+1}}{k}X^k
\quad\text{for }\|X\|\text{ small},
$$

so for $A$ near $I$,
$$
\log(A)=\log\bigl(I+(A-I)\bigr)=\sum_{k=1}^\infty \frac{(-1)^{k+1}}{k}(A-I)^k.
$$

In particular, for $X\in \mathfrak g$ and $t$ small, $\log(\exp(tX))=tX$.

## Context
The logarithm is useful for “linearizing” group multiplication near the identity. For example, the product of two near-identity elements can be expressed in $\mathfrak g$ using the [[lie-groups/baker-campbell-hausdorff-formula|Baker–Campbell–Hausdorff formula]], which compares $\log(gh)$ to $\log(g)+\log(h)$ with Lie bracket corrections.
