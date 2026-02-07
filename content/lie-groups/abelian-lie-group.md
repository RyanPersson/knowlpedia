---
title: "Abelian Lie group"
description: "A Lie group with commutative multiplication."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}}.

**Definition.** $G$ is **abelian** if its multiplication is commutative:
$$
gh=hg \quad \text{for all } g,h\in G.
$$

Equivalently, the {{< knowl id="commutator-subgroup-of-a-lie-group" text="commutator subgroup" >}} $[G,G]$ is trivial, or (for connected $G$) its Lie algebra {{< knowl id="lie-algebra-of-a-lie-group" text="$\mathfrak{g}=\mathrm{Lie}(G)$" >}} is an {{< knowl id="abelian-lie-algebra" text="abelian Lie algebra" >}}.

**Motivation.** For abelian $G$, the {{< knowl id="baker-campbell-hausdorff-formula" text="Baker–Campbell–Hausdorff formula" >}} collapses to ordinary addition in the Lie algebra: in exponential coordinates, local multiplication is just $X+Y$. This is one reason connected abelian Lie groups admit an explicit classification (see {{< knowl id="connected-abelian-lie-group-structure" text="structure of connected abelian Lie groups" >}}).

**Remark.** Any {{< knowl id="coset-space" text="quotient" >}} of an abelian Lie group by a closed subgroup is again abelian, and its Lie algebra is a {{< knowl id="quotient-lie-algebra" text="quotient Lie algebra" >}} of $\mathfrak{g}$.
