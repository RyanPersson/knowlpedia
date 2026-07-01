+++
id = "convex-analysis/codimension-one-subspaces-yield-direct-sum-decompositions"
title = "Codimension-One Subspaces Give Direct Sum Decompositions"
kind = "knowl"
summary = "If codim(L)=1 and x0∉L, then X=L⊕span{x0}."
aliases = ["codimension-one-subspaces-yield-direct-sum-decompositions", "Codimension-One Subspaces Give Direct Sum Decompositions"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/codimension-one-subspaces-yield-direct-sum-decompositions.md"
+++

Let $X$ be a [[linear-algebra/vector-space|vector space]] and let $L\subset X$ be a [[convex-analysis/linear-subspace|subspace]] with [[convex-analysis/codimension|codim(L)]] $=1$. If $x_0\notin L$, then:

**Proposition**:
$$
X = L \oplus \operatorname{span}\{x_0\},
$$

where $\oplus$ denotes the [[convex-analysis/direct-sum-of-subspaces|direct sum]].

**Context:**
This shows that a codimension-one subspace is "one linear dimension short" of the whole space. It is the structural fact behind representing hyperplanes as kernels (or level sets) of nonzero linear functionals.
