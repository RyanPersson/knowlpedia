---
title: "Bijective function"
description: "A function that is both injective and surjective."
---

A {{< knowl id="function-map" text="function" >}} $f:X\to Y$ is **bijective** if it is {{< knowl id="injective-function" text="injective" >}} and {{< knowl id="surjective-function" text="surjective" >}}; equivalently,
$$\forall y\in Y,\ \exists!\ x\in X\ \text{such that}\ f(x)=y,$$
where $\exists!$ means "there exists exactly one."

Bijectivity is the precise condition for the existence of an {{< knowl id="inverse-function" text="inverse function" >}} $f^{-1}:Y\to X$ satisfying $f^{-1}(f(x))=x$ and $f(f^{-1}(y))=y$.

**Examples:**
- $f:\mathbb{R}\to\mathbb{R}$, $f(x)=x+1$ is bijective.
- $\exp:\mathbb{R}\to(0,\infty)$ is bijective.
- $x\mapsto x^2$ is not bijective from $\mathbb{R}$ to $\mathbb{R}$ (not injective and not surjective), but it is bijective from $[0,\infty)$ to $[0,\infty)$.
