---
title: "Integrality of Chern classes"
description: "Chern–Weil forms representing Chern classes have integral periods and come from integral cohomology classes."
---

Let $M$ be a {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let $E\to M$ be a complex vector bundle of rank $r$, equipped with a {{< knowl id="connection-on-a-vector-bundle" text="connection on a vector bundle" >}} $\nabla$ with {{< knowl id="curvature" text="curvature" >}} $F_\nabla$.

## Theorem (integrality)

Form the total Chern–Weil representative
\[
c(E,\nabla)\;=\;\det\!\left(I+\frac{i}{2\pi}F_\nabla\right)
\;=\;1+c_1(E,\nabla)+\cdots+c_r(E,\nabla),
\]
where each $c_k(E,\nabla)$ is a closed {{< knowl id="differential-k-form" text="differential form" >}} of degree $2k$ (closed because its {{< knowl id="exterior-derivative" text="exterior derivative" >}} vanishes by Chern–Weil theory and the Bianchi identity).

Then:

1. The de Rham cohomology class $[c_k(E,\nabla)]\in H^{2k}_{\mathrm{dR}}(M)$ is independent of the choice of $\nabla$, and
2. There exists a unique class $c_k(E)\in H^{2k}(M;\mathbb{Z})$ whose image under the change-of-coefficients map
   \[
   H^{2k}(M;\mathbb{Z})\to H^{2k}(M;\mathbb{R})\cong H^{2k}_{\mathrm{dR}}(M)
   \]
   equals $[c_k(E,\nabla)]$.

Equivalently: for every smooth singular $2k$-cycle $\Sigma$ in $M$,
\[
\int_\Sigma c_k(E,\nabla)\in\mathbb{Z}.
\]
This integrality is the precise sense in which Chern classes are “integral” characteristic classes, even though the Chern–Weil representatives are differential forms.

## Examples

1. **Complex line bundles over the 2-sphere.**  
   For a complex line bundle $L\to S^2$ with any connection, the $2$-form $c_1(L,\nabla)=\frac{i}{2\pi}F_\nabla$ satisfies
   \[
   \int_{S^2} \frac{i}{2\pi}F_\nabla \in \mathbb{Z},
   \]
   and that integer is the degree (first Chern number) of $L$.

2. **The tautological line bundle over complex projective space.**  
   For the tautological line bundle $\mathcal{O}(-1)\to \mathbb{CP}^n$, the class $c_1(\mathcal{O}(-1))$ generates $H^2(\mathbb{CP}^n;\mathbb{Z})\cong\mathbb{Z}$. Any Chern–Weil representative integrates to an integer over any embedded $\mathbb{CP}^1\subset\mathbb{CP}^n$.

3. **Direct sums preserve integrality.**  
   If $E=L_1\oplus\cdots\oplus L_r$ is a sum of line bundles, then the total Chern class satisfies
   \[
   c(E)=\prod_{j=1}^r \bigl(1+c_1(L_j)\bigr),
   \]
   so each $c_k(E)$ lies in integral cohomology and is determined by integral products of the $c_1(L_j)$.
