+++
id = "topology/hausdorff-space"
title = "Hausdorff space"
kind = "knowl"
summary = "A space where any two distinct points have disjoint neighborhoods."
aliases = ["hausdorff-space", "Hausdorff space"]
domains = ["topology"]
legacy_source_path = "topology/hausdorff-space.md"
+++

A **Hausdorff space** (or **T2 space**) is a [[topology/topological-space|topological space]] $X$ such that for any distinct points $x\neq y$ there exist [[topology/neighborhood|neighborhoods]] $U$ of $x$ and $V$ of $y$ with $U\cap V=\varnothing$.
Equivalently, one can require $U$ and $V$ to be disjoint [[topology/open-set|open sets]].

Hausdorffness implies [[topology/t1-space|T1]] and guarantees [[topology/uniqueness-of-limits-hausdorff|uniqueness of limits]] for [[topology/convergent-sequence|convergent sequences]]; it also ensures that [[topology/compact-subset-of-hausdorff-is-closed|compact subsets are closed]].

**Examples:**
- Every [[topology/metric-space|metric space]] is Hausdorff.
- An infinite set with the cofinite topology is not Hausdorff.
