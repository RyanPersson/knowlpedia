+++
id = "lie-groups/special-linear-group"
title = "Special linear group"
kind = "knowl"
summary = "The matrix Lie group SL(n,F) of determinant-1 invertible matrices."
aliases = ["special-linear-group", "Special linear group"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/special-linear-group.md"
+++

For a field $\mathbb F$ equal to $\mathbb R$ or $\mathbb C$, the **special linear group** is
\[
SL(n,\mathbb F)=\{A\in GL(n,\mathbb F): \det(A)=1\},
\]
viewed as a matrix Lie group inside the [[lie-groups/general-linear-group|general linear group]]. It is a closed Lie subgroup (see [[lie-groups/lie-subgroup|Lie subgroup]] and [[lie-groups/closed-subgroup-lie-group|closed subgroup]]), hence a Lie group in its own right. As a manifold, it has dimension $n^2-1$.

Its Lie algebra is the trace-zero matrices,
the [[lie-groups/special-linear-lie-algebra|special linear Lie algebra]] $\mathfrak{sl}_n(\mathbb F)$, and the exponential map restricts to $\exp:\mathfrak{sl}_n(\mathbb F)\to SL(n,\mathbb F)$ (see [[lie-groups/exponential-map-lie-group|exponential map]]). The determinant condition differentiates to the trace condition:
\[
\left.\frac{d}{dt}\right|_{t=0}\det(I+tX)=\mathrm{tr}(X).
\]

The groups $SL(n,\mathbb R)$ and $SL(n,\mathbb C)$ are basic examples of connected linear Lie groups, and they play a central role in semisimple theory (compare [[lie-groups/semisimple-lie-algebra|semisimple Lie algebras]] and the root-theoretic framework starting at [[lie-groups/root-system|root systems]]).
