+++
id = "convex-analysis/image-and-kernel-linear-isomorphism"
title = "Image, kernel, and linear isomorphism"
kind = "knowl"
summary = "The image and kernel of a linear operator; bijective linear maps are isomorphisms"
aliases = ["image-and-kernel-linear-isomorphism", "Image, kernel, and linear isomorphism"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/image-and-kernel-linear-isomorphism.md"
+++

Let $T:X\to Y$ be a [[convex-analysis/linear-operator-linear-transformation|linear operator]] between vector spaces.

- The **image** of $T$ is
  $$
  \operatorname{im}T:=T(X)=\{T(x)\mid x\in X\}\subset Y.
  $$

- The **kernel** of $T$ is
  $$
  \ker T:=T^{-1}(\{0\})=\{x\in X\mid T(x)=0\}\subset X.
  $$

If $T$ is bijective (one-to-one and onto), then $T$ is a **linear isomorphism**, and we say that $X$ and $Y$ are **isomorphic**, written $X\cong Y$.

Both $\ker T$ and $\operatorname{im}T$ are [[convex-analysis/linear-subspace|linear subspaces]] (see [[convex-analysis/images-and-preimages-of-subspaces-under-linear-operators|images and preimages of subspaces]]). The quotient $X/\ker T$ is canonically isomorphic to $\operatorname{im}T$ (see [[convex-analysis/isomorphism-theorem-and-dimension-formula-for-linear-operators|the isomorphism theorem]]).

**Examples:**
- If $T:\mathbb{R}^2\to\mathbb{R}$ is $T(x,y)=x+y$, then $\ker T=\{(t,-t):t\in\mathbb{R}\}$ and $\operatorname{im}T=\mathbb{R}$.
- If $T=\mathrm{id}_X$, then $\ker T=\{0\}$ and $\operatorname{im}T=X$; $T$ is an isomorphism.
