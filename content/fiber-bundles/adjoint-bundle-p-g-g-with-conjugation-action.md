---
title: "Adjoint bundle"
description: "The associated bundle with fiber G where the structure group acts on G by conjugation, yielding a bundle of groups over the base."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} for a {{< knowl id="lie-group" text="Lie group" >}} $G$.

The **adjoint bundle** of $P$ is the associated bundle
\[
\mathrm{Ad}(P):=P\times_G G,
\]
where $G$ acts on itself on the left by conjugation:
\[
g\cdot h := g h g^{-1}.
\]
Each fiber $\mathrm{Ad}(P)_x$ is (noncanonically) isomorphic to $G$, and the group multiplication on $G$ descends to give $\mathrm{Ad}(P)$ the structure of a smooth bundle of groups over $M$.

The group of smooth sections $\Gamma(\mathrm{Ad}(P))$ is naturally identified with the {{< knowl id="gauge-group" text="gauge group" >}} of $P$, and a section can be interpreted as a “gauge function” acting fiberwise (equivalently, as data defining a {{< knowl id="gauge-transformation" text="gauge transformation" >}}).

## Examples
1. **Trivial bundle.** If $P\cong M\times G$, then $\mathrm{Ad}(P)\cong M\times G$ as bundles of groups.
2. **Abelian groups.** If $G$ is abelian, the conjugation action is trivial, so $\mathrm{Ad}(P)\cong M\times G$ for every principal $G$-bundle $P$ (even if $P$ is nontrivial).
3. **Frame bundle interpretation.** If $P$ is the frame bundle of a rank-$n$ vector bundle $E$, then $\mathrm{Ad}(P)$ can be identified with the bundle of fiberwise linear automorphisms $\mathrm{Aut}(E)\to M$ (matrices transform by conjugation under change of frame).
