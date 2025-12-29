---
title: "Linear map"
description: "A function between vector spaces preserving addition and scalar multiplication."
---

Let $V$ and $W$ be vector spaces over the same field $\mathbb{F}$ (typically $\mathbb{F}=\mathbb{R}$ or $\mathbb{C}$). A {{< knowl id="function-map" text="function" >}} $T:V\to W$ is a **linear map** (or **linear transformation**) if for all $x,y\in V$ and all scalars $\alpha,\beta\in\mathbb{F}$,
$$T(\alpha x+\beta y)=\alpha T(x)+\beta T(y).$$

Linear maps are the morphisms in linear algebra; in analysis they model {{< knowl id="total-derivative-frechet-derivative" text="derivatives" >}} (as best linear approximations) and bounded linear operators (when norms are present). See also {{< knowl id="operator-norm" text="operator norm" >}}.

**Examples:**
- If $A$ is an $m\times n$ real matrix, then $T:\mathbb{R}^n\to\mathbb{R}^m$ defined by $T(x)=Ax$ is linear.
- The derivative operator $D:C^1([a,b])\to C([a,b])$, $D(f)=f'$, is linear.
- The map $f:\mathbb{R}\to\mathbb{R}$ given by $f(x)=x^2$ is not linear.
