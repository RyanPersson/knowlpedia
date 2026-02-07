---
title: "Theorem: Pullback of a principal bundle is a principal bundle"
description: "The pullback construction sends principal bundles to principal bundles functorially in the base map."
---

Let $f:N\to M$ be a {{< knowl id="smooth-map" text="smooth map" >}} between smooth manifolds, and let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure {{< knowl id="lie-group" text="Lie group" >}} $G$.

## Theorem (pullback principal bundle)

Define the pullback total space
\[
f^*P := \{(n,p)\in N\times P \mid f(n)=\pi(p)\},
\]
with projection $\pi_N:f^*P\to N$ given by $\pi_N(n,p)=n$. Equip $f^*P$ with the right $G$-action
\[
(n,p)\cdot g := (n,p\cdot g).
\]
Then $\pi_N:f^*P\to N$ is a principal $G$-bundle, called the **pullback bundle** of $P$ along $f$.

Moreover, this construction is functorial: if $g:L\to N$ is another smooth map, then $(f\circ g)^*P$ is canonically isomorphic to $g^*(f^*P)$ as principal bundles.

## Examples

1. **Pullback of a trivial bundle.** If $P\cong M\times G$, then $f^*P\cong N\times G$ by the evident identification.

2. **Restriction to a submanifold.** If $i:Z\hookrightarrow M$ is an embedding, then $i^*P$ is the restriction of $P$ to $Z$; its total space is $\pi^{-1}(Z)\subset P$.

3. **Pullback along a covering map.** If $f:N\to M$ is a covering and $P\to M$ is nontrivial, $f^*P\to N$ may become trivial; for circle bundles this reflects the effect of the degree of $f$ on the corresponding cohomology class.
