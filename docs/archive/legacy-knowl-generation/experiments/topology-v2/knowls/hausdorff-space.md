---
title: "Hausdorff space"
description: "Separation axiom where distinct points have disjoint neighborhoods"
---

A **Hausdorff space** (or **$T_2$ space**) is a {{< knowl id="topological-space" section="topology-core" text="topological space" >}} $X$ such that for any two distinct points $x,y\in X$, there exist {{< knowl id="open-set" section="topology-core" text="open sets" >}} $U,V\subseteq X$ with $x\in U$, $y\in V$, and $U\cap V=\varnothing$ (equivalently, $x$ and $y$ have disjoint {{< knowl id="neighborhood" section="topology-core" text="neighborhoods" >}}).

Hausdorffness implies {{< knowl id="t1-space" text="T1" >}} and ensures {{< knowl id="uniqueness-of-limits-hausdorff" text="uniqueness of limits" >}} for convergent sequences. It is also the standard separation hypothesis used with {{< knowl id="compact-set" section="topology-compactness" text="compactness" >}}; for example, {{< knowl id="compact-subset-of-hausdorff-is-closed" section="topology-compactness" text="compact subsets of Hausdorff spaces are closed" >}}.

**Examples:**
- Every {{< knowl id="metric-space" section="topology-metric" text="metric space" >}} is Hausdorff.
- Any {{< knowl id="subspace-topology" section="topology-core" text="subspace" >}} of a Hausdorff space is Hausdorff.
- On an infinite set, the cofinite topology is not Hausdorff (any two nonempty open sets intersect).
