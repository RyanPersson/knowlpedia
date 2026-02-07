---
title: "Cartan’s criterion for semisimplicity"
description: "A finite-dimensional Lie algebra over characteristic 0 is semisimple iff its Killing form is nondegenerate."
---

Let $\mathfrak{g}$ be a finite-dimensional {{< knowl id="lie-algebra" text="Lie algebra" >}} over a field of characteristic $0$. Let $B$ denote the {{< knowl id="killing-form" text="Killing form" >}} on $\mathfrak{g}$, defined by
$$
B(X,Y)=\mathrm{tr}(\mathrm{ad}_X\circ \mathrm{ad}_Y).
$$

**Theorem (Cartan).** The following are equivalent:
1. $\mathfrak{g}$ is {{< knowl id="semisimple-lie-algebra" text="semisimple" >}}.
2. The Killing form $B$ is nondegenerate on $\mathfrak{g}$, i.e. $B(X,Y)=0$ for all $Y$ implies $X=0$.

**Context.** This criterion is a practical test for semisimplicity: it converts the intrinsic condition “$\mathfrak{g}$ has no nonzero solvable ideals” into a bilinear-algebra statement. It is complementary to {{< knowl id="cartans-criterion-solvability" text="Cartan’s criterion for solvability" >}}, which detects when a Lie algebra is solvable via vanishing of certain traces.

**Remark.** Nondegeneracy of $B$ implies strong structure results, including the decomposition of any semisimple Lie algebra into a {{< knowl id="semisimple-direct-sum-simple" text="direct sum of simple ideals" >}}.
