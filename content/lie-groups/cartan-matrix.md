---
title: "Cartan matrix"
description: "The integer matrix encoding the simple-root geometry of a semisimple Lie algebra."
---

Let $\mathfrak{g}$ be a complex {{< knowl id="semisimple-lie-algebra" text="semisimple Lie algebra" >}}, choose a {{< knowl id="cartan-subalgebra" text="Cartan subalgebra" >}} $\mathfrak{h}$, and let $\Phi\subset \mathfrak{h}^*$ be the associated {{< knowl id="root-system" text="root system" >}}. Fix a set of {{< knowl id="simple-root" text="simple roots" >}} $\Delta=\{\alpha_1,\dots,\alpha_\ell\}$.

Choose any $W$-invariant inner product on the real span of $\Phi$ (for example, the one induced by the {{< knowl id="killing-form" text="Killing form" >}}).

**Definition.** The **Cartan matrix** $A=(a_{ij})_{1\le i,j\le \ell}$ is defined by
$$
a_{ij} \;=\; 2\,\frac{(\alpha_i,\alpha_j)}{(\alpha_j,\alpha_j)}.
$$

**Basic properties.**
- $a_{ii}=2$ for all $i$.
- For $i\ne j$, one has $a_{ij}\in \mathbb{Z}_{\le 0}$, and $a_{ij}=0$ iff $\alpha_i$ is orthogonal to $\alpha_j$.
- The matrix $A$ determines the {{< knowl id="dynkin-diagram" text="Dynkin diagram" >}} (and conversely): the off-diagonal entries record the angles and relative lengths between simple roots.

**Context.** The Cartan matrix is the combinatorial input for the {{< knowl id="classification-simple-lie-algebras" text="classification of complex simple Lie algebras" >}}: connected Dynkin diagrams (or indecomposable Cartan matrices) correspond to simple Lie algebras, while disjoint unions correspond to direct sums.
