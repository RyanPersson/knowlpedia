---
title: "Classification of principal G-bundles by homotopy classes of maps into BG"
description: "Principal G bundles over a paracompact manifold are classified up to isomorphism by homotopy classes of maps into the classifying space BG."
---

Let $G$ be a Lie group and let $M$ be a paracompact smooth manifold. Write $\mathrm{Prin}_G(M)$ for the set of isomorphism classes of {{< knowl id="principal-g-bundle" text="principal G-bundles" >}} over $M$ (isomorphisms are {{< knowl id="principal-bundle-isomorphism" text="principal bundle isomorphisms" >}} covering $\mathrm{id}_M$).

Let $EG \to BG$ be the {{< knowl id="universal-principal-bundle-egbg" text="universal principal G-bundle" >}} over the {{< knowl id="classifying-space-bg" text="classifying space" >}} $BG$. For any continuous map $f \colon M \to BG$, there is a pullback principal $G$-bundle
\[
f^*(EG) \longrightarrow M
\]
constructed via the usual {{< knowl id="construction-pullback-principal-bundle-fp-along-fnm" text="pullback construction" >}} (and guaranteed to be a principal bundle by {{< knowl id="pullback-functoriality-pullback-of-a-principal-bundle-is-a-principal-bundle" text="pullback functoriality for principal bundles" >}}).

## Theorem (classification by maps to BG)
The assignment
\[
[f] \in [M,BG] \longmapsto \big[f^*(EG)\big] \in \mathrm{Prin}_G(M)
\]
is a well-defined bijection from the set of {{< knowl id="homotopy-class-mbg" text="homotopy classes" >}} of maps $M\to BG$ to isomorphism classes of principal $G$-bundles over $M$.

Equivalently:
1. (**Existence**) For every principal $G$-bundle $P\to M$ there exists a (continuous) {{< knowl id="classifying-map-of-a-principal-bundle" text="classifying map" >}} $f_P\colon M\to BG$ such that $P \cong f_P^*(EG)$ as principal $G$-bundles.
2. (**Uniqueness**) If $f,g\colon M\to BG$ are homotopic, then $f^*(EG)\cong g^*(EG)$; conversely, if $f^*(EG)\cong g^*(EG)$ then $f$ and $g$ are homotopic.

## Examples
1. **Contractible base.** If $M$ is contractible, then $[M,BG]$ has one element, so every principal $G$-bundle over $M$ is isomorphic to the {{< knowl id="trivial-principal-bundle-mgm" text="trivial principal bundle" >}}.
2. **Circle and disconnected structure group.** Since $[S^1,BG]\cong \pi_1(BG)\cong \pi_0(G)$, principal $G$-bundles over $S^1$ are classified by connected components of $G$. For instance, with $G=O(1)\cong \{\pm 1\}$ there are two classes; the nontrivial one corresponds (via the usual passage to associated line bundles) to the Möbius bundle.
3. **Hopf bundle as a pullback.** For $G=U(1)$ and $M=S^2$, one has $[S^2,BU(1)]\cong \mathbb{Z}$. Under this identification, the {{< knowl id="hopf-fibration-s3s2-as-a-principal-u-bundle" text="Hopf fibration" >}} represents a generator (so it is a pullback of $EU(1)\to BU(1)$ along a degree-one classifying map).
