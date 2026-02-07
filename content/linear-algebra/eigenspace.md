---
title: "Eigenspace"
description: "Set of vectors sent to scalar multiples of themselves for a fixed eigenvalue."
---

An **eigenspace** of a {{< knowl id="linear-operator" text="linear operator" >}} $T:V\to V$ associated to a scalar $\lambda\in\mathbb{F}$ is the set
\[
E_\lambda(T)=\{v\in V:\ T(v)=\lambda v\}.
\]
Equivalently,
\[
E_\lambda(T)=\{v\in V:\ (T-\lambda I)(v)=0\},
\]
where $I$ is the identity operator on $V$.

If $\lambda$ is an {{< knowl id="eigenvalue" text="eigenvalue" >}}, then $E_\lambda(T)$ contains nonzero {{< knowl id="eigenvector" text="eigenvectors" >}}; otherwise it is $\{0\}$. In all cases, $E_\lambda(T)$ is a {{< knowl id="vector-space" text="vector space" >}} under the operations inherited from $V$.

**Examples:**
- For the identity operator $I$ on $V$, the eigenspace for $\lambda=1$ is all of $V$.
- For the projection $P(x,y)=(x,0)$ on $\mathbb{R}^2$, the eigenspace for $\lambda=1$ is $\{(x,0):x\in\mathbb{R}\}$ and for $\lambda=0$ is $\{(0,y):y\in\mathbb{R}\}$.
- For a diagonal matrix $\operatorname{diag}(d_1,\dots,d_n)$, the eigenspace for $\lambda$ is spanned by those standard basis vectors whose diagonal entry equals $\lambda$.
