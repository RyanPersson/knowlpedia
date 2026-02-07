---
title: "Structure of compact connected Lie groups"
description: "A compact connected Lie group is a torus times a compact semisimple group modulo a finite central subgroup."
---

Let $G$ be a {{< knowl id="compact-lie-group" text="compact" >}}, {{< knowl id="connected-lie-group" text="connected" >}} Lie group with Lie algebra $\mathfrak{g}$.

**Theorem (standard structure decomposition).** There exist:
- a torus $T$ (a compact connected abelian Lie group),
- a simply connected compact semisimple Lie group $K$,
- and a finite central subgroup $F\subset T\times K$,

such that
$$
G \cong (T\times K)/F.
$$
On Lie algebras, one has a canonical decomposition
$$
\mathfrak{g} \cong \mathfrak{z}\oplus [\mathfrak{g},\mathfrak{g}],
$$

where $\mathfrak{z}$ is the {{< knowl id="center-of-a-lie-algebra" text="center" >}} of $\mathfrak{g}$ and $[\mathfrak{g},\mathfrak{g}]$ is semisimple (compare {{< knowl id="cartans-criterion-semisimplicity" text="Cartan’s semisimplicity criterion" >}}).

**Context.** The torus factor encodes the abelian part of $G$ (see {{< knowl id="connected-abelian-lie-group-structure" text="connected abelian structure" >}}), while $K$ encodes the “noncommutative core.” The finite quotient reflects the possibility of nontrivial {{< knowl id="center-of-a-lie-group" text="center" >}}; passing to the {{< knowl id="universal-covering-group" text="universal covering group" >}} eliminates this finite ambiguity.

This decomposition is one conceptual reason compact Lie groups have especially rigid representation theory, via {{< knowl id="peter-weyl-theorem" text="Peter–Weyl" >}} and highest-weight methods (see {{< knowl id="highest-weight-theorem" text="the highest weight theorem" >}}).
