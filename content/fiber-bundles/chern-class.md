---
title: "Chern class via Chern–Weil theory"
description: "Characteristic cohomology classes of a complex vector bundle defined from curvature using invariant polynomials."
---

Let $M$ be a {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let $\pi:E\to M$ be a complex vector bundle of rank $n$ equipped with a (linear) {{< knowl id="connection-on-a-vector-bundle" text="connection" >}} $\nabla$. Write $F_\nabla\in\Omega^2(M;\mathrm{End}(E))$ for its {{< knowl id="curvature" text="curvature" >}}.

## Definition (Chern forms and Chern classes)
The **total Chern form** of $\nabla$ is the even differential form
\[
c(\nabla)\;:=\;\det\!\Big(I+\frac{i}{2\pi}F_\nabla\Big)\;\in\;\Omega^{\mathrm{even}}(M),
\]
where the determinant is computed fiberwise after identifying $\mathrm{End}(E)$ with matrices in local frames. Expanding by degree gives
\[
c(\nabla)=1+c_1(\nabla)+\cdots+c_n(\nabla),
\qquad c_k(\nabla)\in\Omega^{2k}(M).
\]

Then:
1. Each $c_k(\nabla)$ is **closed**, i.e. $d\,c_k(\nabla)=0$, where $d$ is the {{< knowl id="exterior-derivative" text="exterior derivative" >}}.
2. The de Rham cohomology class $[c_k(\nabla)]\in H^{2k}_{\mathrm{dR}}(M)$ is **independent of the choice of** $\nabla$.
3. The **$k$th Chern class** $c_k(E)\in H^{2k}(M;\mathbb Z)$ is the unique integral cohomology class whose image under the natural map
\[
H^{2k}(M;\mathbb Z)\longrightarrow H^{2k}(M;\mathbb R)\cong H^{2k}_{\mathrm{dR}}(M)
\]
equals $[c_k(\nabla)]$.

Equivalently, $c_k(E)$ is the characteristic class obtained by the Chern–Weil construction for the structure group $U(n)$ of a Hermitian bundle (or the corresponding {{< knowl id="principal-g-bundle" text="principal bundle" >}} of unitary frames) using the invariant polynomial given by the $k$th elementary symmetric function of eigenvalues.

The Chern classes are natural under pullback: for any {{< knowl id="smooth-map" text="smooth map" >}} $f:N\to M$,
\[
c_k(f^*E)=f^*c_k(E)\in H^{2k}(N;\mathbb Z).
\]

## Examples
1. **Trivial bundle.** If $E\cong M\times\mathbb C^n$ admits the flat connection ($F_\nabla=0$), then $c(\nabla)=1$ and hence $c_k(E)=0$ for all $k\ge 1$.

2. **Complex line bundle.** If $\mathrm{rank}_{\mathbb C}E=1$, then
   \[
   c(\nabla)=1+\frac{i}{2\pi}F_\nabla,
   \]
   so $c_1(E)$ is represented in de Rham cohomology by the real 2-form $\frac{i}{2\pi}F_\nabla$.

3. **Whitney sum behavior (curvature-level).** If $E=E_1\oplus E_2$ with a block-diagonal connection $\nabla=\nabla_1\oplus\nabla_2$, then $F_\nabla$ is block-diagonal and
   \[
   c(\nabla)=c(\nabla_1)\wedge c(\nabla_2),
   \]
   recovering the usual multiplicativity of total Chern classes under direct sum.
