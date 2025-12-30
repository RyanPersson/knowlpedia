---
title: "Center of a ring"
description: "The subring of elements that commute with every element of the ring."
---

Let $R$ be a {{< knowl id="ring" text="ring" >}}. The **center** of $R$ is
\[
Z(R)=\{\,z\in R:\forall r\in R,\; zr=rz\,\}.
\]
It is a {{< knowl id="subring" text="subring" >}} of $R$, and in fact a {{< knowl id="commutative-ring" text="commutative ring" >}}.

The center measures how far $R$ is from being commutative: $R$ is commutative iff $Z(R)=R$. The center also controls constructions like the {{< knowl id="opposite-ring" text="opposite ring" >}} and scalar actions on modules and representations.

**Examples:**
- If $k$ is a field and $n\ge 1$, then $Z(M_n(k))$ consists of scalar matrices and is isomorphic to $k$.
- The center of the quaternion division ring $\mathbb{H}$ is $\mathbb{R}$.
- In $M_2(k)$, the matrix $\begin{pmatrix}0&1\\0&0\end{pmatrix}$ is not central since it does not commute with all matrices.