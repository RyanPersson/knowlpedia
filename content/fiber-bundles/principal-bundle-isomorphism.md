---
title: "Principal bundle isomorphism"
description: "An invertible principal bundle morphism, equivalently an equivariant diffeomorphism of total spaces covering a base diffeomorphism."
---

Let $\pi:P\to M$ and $\pi':P'\to M'$ be {{< knowl id="principal-g-bundle" text="principal G-bundles" >}}.

A **principal bundle isomorphism** is a {{< knowl id="principal-bundle-morphism" text="principal bundle morphism" >}} $\Phi:P\to P'$ such that:
- $\Phi$ is a {{< knowl id="diffeomorphism" text="diffeomorphism" >}} (so it has a smooth inverse), and hence
- the induced base map $f:M\to M'$ defined by $\pi'\circ\Phi=f\circ\pi$ is automatically a diffeomorphism.

Equivalently, $\Phi$ is a morphism admitting an inverse morphism $\Psi:P'\to P$ with $\Psi\circ\Phi=\mathrm{id}_P$ and $\Phi\circ\Psi=\mathrm{id}_{P'}$.

## Examples
1. **Trivialization from a global section.** If $P\to M$ admits a global smooth section $s:M\to P$, then $P$ is isomorphic to the trivial bundle $M\times G$ via $p=s(\pi(p))\cdot g \mapsto (\pi(p),g)$.
2. **Isomorphism from cohomologous transition data.** If two principal bundles over the same base have transition functions related by a coboundary $g'_{ij}=a_i^{-1}g_{ij}a_j$ for smooth $a_i:U_i\to G$, then they are isomorphic (via maps defined locally using the $a_i$).
3. **Change of coordinates on a frame bundle.** A diffeomorphism $f:M\to M$ induces an isomorphism of $\mathrm{Fr}(M)$ with itself covering $f$.
