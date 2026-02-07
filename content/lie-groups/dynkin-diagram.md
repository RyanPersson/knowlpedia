---
title: "Dynkin diagram"
description: "A graph encoding the angles and relative lengths among simple roots of a semisimple Lie algebra via the Cartan matrix."
---

Let $\mathfrak g$ be a complex {{< knowl id="semisimple-lie-algebra" text="semisimple Lie algebra" >}}. Fix a {{< knowl id="cartan-subalgebra" text="Cartan subalgebra" >}} $\mathfrak h$ and a choice of positive roots in its {{< knowl id="root-system" text="root system" >}}. Let $\Delta=\{\alpha_1,\dots,\alpha_\ell\}$ be the corresponding set of {{< knowl id="simple-root" text="simple roots" >}}.

The **Cartan matrix** $A=(a_{ij})$ (see {{< knowl id="cartan-matrix" text="Cartan matrix" >}}) is defined by
\[
a_{ij} := \langle \alpha_i^\vee,\alpha_j\rangle,
\]
where $\alpha_i^\vee$ is the coroot associated to $\alpha_i$.

The **Dynkin diagram** of $(\mathfrak g,\Delta)$ is the graph with:
- one vertex for each simple root $\alpha_i$;
- between vertices $i$ and $j$:
  - no edge if $a_{ij}a_{ji}=0$,
  - a single, double, or triple edge if $a_{ij}a_{ji}=1,2,3$ respectively;
- if roots have different lengths, the multiple edge is oriented toward the shorter root (equivalently, toward the vertex with larger $|a_{ij}|$).

Up to isomorphism, the Dynkin diagram does not depend on choices beyond the isomorphism class of $\mathfrak g$.

## Why it matters
The diagram packages the essential combinatorics of the root system (angles and length ratios) into a finite graph. The connected Dynkin diagrams classify complex {{< knowl id="simple-lie-algebra" text="simple Lie algebras" >}}; see {{< knowl id="classification-simple-lie-algebras" text="classification of simple Lie algebras" >}}. This is the starting point for describing {{< knowl id="highest-weight-theorem" text="highest-weight" >}} representation theory.
