---
title: "Ado’s theorem"
description: "Every finite-dimensional Lie algebra over characteristic 0 has a faithful finite-dimensional representation."
---

Let $\mathfrak{g}$ be a finite-dimensional {{< knowl id="lie-algebra" text="Lie algebra" >}} over a field of characteristic $0$ (typically $\mathbb{R}$ or $\mathbb{C}$).

**Theorem (Ado).** There exists a finite-dimensional vector space $V$ and an injective {{< knowl id="lie-algebra-homomorphism" text="Lie algebra homomorphism" >}}
$$
\rho:\mathfrak{g}\hookrightarrow \mathfrak{gl}(V),
$$

so $\mathfrak{g}$ is isomorphic to a {{< knowl id="lie-subalgebra" text="Lie subalgebra" >}} of the {{< knowl id="general-linear-lie-algebra" text="general linear Lie algebra" >}}.

Equivalently, every finite-dimensional Lie algebra is a “matrix Lie algebra” up to isomorphism.

**Motivation.** Ado’s theorem guarantees that Lie algebra theory can be studied inside $\mathfrak{gl}_n$ using linear algebra. It complements {{< knowl id="lies-third-theorem" text="Lie’s third theorem" >}}, which integrates Lie algebras to (simply connected) Lie groups, by ensuring that the infinitesimal data can always be realized concretely as endomorphisms.

**Remark.** Given a representation $\rho$ of $\mathfrak{g}$ and a {{< knowl id="simply-connected-lie-group" text="simply connected Lie group" >}} $G$ with Lie algebra $\mathfrak{g}$, $\rho$ integrates to a group representation $G\to \mathrm{GL}(V)$; this bridges Ado’s theorem with the study of {{< knowl id="representation-of-a-lie-group" text="linear Lie groups" >}}.
