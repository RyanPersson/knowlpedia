+++
id = "convex-analysis/affine-mapping"
title = "Affine mapping"
kind = "knowl"
summary = "A map of the form x↦Ax+b, i.e., linear plus a translation"
aliases = ["affine-mapping", "Affine mapping"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/affine-mapping.md"
+++

Let $X,Y$ be real vector spaces. A mapping $B:X\to Y$ is **affine** if there exist a [[convex-analysis/linear-operator-linear-transformation|linear mapping]] $A:X\to Y$ and a vector $b\in Y$ such that
$$
B(x)=A(x)+b\quad\text{for all }x\in X.
$$

**Context.** Affine maps preserve "straightness": they map [[convex-analysis/line-segments-in-a-vector-space|line segments]] to line segments, and therefore preserve convexity properties (see [[convex-analysis/affine-images-and-preimages-of-convex-sets-are-convex|affine images/preimages of convex sets]]).

**Examples:**
- Any translation $B(x)=x+b$ is affine (take $A=\mathrm{Id}$).
- Any linear map is affine (take $b=0$).
- In $\mathbb{R}^n$, $B(x)=Mx+b$ with a fixed matrix $M$ and vector $b$ is affine.
