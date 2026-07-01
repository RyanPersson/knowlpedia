+++
id = "real-analysis/constraint-set"
title = "Constraint set"
kind = "knowl"
summary = "A subset defined by one or more equations or inequalities that restrict admissible points"
aliases = ["constraint-set", "Constraint set"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/constraint-set.md"
+++

A **constraint set** is a subset of a domain $U\subseteq \mathbb{R}^n$ described by one or more constraints, commonly written as a level set
$$
C=\{x\in U:\ g(x)=c\}=g^{-1}(\{c\}),
$$

where $g:U\to \mathbb{R}^m$ is a [[shared-foundations/function|function]] and $g^{-1}$ denotes [[shared-foundations/preimage|preimage]].

Constraint sets are central in constrained optimization (see [[real-analysis/lagrange-multipliers-theorem|Lagrange multipliers]]). When $c$ is a [[fiber-bundles/regular-value|regular value]] of $g$, the constraint set typically has good local structure and is a natural domain for an [[real-analysis/implicitly-defined-function|implicitly defined function]].

**Examples:**
- The unit circle is the constraint set $\{(x,y)\in\mathbb{R}^2:\ x^2+y^2=1\}$.
- The affine plane in $\mathbb{R}^3$ given by $x+2y-z=0$ is the constraint set $\{(x,y,z): x+2y-z=0\}$.
