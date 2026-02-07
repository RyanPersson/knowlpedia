---
title: "Constraint set"
description: "A subset defined by one or more equations or inequalities that restrict admissible points"
---

A **constraint set** is a subset of a domain $U\subseteq \mathbb{R}^n$ described by one or more constraints, commonly written as a level set
$$
C=\{x\in U:\ g(x)=c\}=g^{-1}(\{c\}),
$$

where $g:U\to \mathbb{R}^m$ is a {{< knowl id="function" section="shared-foundations" text="function" >}} and $g^{-1}$ denotes {{< knowl id="preimage" section="shared-foundations" text="preimage" >}}.

Constraint sets are central in constrained optimization (see {{< knowl id="lagrange-multipliers-theorem" text="Lagrange multipliers" >}}). When $c$ is a {{< knowl id="regular-value" text="regular value" section="fiber-bundles">}} of $g$, the constraint set typically has good local structure and is a natural domain for an {{< knowl id="implicitly-defined-function" text="implicitly defined function" >}}.

**Examples:**
- The unit circle is the constraint set $\{(x,y)\in\mathbb{R}^2:\ x^2+y^2=1\}$.
- The affine plane in $\mathbb{R}^3$ given by $x+2y-z=0$ is the constraint set $\{(x,y,z): x+2y-z=0\}$.
