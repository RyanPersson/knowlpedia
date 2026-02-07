---
title: "Compact Lie algebra is reductive"
description: "The Lie algebra of a compact Lie group splits as center ⊕ semisimple part."
---

Let $G$ be a compact {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} with Lie algebra $\mathfrak g$.

**Theorem (Compact implies reductive).**  
The Lie algebra $\mathfrak g$ is **reductive**: it decomposes as a direct sum of ideals
\[
\mathfrak g \cong Z(\mathfrak g)\oplus [\mathfrak g,\mathfrak g],
\]
where $Z(\mathfrak g)$ is the {{< knowl id="center-of-a-lie-algebra" text="center" >}} (an abelian ideal, compare {{< knowl id="abelian-lie-algebra" text="abelian Lie algebras" >}}) and $[\mathfrak g,\mathfrak g]$ is semisimple (see {{< knowl id="semisimple-lie-algebra" text="semisimple Lie algebra" >}}). In particular, $[\mathfrak g,\mathfrak g]$ has nondegenerate Killing form, while the Killing form of $\mathfrak g$ is negative semidefinite with kernel $Z(\mathfrak g)$ (compare {{< knowl id="killing-form" text="Killing form" >}} and {{< knowl id="killing-form-nondegenerate-iff-semisimple" text="nondegeneracy vs semisimplicity" >}}).

**Idea of proof.**  
Compactness gives an $\mathrm{Ad}(G)$-invariant inner product on $\mathfrak g$ by averaging any inner product over $G$; equivalently, compact $G$ admits a {{< knowl id="compact-lie-group-bi-invariant-metric" text="bi-invariant metric" >}}. With such an inner product, $\mathrm{ad}_x$ is skew-adjoint for all $x$, forcing strong structural constraints that split off the center and make the derived ideal semisimple.

**Context.**  
Reductivity is the Lie-algebra reflection of robust representation theory for compact groups: finite-dimensional representations are completely reducible (compare {{< knowl id="weyls-theorem-complete-reducibility" text="complete reducibility" >}} and {{< knowl id="peter-weyl-theorem" text="Peter–Weyl theorem" >}}).
