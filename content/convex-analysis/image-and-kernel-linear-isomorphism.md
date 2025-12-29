---
title: "Image, kernel, and linear isomorphism"
description: "The image and kernel of a linear operator; bijective linear maps are isomorphisms"
---

Let $T:X\to Y$ be a {{< knowl id="linear-operator-linear-transformation" text="linear operator" >}} between vector spaces.

- The **image** of $T$ is
  $$
  \operatorname{im}T:=T(X)=\{T(x)\mid x\in X\}\subset Y.
  $$
- The **kernel** of $T$ is
  $$
  \ker T:=T^{-1}(\{0\})=\{x\in X\mid T(x)=0\}\subset X.
  $$

If $T$ is bijective (one-to-one and onto), then $T$ is a **linear isomorphism**, and we say that $X$ and $Y$ are **isomorphic**, written $X\cong Y$.

Both $\ker T$ and $\operatorname{im}T$ are {{< knowl id="linear-subspace" text="linear subspaces" >}} (see {{< knowl id="images-and-preimages-of-subspaces-under-linear-operators" text="images and preimages of subspaces" >}}). The quotient $X/\ker T$ is canonically isomorphic to $\operatorname{im}T$ (see {{< knowl id="isomorphism-theorem-and-dimension-formula-for-linear-operators" text="the isomorphism theorem" >}}).

**Examples:**
- If $T:\mathbb{R}^2\to\mathbb{R}$ is $T(x,y)=x+y$, then $\ker T=\{(t,-t):t\in\mathbb{R}\}$ and $\operatorname{im}T=\mathbb{R}$.
- If $T=\mathrm{id}_X$, then $\ker T=\{0\}$ and $\operatorname{im}T=X$; $T$ is an isomorphism.
