---
title: "Surjective function"
description: "A function whose image equals its codomain."
---

A {{< knowl id="function-map" text="function" >}} $f:X\to Y$ is **surjective** (or **onto**) if
$$\forall y\in Y,\ \exists x\in X\ \text{such that}\ f(x)=y.$$
Equivalently, $f(X)=Y$ (the {{< knowl id="image-range" text="image" >}} equals the {{< knowl id="codomain" text="codomain" >}}).

Surjectivity depends on the specified codomain $Y$, not just on the rule $x\mapsto f(x)$. Many constructions in analysis naturally produce surjections (e.g., quotient maps, parameterizations) and surjectivity is required for an {{< knowl id="inverse-function" text="inverse" >}} to be defined on all of $Y$.

**Examples:**
- $\sin:\mathbb{R}\to[-1,1]$ is surjective.
- The same rule $\sin:\mathbb{R}\to\mathbb{R}$ is not surjective since no real $x$ satisfies $\sin x = 2$.
- $f:\mathbb{R}\to[0,\infty)$, $f(x)=x^2$ is surjective.
