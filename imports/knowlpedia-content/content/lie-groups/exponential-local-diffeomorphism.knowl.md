+++
id = "lie-groups/exponential-local-diffeomorphism"
title = "Exponential map is a local diffeomorphism"
kind = "knowl"
summary = "For any Lie group , is a diffeomorphism from a neighborhood of onto a neighborhood of ."
aliases = ["exponential-local-diffeomorphism", "Exponential map is a local diffeomorphism"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/exponential-local-diffeomorphism.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] with Lie algebra $\mathfrak g$ and [[lie-groups/exponential-map-lie-group|exponential map]] $\exp:\mathfrak g\to G$.

## Theorem
There exist open neighborhoods $U\subset \mathfrak g$ of $0$ and $V\subset G$ of the identity element $e$ such that
\[
\exp:U \longrightarrow V
\]
is a smooth diffeomorphism.

Equivalently, $\exp$ is a local diffeomorphism at $0$.

## Key points
- The differential at the origin is the identity map once we identify $T_0\mathfrak g\cong \mathfrak g$ and $T_eG\cong \mathfrak g$:
  \[
  d(\exp)_0 = \mathrm{id}_{\mathfrak g}.
  \]
- By the inverse function theorem, this implies local invertibility; the local inverse is the [[lie-groups/logarithm-map|logarithm map]] $\log:V\to U$.

## Context
This result supplies canonical local coordinates near the identity and underlies the [[lie-groups/baker-campbell-hausdorff-formula|Baker–Campbell–Hausdorff formula]], which describes the group law on $V$ in terms of the Lie bracket on $\mathfrak g$ after transporting multiplication through $\log$ and $\exp`.
