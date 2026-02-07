---
title: "Adjoint bundle Ad(P)"
description: "The bundle of groups associated to a principal G-bundle via the conjugation action of G on itself."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} for a {{< knowl id="lie-group" text="Lie group" >}} $G$. Let $G$ act on itself on the left by conjugation: $g\cdot h := ghg^{-1}$.

**Construction (adjoint bundle).** The adjoint bundle is the associated bundle
\[
\mathrm{Ad}(P) := P\times_G G,
\]
formed using the conjugation action. Each fiber $\mathrm{Ad}(P)_x$ is canonically a group (isomorphic to $G$, but not canonically identified without choosing a point in $P_x$), and the group law is defined fiberwise by
\[
[p,h_1]\cdot [p,h_2] := [p,h_1h_2],
\]
which is well-defined because conjugation is by group automorphisms.

A choice of local section $s:U\to P$ identifies $\mathrm{Ad}(P)|_U$ with $U\times G$, and changes of section act by conjugation.

## Examples
1. If $P$ is trivial, $P\cong M\times G$, then $\mathrm{Ad}(P)\cong M\times G$ as a bundle of groups.
2. If $G$ is abelian, conjugation is trivial, so $\mathrm{Ad}(P)\cong M\times G$ for every principal $G$-bundle.
3. For the frame bundle of a vector bundle with structure group $\mathrm{GL}(n)$, $\mathrm{Ad}(P)$ encodes the bundle of change-of-frame maps, with fibers identified (after choosing a frame) with $\mathrm{GL}(n)$.
