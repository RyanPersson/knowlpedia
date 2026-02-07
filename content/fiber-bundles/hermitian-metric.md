---
title: "Hermitian metric"
description: "A smoothly varying Hermitian inner product on the fibers of a complex vector bundle."
---

Let $\pi:E\to M$ be a {{< knowl id="complex-vector-bundle" text="complex vector bundle" >}} over a smooth manifold $M$. A **Hermitian metric** on $E$ is an assignment, for each $x\in M$, of a Hermitian inner product
\[
h_x:E_x\times E_x\to \mathbb C
\]
such that:

1. $h_x$ is complex linear in the second variable and conjugate-linear in the first variable.

2. $h_x(v,w)=\overline{h_x(w,v)}$ for all $v,w\in E_x$.

3. $h_x(v,v)>0$ for all nonzero $v\in E_x$.

4. For any smooth local sections $s,t:U\to E$, the function $x\mapsto h_x(s(x),t(x))$ is smooth on $U$.

In a local frame, the matrix $(h_x(e_i,e_j))$ is a smooth map to positive-definite Hermitian matrices, and transforms under change of frame by the Hermitian congruence rule.

A Hermitian metric is equivalent to a reduction of the structure group to the unitary group, yielding the {{< knowl id="unitary-frame-bundle-reduction" text="unitary frame bundle" >}}.

## Examples
1. **Trivial bundle.** On $M\times\mathbb C^r$, the standard Hermitian form on $\mathbb C^r$ defines a Hermitian metric.

2. **Complexification from a real metric.** If $E_\mathbb R\to M$ is a real bundle with a {{< knowl id="bundle-metric" text="bundle metric" >}} $g$, then its complexification $E_\mathbb R\otimes_\mathbb R\mathbb C$ carries a canonical Hermitian metric obtained by extending $g$ complex bilinearly and then taking the associated sesquilinear form.

3. **Determinant metric.** A Hermitian metric on $E$ induces a Hermitian metric on the determinant line bundle $\det(E)=\Lambda^rE$ by declaring the wedge of an orthonormal frame to have unit norm.
