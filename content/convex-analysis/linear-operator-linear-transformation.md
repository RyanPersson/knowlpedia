---
title: "Linear operator"
description: "A map between vector spaces preserving addition and scalar multiplication"
---

Let $X$ and $Y$ be vector spaces over the same field $K$.

A function $T:X\to Y$ is a **linear operator** (or **linear transformation**) if:

1. $T(x+u)=T(x)+T(u)$ for all $x,u\in X$,
2. $T(\alpha x)=\alpha T(x)$ for all $\alpha\in K$ and $x\in X$.

Equivalently, $T$ is linear if and only if
$$
T(\alpha x+\beta u)=\alpha T(x)+\beta T(u)\quad\text{for all }\alpha,\beta\in K,\ x,u\in X.
$$

One often writes $Tx$ instead of $T(x)$.

Linear operators are the morphisms of {{< knowl id="vector-space" section="linear-algebra" section="linear-algebra" text="vector spaces" >}}. Their {{< knowl id="image-and-kernel-linear-isomorphism" text="kernels and images" >}} give canonical subspaces, and the associated quotient describes the operator up to isomorphism.

**Examples:**
- Matrix multiplication $T(x)=Ax$ on $K^n$.
- The derivative $D:C^1[a,b]\to C[a,b]$, $Df=f'$ (linear over $\mathbb{R}$).
- The evaluation map $\mathrm{ev}_{x_0}:F(\Omega)\to K$, $\mathrm{ev}_{x_0}(f)=f(x_0)$.
