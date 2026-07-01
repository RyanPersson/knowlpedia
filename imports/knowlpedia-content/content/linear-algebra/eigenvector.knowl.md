+++
id = "linear-algebra/eigenvector"
title = "Eigenvector"
kind = "knowl"
summary = "A nonzero vector that is scaled by a linear operator."
aliases = ["eigenvector"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/eigenvector.md"
+++

An **eigenvector** of a [[linear-algebra/linear-operator|linear operator]] $T:V\to V$ is a nonzero vector $v\in V$ for which there exists a scalar $\lambda\in\mathbb{F}$ such that
\[
T(v)=\lambda v.
\]
The corresponding scalar $\lambda$ is an [[linear-algebra/eigenvalue|eigenvalue]] of $T$.

Eigenvectors for a fixed eigenvalue $\lambda$ form the [[linear-algebra/eigenspace|eigenspace]] of $\lambda$, which is a [[linear-algebra/vector-space|vector space]] inside $V$. In an [[linear-algebra/inner-product-space|inner product space]], geometric conditions like [[linear-algebra/orthogonality|orthogonality]] often organize eigenvectors of important classes of operators.

**Examples:**
- For $A=\operatorname{diag}(2,3)$ on $\mathbb{R}^2$, the vector $(1,0)$ is an eigenvector with eigenvalue $2$.
- For the projection $P(x,y)=(x,0)$, the vector $(1,0)$ is an eigenvector with eigenvalue $1$ and $(0,1)$ is an eigenvector with eigenvalue $0$.
- For the scaling map $T(v)=c\,v$, every nonzero vector is an eigenvector with eigenvalue $c$.
