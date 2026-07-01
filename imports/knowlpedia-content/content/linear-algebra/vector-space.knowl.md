+++
id = "linear-algebra/vector-space"
title = "Vector space"
kind = "knowl"
summary = "A set with addition and scalar multiplication satisfying the vector space axioms."
aliases = ["vector-space", "Vector space"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/vector-space.md"
+++

A **vector space** over a [[real-analysis/field-axioms|field]] $\mathbb{F}$ is a [[shared-foundations/set|set]] $V$ equipped with two operations ([[shared-foundations/function|functions]]) $+:V\times V\to V$ and $\cdot:\mathbb{F}\times V\to V$ such that for all $u,v,w\in V$ and $a,b\in\mathbb{F}$:
\[
\begin{aligned}
&u+v=v+u,\qquad (u+v)+w=u+(v+w),\\
&\exists\,0\in V:\ v+0=v,\qquad \forall v\in V\ \exists\,(-v)\in V:\ v+(-v)=0,\\
&a\cdot(u+v)=a\cdot u+a\cdot v,\qquad (a+b)\cdot v=a\cdot v+b\cdot v,\\
&(ab)\cdot v=a\cdot(b\cdot v),\qquad 1\cdot v=v.
\end{aligned}
\]

Vector spaces are the basic objects studied via [[linear-algebra/linear-map|linear maps]] and invariants such as the [[linear-algebra/determinant|determinant]] and [[linear-algebra/eigenvalue|eigenvalues]] of operators.

**Examples:**
- $\mathbb{R}^n$ with componentwise addition and scalar multiplication is a vector space over $\mathbb{R}$.
- The set of polynomials $\mathbb{F}[x]$ with the usual addition and scalar multiplication is a vector space over $\mathbb{F}$.
- The set of $m\times n$ matrices over $\mathbb{F}$ is a vector space over $\mathbb{F}$.
