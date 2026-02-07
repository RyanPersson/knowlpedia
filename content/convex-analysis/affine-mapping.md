---
title: "Affine mapping"
description: "A map of the form x↦Ax+b, i.e., linear plus a translation"
---

Let $X,Y$ be real vector spaces. A mapping $B:X\to Y$ is **affine** if there exist a {{< knowl id="linear-operator-linear-transformation" text="linear mapping" >}} $A:X\to Y$ and a vector $b\in Y$ such that
$$
B(x)=A(x)+b\quad\text{for all }x\in X.
$$

**Context.** Affine maps preserve "straightness": they map {{< knowl id="line-segments-in-a-vector-space" text="line segments" >}} to line segments, and therefore preserve convexity properties (see {{< knowl id="affine-images-and-preimages-of-convex-sets-are-convex" text="affine images/preimages of convex sets" >}}).

**Examples:**
- Any translation $B(x)=x+b$ is affine (take $A=\mathrm{Id}$).
- Any linear map is affine (take $b=0$).
- In $\mathbb{R}^n$, $B(x)=Mx+b$ with a fixed matrix $M$ and vector $b$ is affine.
