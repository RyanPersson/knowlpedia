+++
id = "fiber-bundles/construction-induced-map-on-associated-bundles-from-a-principal-bundle-morphism"
title = "Induced map on associated bundles"
kind = "knowl"
summary = "How a principal bundle morphism induces a map between associated bundles."
aliases = ["construction-induced-map-on-associated-bundles-from-a-principal-bundle-morphism", "Induced map on associated bundles"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/construction-induced-map-on-associated-bundles-from-a-principal-bundle-morphism.md"
+++

Let $P\to M$ and $P'\to M'$ be [[fiber-bundles/principal-g-bundle|principal G-bundles]]. A principal bundle morphism consists of a smooth map [[fiber-bundles/smooth-map|smooth map]] $f:M\to M'$ and a smooth map $\Phi:P\to P'$ such that
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
1. (Pullback trivialization maps) If $P'=P$ and $f=\mathrm{id}_M$, then a gauge transformation $\Phi$ induces a bundle automorphism of any [[fiber-bundles/construction-associated-bundle-p-g-f-from-a-left-g-space-f|associated bundle]] $P\times_G F$ by $[p,u]\mapsto [\Phi(p),u]$.
2. (Vector bundle case) For $F=V$ and $F'=V'$ linear $G$-spaces, a $G$-equivariant linear map $\psi:V\to V'$ yields a vector bundle morphism $P\times_G V\to P'\times_G V'$ covering $f$.
3. (Adjoint functoriality) Taking $F=F'=G$ with conjugation and $\psi=\mathrm{id}$ gives a morphism of [[fiber-bundles/construction-adjoint-bundle-ad|adjoint bundles]] induced from any principal bundle morphism.
