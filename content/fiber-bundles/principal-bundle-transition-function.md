---
title: "Principal bundle transition function"
description: "The group-valued cocycle on overlaps that relates two equivariant trivializations of a principal bundle."
---

Fix a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} $\pi:P\to M$ and an {{< knowl id="open-cover" text="open cover" section="topology">}} $\{U_i\}_{i\in I}$ together with {{< knowl id="equivariant-local-trivialization" text="equivariant local trivializations" >}}
\[
\psi_i:\pi^{-1}(U_i)\to U_i\times G.
\]

On an overlap $U_{ij}=U_i\cap U_j$, the **principal bundle transition function** is the (necessarily unique) {{< knowl id="smooth-map" text="smooth map" >}}
\[
g_{ij}:U_{ij}\to G
\]
characterized by either of the equivalent conditions:

- (Trivialization comparison) For all $x\in U_{ij}$ and $h\in G$,
  \[
  \psi_i\circ\psi_j^{-1}(x,h)=(x,\,g_{ij}(x)\,h).
  \]
- (Local section comparison) If $s_i(x)=\psi_i^{-1}(x,e)$ and $s_j(x)=\psi_j^{-1}(x,e)$, then
  \[
  s_j(x)=s_i(x)\cdot g_{ij}(x)\qquad (x\in U_{ij}).
  \]

The functions $g_{ij}$ satisfy the cocycle identities on overlaps:
1. $g_{ii}(x)=e$ on $U_i$,
2. $g_{ij}(x)=g_{ji}(x)^{-1}$ on $U_{ij}$,
3. $g_{ij}(x)\,g_{jk}(x)=g_{ik}(x)$ on triple overlaps $U_i\cap U_j\cap U_k$.

These identities are the compatibility conditions ensuring that the local products $U_i\times G$ glue to a global principal bundle.

## Examples
1. **Trivial bundle.** If $P=M\times G$ with the standard trivializations on each $U_i$, then all transition functions are $g_{ij}\equiv e$.
2. **Möbius band as an $O(1)$-bundle.** Over $S^1$ covered by two arcs, the nontrivial real line bundle has transition function $g_{12}\equiv -1\in O(1)$ on the overlap.
3. **Hopf bundle.** For $S^3\to S^2$ with the usual two-chart cover of $S^2$, the transition function on the overlap (homotopic to the equator) is a nontrivial map $S^1\to S^1$ representing the generator of $\pi_1(S^1)$.
