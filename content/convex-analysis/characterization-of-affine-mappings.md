---
title: "Characterization of affine mappings"
description: "Affine maps are exactly those that preserve two-point convex combinations"
---

**Proposition.**
A map $B:X\to Y$ between real vector spaces is {{< knowl id="affine-mapping" text="affine" >}} if and only if for all $x_1,x_2\in X$ and all $\lambda\in\mathbb{R}$,
$$
B\big(\lambda x_1+(1-\lambda)x_2\big)=\lambda B(x_1)+(1-\lambda)B(x_2).
$$

**Context.** This shows that "affine" is exactly the property of preserving barycentric combinations of two points (for all real weights).

**Proof sketch.** If $B(x)=A(x)+b$ with $A$ linear, expand both sides and use linearity of $A$. Conversely, define $b:=B(0)$ and $A(x):=B(x)-b$. The identity implies $A(\lambda x)=\lambda A(x)$ and $A(x+y)=A(x)+A(y)$, so $A$ is linear and $B(x)=A(x)+b$.
