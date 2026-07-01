+++
id = "convex-analysis/existence-of-a-functional-attaining-its-norm-at-a-point"
title = "Existence of a Norming Functional"
kind = "knowl"
summary = "For any nonzero z0, there is a bounded functional f with ||f||=1 and f(z0)=||z0||."
aliases = ["existence-of-a-functional-attaining-its-norm-at-a-point", "Existence of a Norming Functional"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/existence-of-a-functional-attaining-its-norm-at-a-point.md"
+++

Let $X$ be a [[convex-analysis/norm-normed-vector-space|normed space]] and let $z_0\in X\setminus\{0\}$.

**Corollary**: There exists a [[convex-analysis/bounded-linear-functional-norm-of-a-functional|bounded linear functional]] $f:X\to\mathbb{K}$ such that
$$
\|f\|=1\quad\text{and}\quad f(z_0)=\|z_0\|.
$$

This is a direct consequence of [[convex-analysis/separation-of-a-point-and-a-subspace|separation of a point and a subspace]] by applying it to $Y=\{0\}$ and $x_0=z_0/\|z_0\|$.
