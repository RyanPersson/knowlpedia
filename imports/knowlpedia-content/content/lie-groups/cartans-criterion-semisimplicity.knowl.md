+++
id = "lie-groups/cartans-criterion-semisimplicity"
title = "Cartan’s criterion for semisimplicity"
kind = "knowl"
summary = "A finite-dimensional Lie algebra over characteristic 0 is semisimple iff its Killing form is nondegenerate."
aliases = ["cartans-criterion-semisimplicity", "Cartan’s criterion for semisimplicity"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/cartans-criterion-semisimplicity.md"
+++

Let $\mathfrak{g}$ be a finite-dimensional [[lie-groups/lie-algebra|Lie algebra]] over a field of characteristic $0$. Let $B$ denote the [[lie-groups/killing-form|Killing form]] on $\mathfrak{g}$, defined by
$$
B(X,Y)=\mathrm{tr}(\mathrm{ad}_X\circ \mathrm{ad}_Y).
$$

**Theorem (Cartan).** The following are equivalent:
1. $\mathfrak{g}$ is [[lie-groups/semisimple-lie-algebra|semisimple]].
2. The Killing form $B$ is nondegenerate on $\mathfrak{g}$, i.e. $B(X,Y)=0$ for all $Y$ implies $X=0$.

**Context.** This criterion is a practical test for semisimplicity: it converts the intrinsic condition “$\mathfrak{g}$ has no nonzero solvable ideals” into a bilinear-algebra statement. It is complementary to [[lie-groups/cartans-criterion-solvability|Cartan’s criterion for solvability]], which detects when a Lie algebra is solvable via vanishing of certain traces.

**Remark.** Nondegeneracy of $B$ implies strong structure results, including the decomposition of any semisimple Lie algebra into a [[lie-groups/semisimple-direct-sum-simple|direct sum of simple ideals]].
