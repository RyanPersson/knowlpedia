---
title: "Hausdorff space"
description: "A space where any two distinct points have disjoint neighborhoods."
---

A **Hausdorff space** (or **T2 space**) is a {{< knowl id="topological-space" text="topological space" >}} $X$ such that for any distinct points $x\neq y$ there exist {{< knowl id="neighborhood" text="neighborhoods" >}} $U$ of $x$ and $V$ of $y$ with $U\cap V=\varnothing$.
Equivalently, one can require $U$ and $V$ to be disjoint {{< knowl id="open-set" text="open sets" >}}.

Hausdorffness implies {{< knowl id="t1-space" text="T1" >}} and guarantees {{< knowl id="uniqueness-of-limits-hausdorff" text="uniqueness of limits" >}} for {{< knowl id="convergent-sequence" text="convergent sequences" >}}; it also ensures that {{< knowl id="compact-subset-of-hausdorff-is-closed" text="compact subsets are closed" >}}.

**Examples:**
- Every {{< knowl id="metric-space" text="metric space" >}} is Hausdorff.
- An infinite set with the cofinite topology is not Hausdorff.
