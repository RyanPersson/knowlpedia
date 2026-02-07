---
title: "Exponential map is a local diffeomorphism"
description: "For any Lie group , is a diffeomorphism from a neighborhood of onto a neighborhood of ."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} with Lie algebra $\mathfrak g$ and {{< knowl id="exponential-map-lie-group" text="exponential map" >}} $\exp:\mathfrak g\to G$.

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
- By the inverse function theorem, this implies local invertibility; the local inverse is the {{< knowl id="logarithm-map" text="logarithm map" >}} $\log:V\to U$.

## Context
This result supplies canonical local coordinates near the identity and underlies the {{< knowl id="baker-campbell-hausdorff-formula" text="Baker–Campbell–Hausdorff formula" >}}, which describes the group law on $V$ in terms of the Lie bracket on $\mathfrak g$ after transporting multiplication through $\log$ and $\exp`.
