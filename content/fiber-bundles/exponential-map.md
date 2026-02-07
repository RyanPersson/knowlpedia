---
title: "Exponential map"
description: "The map from a Lie algebra to its Lie group defined by flowing left-invariant vector fields for unit time."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" >}} with Lie algebra {{< knowl id="lie-algebra" text="Lie algebra" section="lie-groups">}} $\mathfrak{g}=T_eG$. For each $X\in\mathfrak{g}$, let $X^L$ denote the left-invariant vector field on $G$ determined by $X$ (so $X^L_e=X$). Let $\gamma_X(t)$ be the integral curve of $X^L$ with initial condition $\gamma_X(0)=e$.

The **(Lie group) exponential map** is
\[
\exp:\mathfrak{g}\to G,\qquad \exp(X)=\gamma_X(1).
\]
It satisfies $\exp(0)=e$ and its differential at $0$ is the identity map on $\mathfrak{g}$. Moreover, $\exp$ is a local diffeomorphism near $0\in\mathfrak{g}$ (so it provides coordinates near the identity in $G$).

## Examples
1. **Matrix groups.** For $G\subset \mathrm{GL}(n,\mathbb{R})$ a matrix Lie group, $\exp$ agrees with the matrix exponential $X\mapsto \sum_{k\ge0}\frac{1}{k!}X^k$ (and lands in $G$ when $X\in\mathfrak{g}$).
2. **Additive group.** For $G=\mathbb{R}^n$ under addition, $\mathfrak{g}\cong\mathbb{R}^n$ and $\exp$ is the identity map.
3. **Circle group.** For $G=S^1\subset\mathbb{C}$, $\mathfrak{g}\cong\mathbb{R}$ and $\exp(t)=e^{it}$ (up to the chosen identification of $\mathfrak{g}$ with $\mathbb{R}$).
