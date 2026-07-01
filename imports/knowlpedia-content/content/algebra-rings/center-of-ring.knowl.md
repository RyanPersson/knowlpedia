+++
id = "algebra-rings/center-of-ring"
title = "Center of a ring"
kind = "knowl"
summary = "The subring of elements that commute with every element of the ring."
aliases = ["center-of-ring", "Center of a ring"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/center-of-ring.md"
+++

Let $R$ be a [[algebra-rings/ring|ring]]. The **center** of $R$ is
\[
Z(R)=\{\,z\in R:\forall r\in R,\; zr=rz\,\}.
\]
It is a [[algebra-rings/subring|subring]] of $R$, and in fact a [[algebra-rings/commutative-ring|commutative ring]].

The center measures how far $R$ is from being commutative: $R$ is commutative iff $Z(R)=R$. The center also controls constructions like the [[algebra-rings/opposite-ring|opposite ring]] and scalar actions on modules and representations.

**Examples:**
- If $k$ is a field and $n\ge 1$, then $Z(M_n(k))$ consists of scalar matrices and is isomorphic to $k$.
- The center of the quaternion division ring $\mathbb{H}$ is $\mathbb{R}$.
- In $M_2(k)$, the matrix $\begin{pmatrix}0&1\\0&0\end{pmatrix}$ is not central since it does not commute with all matrices.
