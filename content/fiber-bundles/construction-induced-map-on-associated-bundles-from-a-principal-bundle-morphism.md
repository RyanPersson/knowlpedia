---
title: "Induced map on associated bundles"
description: "How a principal bundle morphism induces a map between associated bundles."
---

Let $P\to M$ and $P'\to M'$ be {{< knowl id="principal-g-bundle" text="principal G-bundles" >}}. A principal bundle morphism consists of a smooth map {{< knowl id="smooth-map" text="smooth map" >}} $f:M\to M'$ and a smooth map $\Phi:P\to P'$ such that
\[
\pi'\circ \Phi = f\circ \pi,\qquad \Phi(pg)=\Phi(p)g\ \text{ for all }g\in G.
\]
Let $F$ and $F'$ be left $G$-spaces, and let $\psi:F\to F'$ be $G$-equivariant.

**Construction.** Define
\[
\Phi\times_G \psi : P\times_G F \to P'\times_G F',\qquad [p,u]\mapsto [\Phi(p),\psi(u)].
\]
This is well-defined (independent of the representative $(p,u)$) and is a smooth bundle map covering $f$:
\[
\pi_{F'}\circ (\Phi\times_G\psi) = f\circ \pi_F.
\]
When $F=F'$ and $\psi=\mathrm{id}$, one gets the induced map on a fixed associated bundle functorially from $\Phi$.

## Examples
1. (Pullback trivialization maps) If $P'=P$ and $f=\mathrm{id}_M$, then a gauge transformation $\Phi$ induces a bundle automorphism of any {{< knowl id="construction-associated-bundle-p-g-f-from-a-left-g-space-f" text="associated bundle" >}} $P\times_G F$ by $[p,u]\mapsto [\Phi(p),u]$.
2. (Vector bundle case) For $F=V$ and $F'=V'$ linear $G$-spaces, a $G$-equivariant linear map $\psi:V\to V'$ yields a vector bundle morphism $P\times_G V\to P'\times_G V'$ covering $f$.
3. (Adjoint functoriality) Taking $F=F'=G$ with conjugation and $\psi=\mathrm{id}$ gives a morphism of {{< knowl id="construction-adjoint-bundle-ad" text="adjoint bundles" >}} induced from any principal bundle morphism.
