+++
id = "lie-groups/ados-theorem"
title = "Ado’s theorem"
kind = "knowl"
summary = "Every finite-dimensional Lie algebra over characteristic 0 has a faithful finite-dimensional representation."
aliases = ["ados-theorem", "Ado’s theorem"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/ados-theorem.md"
+++

Let $\mathfrak{g}$ be a finite-dimensional [[lie-groups/lie-algebra|Lie algebra]] over a field of characteristic $0$ (typically $\mathbb{R}$ or $\mathbb{C}$).

**Theorem (Ado).** There exists a finite-dimensional vector space $V$ and an injective [[lie-groups/lie-algebra-homomorphism|Lie algebra homomorphism]]
$$
\rho:\mathfrak{g}\hookrightarrow \mathfrak{gl}(V),
$$

so $\mathfrak{g}$ is isomorphic to a [[lie-groups/lie-subalgebra|Lie subalgebra]] of the [[lie-groups/general-linear-lie-algebra|general linear Lie algebra]].

Equivalently, every finite-dimensional Lie algebra is a “matrix Lie algebra” up to isomorphism.

**Motivation.** Ado’s theorem guarantees that Lie algebra theory can be studied inside $\mathfrak{gl}_n$ using linear algebra. It complements [[lie-groups/lies-third-theorem|Lie’s third theorem]], which integrates Lie algebras to (simply connected) Lie groups, by ensuring that the infinitesimal data can always be realized concretely as endomorphisms.

**Remark.** Given a representation $\rho$ of $\mathfrak{g}$ and a [[lie-groups/simply-connected-lie-group|simply connected Lie group]] $G$ with Lie algebra $\mathfrak{g}$, $\rho$ integrates to a group representation $G\to \mathrm{GL}(V)$; this bridges Ado’s theorem with the study of [[lie-groups/representation-of-a-lie-group|linear Lie groups]].
