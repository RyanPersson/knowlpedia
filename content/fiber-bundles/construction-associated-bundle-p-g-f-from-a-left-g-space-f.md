---
title: "Associated bundle from a principal bundle and a left G-space"
description: "Construction of the fiber bundle P×_G F associated to a principal G-bundle and a left G-space."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} and let $F$ be a smooth manifold with a smooth left action of the {{< knowl id="lie-group" text="Lie group" >}} $G$ (a left $G$-space).

**Construction (associated bundle).** Consider $P\times F$ with the right $G$-action
\[
(p,f)\cdot g := (pg, g^{-1}\cdot f).
\]
Define the associated bundle as the quotient
\[
P\times_G F := (P\times F)/G,
\]
and write $[p,f]$ for the equivalence class of $(p,f)$. The projection
\[
\pi_F: P\times_G F \to M,\qquad \pi_F([p,f])=\pi(p),
\]
is well-defined and makes $P\times_G F$ into a smooth fiber bundle with typical fiber $F$.

If $s:U\to P$ is a local section, then
\[
\Phi_s:U\times F\to \pi_F^{-1}(U),\qquad (x,f)\mapsto [s(x),f],
\]
is a bundle trivialization; on overlaps, the transition functions are given by the $G$-action on $F$.

## Examples
1. Taking $F=G$ with left multiplication, $P\times_G G$ is canonically isomorphic to $P$ as a principal $G$-bundle (via $[p,g]\mapsto pg$).
2. Taking $F=G$ with conjugation recovers the {{< knowl id="construction-adjoint-bundle-ad" text="adjoint bundle" >}} $P\times_G G$, a bundle of groups over $M$.
3. If $F$ is a homogeneous space $G/H$, then $P\times_G (G/H)$ is a fiber bundle with fiber $G/H$; reductions of structure group to $H$ can be expressed as sections of this associated bundle.
