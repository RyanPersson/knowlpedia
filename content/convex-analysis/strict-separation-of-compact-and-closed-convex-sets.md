---
title: "Strict Separation of Compact and Closed Convex Sets"
description: "Disjoint compact convex and closed convex sets in a normed space admit strict separation by a continuous functional."
---

Let $X$ be a real {{< knowl id="norm-normed-vector-space" text="normed space" >}}. Let $K,F\subset X$ be nonempty {{< knowl id="convex-set" text="convex sets" >}} and assume:
- $K$ is compact,
- $F$ is {{< knowl id="closed-subset" text="closed" >}}, and
- $K\cap F=\emptyset$.

**Theorem**: The sets $K$ and $F$ can be {{< knowl id="strict-separation-by-a-closed-hyperplane" text="strictly separated by a closed hyperplane" >}}. Equivalently, there exists $x^*\in {{< knowl id="dual-space-and-duality-pairing" text="X*" >}}$ such that
$$
\sup_{x\in K}\langle x^*,x\rangle < \inf_{y\in F}\langle x^*,y\rangle.
$$

**Context:**
This is a strong separation result in normed spaces. The proof in the notes applies {{< knowl id="separation-by-closed-hyperplane-under-interior-condition" text="closed hyperplane separation" >}} to a ball around $0$ and a translated difference set $F-K$, using compactness/closedness to guarantee closedness and a positive gap.
