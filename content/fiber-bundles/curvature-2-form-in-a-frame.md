---
title: "Curvature 2-form in a frame"
description: "The matrix of 2-forms computed from a local connection 1-form by dA plus A wedge A."
---

Let $E\to M$ be a vector bundle with connection $\nabla$, and let $U\subset M$ be an open set with a chosen local frame. Let $A$ denote the {{< knowl id="local-connection-1-form" text="local connection 1-form" >}} (connection matrix) on $U$ in that frame.

**Definition.** The curvature 2-form of $\nabla$ in the chosen frame is the matrix $F$ of {{< knowl id="differential-k-form" text="differential 2-forms" >}} on $U$ defined by
\[
F := dA + A\wedge A,
\]
where $d$ is the {{< knowl id="exterior-derivative" text="exterior derivative" >}} applied entrywise and $A\wedge A$ uses matrix multiplication together with the wedge product of forms.

The matrix $F$ represents the curvature operator in the sense that, writing the frame vectors as $e_j$,
\[
R^\nabla(X,Y)e_j = \sum_i F^i{}_j(X,Y)\,e_i,
\]
so $F$ encodes the same information as {{< knowl id="curvature-of-a-vector-bundle-connection" text="the curvature tensor" >}}.

Under a change of frame by a gauge matrix $g:U\to \mathrm{GL}(r)$, the curvature transforms tensorially:
\[
F' = g^{-1} F g.
\]

## Examples
1. **Line bundle.** For rank $1$, the wedge term vanishes (there is no matrix noncommutativity), so $F=dA$ is just the exterior derivative of the connection 1-form.
2. **Trivial connection.** If $A=0$ in some frame, then $F=0$ in that frame and the connection is flat on $U$.
3. **Constant coefficient connection.** If $A=\sum_k A_k\,dx^k$ with constant matrices $A_k$, then $dA=0$ and $F=\sum_{k<\ell}[A_k,A_\ell]\,dx^k\wedge dx^\ell$.
