+++
id = "linear-algebra/eigenvalue"
title = "Eigenvalue"
kind = "knowl"
summary = "A scalar for which a linear operator has a nonzero vector it only scales."
aliases = ["eigenvalue"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/eigenvalue.md"
+++

An **eigenvalue** of a [[linear-algebra/linear-operator|linear operator]] $T:V\to V$ is a scalar $\lambda\in\mathbb{F}$ such that there exists a nonzero vector $v\in V$ with
\[
T(v)=\lambda v.
\]

A vector $v\neq 0$ satisfying this equation is an [[linear-algebra/eigenvector|eigenvector]], and all such vectors (together with $0$) form the [[linear-algebra/eigenspace|eigenspace]] for $\lambda$. Eigenvalues are precisely the roots of the [[linear-algebra/characteristic-polynomial|characteristic polynomial]].

**Examples:**
- For a diagonal matrix $\operatorname{diag}(d_1,\dots,d_n)$, the eigenvalues are $d_1,\dots,d_n$.
- For the projection $P(x,y)=(x,0)$ on $\mathbb{R}^2$, the eigenvalues are $1$ and $0$.
- For the identity operator $I$, the only eigenvalue is $1$.
