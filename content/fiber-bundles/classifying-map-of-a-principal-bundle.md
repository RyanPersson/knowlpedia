---
title: "Classifying map of a principal bundle"
description: "A map from the base into BG whose pullback of EG reproduces a given principal G-bundle."
---

Fix a {{< knowl id="lie-group" text="Lie group" >}} $G$ and a chosen {{< knowl id="universal-principal-bundle-egbg" text="universal principal bundle" >}} $\pi\colon EG\to BG$.

## Definition (Classifying map)
Let $M$ be a {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let $P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}. A **classifying map** for $P$ is a continuous map
\[
c\colon M \longrightarrow BG
\]
such that there is an isomorphism of principal $G$-bundles
\[
P \cong c^{*}(EG).
\]

If $M$ is paracompact (in particular, if $M$ is a smooth manifold), then:

- a classifying map exists, and
- its homotopy class in {{< knowl id="homotopy-class-mbg" text="[M,BG]" >}} is uniquely determined by $P$.

Equivalently, isomorphism classes of principal $G$-bundles correspond to homotopy classes of classifying maps (see {{< knowl id="classification-theorem-principal-g-bundles-over-m-are-classified-by-homotopy-classes-mbg" text="the classification theorem" >}}).

## Examples
1. **Trivial bundle.** For $P=M\times G$, a classifying map can be taken to be constant (and hence null-homotopic).
2. **Hopf fibration.** The principal $U(1)$-bundle $S^3\to S^2$ is classified by a map $S^2\to BU(1)\simeq \mathbb{C}P^\infty$ representing the generator of $H^2(S^2;\mathbb{Z})$.
3. **Frame bundle viewpoint.** The oriented orthonormal frame bundle of a Riemannian $n$-manifold is a principal $SO(n)$-bundle; its classifying map $M\to BSO(n)$ encodes characteristic classes such as the Stiefel–Whitney and Pontryagin classes.
