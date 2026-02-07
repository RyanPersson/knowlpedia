---
title: "Eigenvector"
description: "A nonzero vector that is scaled by a linear operator."
---

An **eigenvector** of a {{< knowl id="linear-operator" text="linear operator" >}} $T:V\to V$ is a nonzero vector $v\in V$ for which there exists a scalar $\lambda\in\mathbb{F}$ such that
\[
T(v)=\lambda v.
\]
The corresponding scalar $\lambda$ is an {{< knowl id="eigenvalue" text="eigenvalue" >}} of $T$.

Eigenvectors for a fixed eigenvalue $\lambda$ form the {{< knowl id="eigenspace" text="eigenspace" >}} of $\lambda$, which is a {{< knowl id="vector-space" text="vector space" >}} inside $V$. In an {{< knowl id="inner-product-space" text="inner product space" >}}, geometric conditions like {{< knowl id="orthogonality" text="orthogonality" >}} often organize eigenvectors of important classes of operators.

**Examples:**
- For $A=\operatorname{diag}(2,3)$ on $\mathbb{R}^2$, the vector $(1,0)$ is an eigenvector with eigenvalue $2$.
- For the projection $P(x,y)=(x,0)$, the vector $(1,0)$ is an eigenvector with eigenvalue $1$ and $(0,1)$ is an eigenvector with eigenvalue $0$.
- For the scaling map $T(v)=c\,v$, every nonzero vector is an eigenvector with eigenvalue $c$.
