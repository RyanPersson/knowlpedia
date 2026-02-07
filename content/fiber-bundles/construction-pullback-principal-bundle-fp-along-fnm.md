---
title: "Construction: pullback principal bundle"
description: "Given a principal bundle P over M and a smooth map f from N to M, the pullback f-star P is a principal bundle over N."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with right action, and let $f:N\to M$ be a {{< knowl id="smooth-map" text="smooth map" >}} between {{< knowl id="smooth-manifold" text="smooth manifolds" >}}.

## Construction (Pullback bundle)
Define the fiber product
\[
f^*P \;:=\;\{(y,p)\in N\times P:\ f(y)=\pi(p)\}.
\]
Let $\pi_N:f^*P\to N$ be projection to the first factor, $\pi_N(y,p)=y$. Define a right $G$-action on $f^*P$ by
\[
(y,p)\cdot g := (y,\ p\cdot g).
\]

Then:
1. $f^*P$ is a smooth manifold and $\pi_N:f^*P\to N$ is a smooth submersion.
2. $(f^*P,\pi_N)$ is a principal $G$-bundle over $N$.
3. There is a canonical $G$-equivariant map $\widetilde f:f^*P\to P$ given by $\widetilde f(y,p)=p$ covering $f$ (i.e. $\pi\circ \widetilde f = f\circ \pi_N$).

This construction is functorial: if $g:K\to N$ is another smooth map, then $(f\circ g)^*P$ is canonically isomorphic to $g^*(f^*P)$ as principal bundles.

## Examples
1. **Restriction to a submanifold.** If $i:U\hookrightarrow M$ is the inclusion of an open set (or an embedded submanifold), then $i^*P\to U$ is the restriction of $P$ to $U$.

2. **Pullback of a trivial bundle.** If $P\cong M\times G$, then $f^*P\cong N\times G$ canonically.

3. **Pullback of local trivializations.** If $P$ is described by transition functions $g_{ij}$ on a cover of $M$, then $f^*P$ is described by the pulled-back transition functions $g_{ij}\circ f$ on the induced cover $\{f^{-1}(U_i)\}$ of $N$.
