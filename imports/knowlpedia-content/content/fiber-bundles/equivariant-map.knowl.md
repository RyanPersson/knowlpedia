+++
id = "fiber-bundles/equivariant-map"
title = "Equivariant map"
kind = "knowl"
summary = "A smooth map between G-manifolds that intertwines the group actions."
aliases = ["equivariant-map", "Equivariant map"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/equivariant-map.md"
+++

Let $G$ act on manifolds $M$ and $N$ (on the left, unless stated otherwise).

A [[fiber-bundles/smooth-map|smooth map]] $f:M\to N$ is **$G$-equivariant** if
\[
f(g\cdot x)=g\cdot f(x)\qquad\text{for all }g\in G,\ x\in M.
\]
If instead $M$ and $N$ carry right actions, equivariance means $f(x\cdot g)=f(x)\cdot g$ for all $g$.

Equivariant maps are precisely morphisms in the category of manifolds with a [[fiber-bundles/smooth-action-of-a-lie-group-on-a-manifold|smooth action]] of $G$. They preserve orbits and stabilizers (up to inclusion): $f(G\cdot x)\subseteq G\cdot f(x)$ and $G_x\subseteq G_{f(x)}$.

## Examples
1. **Bundle projection.** For a principal $G$-bundle $\pi:P\to B$ with right action on $P$ and the trivial action on $B$, the projection is equivariant (it is invariant): $\pi(p\cdot g)=\pi(p)$.
2. **Inversion under conjugation.** For the conjugation action of $G$ on itself, the inversion map $i(g)=g^{-1}$ is equivariant because $i(hgh^{-1})=hg^{-1}h^{-1}$.
3. **Intertwiners of representations.** If $G$ acts linearly on vector spaces $V,W$ (representations), then a linear map $T:V\to W$ is equivariant exactly when $T(\rho_V(g)v)=\rho_W(g)T(v)$ for all $g,v$.
