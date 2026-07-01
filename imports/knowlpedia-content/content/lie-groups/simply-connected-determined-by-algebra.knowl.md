+++
id = "lie-groups/simply-connected-determined-by-algebra"
title = "Simply connected Lie groups are determined by their Lie algebras"
kind = "knowl"
summary = "Connected simply connected Lie groups with isomorphic Lie algebras are isomorphic as Lie groups."
aliases = ["simply-connected-determined-by-algebra", "Simply connected Lie groups are determined by their Lie algebras"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/simply-connected-determined-by-algebra.md"
+++

A central “uniqueness” principle in Lie theory is:

**Theorem (uniqueness for simply connected groups).**
Let $G$ and $H$ be connected [[lie-groups/simply-connected-lie-group|simply connected Lie groups]]. If their Lie algebras are isomorphic,
\[
\mathrm{Lie}(G)\cong \mathrm{Lie}(H)
\]
(as Lie algebras; see [[lie-groups/lie-algebra-isomorphism|Lie algebra isomorphism]]), then $G$ and $H$ are isomorphic as Lie groups.

More precisely, if $\varphi:\mathfrak g\to\mathfrak h$ is a Lie algebra homomorphism between $\mathfrak g=\mathrm{Lie}(G)$ and $\mathfrak h=\mathrm{Lie}(H)$, then there exists a **unique** Lie group homomorphism $\Phi:G\to H$ such that $d\Phi_e=\varphi$ (see [[lie-groups/differential-is-lie-algebra-homomorphism|differential is a Lie algebra homomorphism]]). When $\varphi$ is an isomorphism, $\Phi$ is an isomorphism.

Existence of a simply connected Lie group integrating a given finite-dimensional Lie algebra is guaranteed by [[lie-groups/lies-third-theorem|Lie’s third theorem]]. The uniqueness above explains why, in practice, one often works “purely algebraically” at the level of Lie algebras and then passes to a canonical global group by taking the [[lie-groups/universal-covering-group|simply connected (universal cover) Lie group]] (see [[lie-groups/universal-covering-group-existence|existence of universal covering groups]]).
