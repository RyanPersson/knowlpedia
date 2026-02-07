---
title: "Chern character via Chern–Weil theory"
description: "A characteristic class of complex vector bundles defined as the trace of the exponential of curvature; it is additive under direct sum."
---

Let $M$ be a {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let $E\to M$ be a complex vector bundle equipped with a {{< knowl id="connection-on-a-vector-bundle" text="connection" >}} $\nabla$ with {{< knowl id="curvature" text="curvature" >}} $F_\nabla\in\Omega^2(M;\mathrm{End}(E))$.

## Definition (Chern character form and Chern character)
The **Chern character form** of $\nabla$ is the even differential form
\[
\mathrm{ch}(\nabla)\;:=\;\mathrm{tr}\!\left(\exp\!\Big(\frac{i}{2\pi}F_\nabla\Big)\right)\in\Omega^{\mathrm{even}}(M),
\]
where the exponential is taken as a formal power series and $\mathrm{tr}$ is the fiberwise trace. Writing by degree,
\[
\mathrm{ch}(\nabla)=\mathrm{ch}_0(\nabla)+\mathrm{ch}_1(\nabla)+\mathrm{ch}_2(\nabla)+\cdots,
\qquad \mathrm{ch}_k(\nabla)\in\Omega^{2k}(M).
\]

Then:
1. Each $\mathrm{ch}_k(\nabla)$ is closed: $d\,\mathrm{ch}_k(\nabla)=0$, where $d$ is the {{< knowl id="exterior-derivative" text="exterior derivative" >}}.
2. The de Rham class $[\mathrm{ch}(\nabla)]\in H^{\mathrm{even}}_{\mathrm{dR}}(M)$ is independent of $\nabla$.
3. The **Chern character** $\mathrm{ch}(E)\in H^{\mathrm{even}}(M;\mathbb Q)$ is the rational cohomology class whose image in de Rham cohomology equals $[\mathrm{ch}(\nabla)]$.

The Chern character is natural under pullback: for any {{< knowl id="smooth-map" text="smooth map" >}} $f:N\to M$,
\[
\mathrm{ch}(f^*E)=f^*\mathrm{ch}(E).
\]
It is also additive under direct sum (already at the level of forms): if $\nabla=\nabla_1\oplus\nabla_2$ on $E_1\oplus E_2$, then
\[
\mathrm{ch}(\nabla)=\mathrm{ch}(\nabla_1)+\mathrm{ch}(\nabla_2).
\]

## Examples
1. **Rank.** The degree-zero component is the rank:
   \[
   \mathrm{ch}_0(E)=\mathrm{rank}_{\mathbb C}(E)\in H^0(M;\mathbb Q).
   \]

2. **Line bundles.** For a complex line bundle $L\to M$ with first Chern class $c_1(L)\in H^2(M;\mathbb Z)$,
   \[
   \mathrm{ch}(L)=\exp(c_1(L))=1+c_1(L)+\tfrac12 c_1(L)^2+\cdots
   \]
   in rational cohomology.

3. **Trivial / flat bundles.** If $E$ admits a flat connection ($F_\nabla=0$), then $\mathrm{ch}(\nabla)=\mathrm{rank}(E)$, so $\mathrm{ch}_k(E)=0$ for all $k\ge 1$ in de Rham cohomology.
