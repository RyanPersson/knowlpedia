---
title: "Completely reducible representation"
description: "A representation that splits as a direct sum of irreducible subrepresentations."
---

Let $\rho$ be a finite-dimensional representation, either of a {{< knowl id="lie-algebra" text="Lie algebra" >}} $\mathfrak{g}$ (a {{< knowl id="representation-of-a-lie-algebra" text="Lie algebra representation" >}}) or of a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} $G$ (a {{< knowl id="representation-of-a-lie-group" text="Lie group representation" >}}).

**Definition.** $\rho$ is **completely reducible** if for every invariant subspace $W\subset V$ (a {{< knowl id="subrepresentation-lie-algebra" text="subrepresentation" >}}), there exists an invariant complement $W'\subset V$ such that
$$
V = W \oplus W'
$$
as representations.

Equivalently, $V$ can be written as a finite direct sum of {{< knowl id="irreducible-representation-lie-algebra" text="irreducible" >}} subrepresentations.

**Context and key theorems.**
- If $\mathfrak{g}$ is {{< knowl id="semisimple-lie-algebra" text="semisimple" >}} over $\mathbb{C}$ (or $\mathbb{R}$ with suitable hypotheses), then every finite-dimensional representation is completely reducible; this is {{< knowl id="weyls-theorem-complete-reducibility" text="Weyl’s complete reducibility theorem" >}}.
- If $G$ is {{< knowl id="compact-lie-group" text="compact" >}}, then every finite-dimensional continuous representation is completely reducible, via averaging an inner product (a Lie-group analogue of Maschke’s theorem), and more globally by {{< knowl id="peter-weyl-theorem" text="Peter–Weyl" >}}.

Complete reducibility is the structural reason highest-weight classifications work for compact and semisimple settings.
