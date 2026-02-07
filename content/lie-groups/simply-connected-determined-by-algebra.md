---
title: "Simply connected Lie groups are determined by their Lie algebras"
description: "Connected simply connected Lie groups with isomorphic Lie algebras are isomorphic as Lie groups."
---

A central “uniqueness” principle in Lie theory is:

**Theorem (uniqueness for simply connected groups).**  
Let $G$ and $H$ be connected {{< knowl id="simply-connected-lie-group" text="simply connected Lie groups" >}}. If their Lie algebras are isomorphic,
\[
\mathrm{Lie}(G)\cong \mathrm{Lie}(H)
\]
(as Lie algebras; see {{< knowl id="lie-algebra-isomorphism" text="Lie algebra isomorphism" >}}), then $G$ and $H$ are isomorphic as Lie groups.

More precisely, if $\varphi:\mathfrak g\to\mathfrak h$ is a Lie algebra homomorphism between $\mathfrak g=\mathrm{Lie}(G)$ and $\mathfrak h=\mathrm{Lie}(H)$, then there exists a **unique** Lie group homomorphism $\Phi:G\to H$ such that $d\Phi_e=\varphi$ (see {{< knowl id="differential-is-lie-algebra-homomorphism" text="differential is a Lie algebra homomorphism" >}}). When $\varphi$ is an isomorphism, $\Phi$ is an isomorphism.

Existence of a simply connected Lie group integrating a given finite-dimensional Lie algebra is guaranteed by {{< knowl id="lies-third-theorem" text="Lie’s third theorem" >}}. The uniqueness above explains why, in practice, one often works “purely algebraically” at the level of Lie algebras and then passes to a canonical global group by taking the {{< knowl id="universal-covering-group" text="simply connected (universal cover) Lie group" >}} (see {{< knowl id="universal-covering-group-existence" text="existence of universal covering groups" >}}).
