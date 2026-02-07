---
title: "Extension of structure group"
description: "A construction that turns a principal G-bundle into a principal H-bundle using a homomorphism from G to H."
---

Let $P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure group $G$, and let $\varphi:G\to H$ be a smooth homomorphism of {{< knowl id="lie-group" text="Lie groups" >}}.

The **extension of structure group** of $P$ along $\varphi$ is the quotient
\[
P\times_\varphi H := (P\times H)/\sim,
\]
where
\[
(p\cdot g,\; h)\sim (p,\; \varphi(g)\,h).
\]
Write $[p,h]$ for the class of $(p,h)$. The projection map is
\[
[p,h]\longmapsto \pi(p),
\]
and the right $H$-action is
\[
[p,h]\cdot k := [p,hk].
\]
With these structures, $P\times_\varphi H\to M$ is a principal $H$-bundle.

This construction is a special case of an {{< knowl id="associated-bundle" text="associated bundle" >}}: it is the associated bundle to $P$ with fiber $H$ where $G$ acts on $H$ by left multiplication through $\varphi$.

There is a canonical {{< knowl id="principal-bundle-morphism" text="principal bundle morphism" >}}
\[
P\to P\times_\varphi H,\qquad p\mapsto [p,e],
\]
covering $\mathrm{id}_M$.

## Examples
1. **From orthonormal frames to all frames.** The inclusion $SO(n)\hookrightarrow GL(n)$ extends the principal $SO(n)$-bundle of oriented orthonormal frames to the full $GL(n)$-frame bundle.
2. **Nonzero vectors in a line bundle.** Extending a principal $U(1)$-bundle along $U(1)\hookrightarrow \mathbb{C}^\ast$ produces the principal $\mathbb{C}^\ast$-bundle of nonzero vectors in the associated complex line bundle.
3. **From SU(n) to U(n).** Extending a principal $SU(n)$-bundle along $SU(n)\hookrightarrow U(n)$ yields a principal $U(n)$-bundle; geometrically this forgets the determinant-one constraint.
