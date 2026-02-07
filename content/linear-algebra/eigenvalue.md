---
title: "Eigenvalue"
description: "A scalar for which a linear operator has a nonzero vector it only scales."
---

An **eigenvalue** of a {{< knowl id="linear-operator" text="linear operator" >}} $T:V\to V$ is a scalar $\lambda\in\mathbb{F}$ such that there exists a nonzero vector $v\in V$ with
\[
T(v)=\lambda v.
\]

A vector $v\neq 0$ satisfying this equation is an {{< knowl id="eigenvector" text="eigenvector" >}}, and all such vectors (together with $0$) form the {{< knowl id="eigenspace" text="eigenspace" >}} for $\lambda$. Eigenvalues are precisely the roots of the {{< knowl id="characteristic-polynomial" text="characteristic polynomial" >}}.

**Examples:**
- For a diagonal matrix $\operatorname{diag}(d_1,\dots,d_n)$, the eigenvalues are $d_1,\dots,d_n$.
- For the projection $P(x,y)=(x,0)$ on $\mathbb{R}^2$, the eigenvalues are $1$ and $0$.
- For the identity operator $I$, the only eigenvalue is $1$.
