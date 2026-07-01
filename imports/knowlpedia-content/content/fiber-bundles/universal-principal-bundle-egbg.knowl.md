+++
id = "fiber-bundles/universal-principal-bundle-egbg"
title = "Universal principal bundle EG→BG"
kind = "knowl"
summary = "A canonical principal G-bundle whose pullbacks classify principal G-bundles over paracompact bases."
aliases = ["universal-principal-bundle-egbg", "Universal principal bundle EG→BG"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/universal-principal-bundle-egbg.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]]. A **universal principal bundle** for $G$ consists of a free $G$-space $EG$ that is contractible, together with the quotient space
\[
BG := EG/G,
\]
and the quotient map $\pi\colon EG \to BG$.

## Definition (Universal principal G-bundle)
The map $\pi\colon EG\to BG$ is called a **universal principal $G$-bundle** if:

1. The right $G$-action on $EG$ is free and $\pi$ exhibits $EG$ as a [[fiber-bundles/principal-g-bundle|principal G-bundle]] over $BG$.
2. The total space $EG$ is contractible.
3. (Universal property for paracompact bases) For every paracompact space $X$ (in particular, any [[fiber-bundles/smooth-manifold|smooth manifold]]), every principal $G$-bundle $P\to X$ is isomorphic to a pullback $f^{*}(EG)\to X$ for some map $f\colon X\to BG$. Such an $f$ is a [[fiber-bundles/classifying-map-of-a-principal-bundle|classifying map]], and its homotopy class in [[fiber-bundles/homotopy-class-mbg|[X,BG]]] is determined uniquely by $P$.

The pair $(EG, BG)$ is unique up to $G$-equivariant homotopy equivalence (and $BG$ up to homotopy equivalence).

## Examples
1. **Circle group.** For $G=U(1)$ one model is $EU(1)=S^\infty$ with the free $U(1)$-action by scalar multiplication, and $BU(1)=\mathbb{C}P^\infty$.
2. **A two-point group.** For $G=\mathbb{Z}/2$, take $EG=S^\infty$ with the antipodal action; then $BG=\mathbb{R}P^\infty$.
3. **Classifying bundles over manifolds.** For any principal $G$-bundle $P\to M$ over a smooth manifold $M$, choosing $EG\to BG$ produces a classifying map $M\to BG$ whose pullback recovers $P$ (up to isomorphism).
