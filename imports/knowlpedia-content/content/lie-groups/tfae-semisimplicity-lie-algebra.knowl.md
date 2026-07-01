+++
id = "lie-groups/tfae-semisimplicity-lie-algebra"
title = "Equivalent characterizations of semisimplicity for Lie algebras"
kind = "knowl"
summary = "Semisimplicity is equivalent to nondegeneracy of the Killing form and to decomposition into simple ideals."
aliases = ["tfae-semisimplicity-lie-algebra", "Equivalent characterizations of semisimplicity for Lie algebras"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/tfae-semisimplicity-lie-algebra.md"
+++

### Theorem (TFAE: semisimplicity)
Let $\mathfrak g$ be a finite-dimensional Lie algebra over a field of characteristic $0$ (in particular over $\mathbb R$ or $\mathbb C$). The following are equivalent.

1. **No nonzero solvable ideals:** $\mathfrak g$ is [[lie-groups/semisimple-lie-algebra|semisimple]], i.e. it has no nonzero solvable ideal (equivalently, its radical is $0$).

2. **Nondegenerate Killing form:** the [[lie-groups/killing-form|Killing form]] $\kappa(X,Y)=\mathrm{tr}(\mathrm{ad}_X\mathrm{ad}_Y)$ is nondegenerate; compare [[lie-groups/killing-form-nondegenerate-iff-semisimple|nondegeneracy of the Killing form]].

3. **Direct sum of simple ideals:** $\mathfrak g$ is a (finite) [[lie-groups/direct-sum-of-lie-algebras|direct sum]] of [[lie-groups/simple-lie-algebra|simple Lie algebras]]; see [[lie-groups/semisimple-direct-sum-simple|semisimple equals direct sum of simple ideals]].

4. **Adjoint representation is completely reducible:** the representation $\mathrm{ad}:\mathfrak g\to \mathfrak{gl}(\mathfrak g)$ is [[lie-groups/completely-reducible-representation-lie|completely reducible]].

5. **Cartan-type trace criterion:** $\mathfrak g$ satisfies a trace criterion equivalent to semisimplicity as in [[lie-groups/cartans-criterion-semisimplicity|Cartan’s criterion for semisimplicity]].

### Context
These equivalences are used interchangeably in practice: (2) is often the fastest computational test, while (3) is the structural starting point for classification (compare [[lie-groups/classification-simple-lie-algebras|classification of simple Lie algebras]]). Complete reducibility of representations (see [[lie-groups/weyls-theorem-complete-reducibility|Weyl’s theorem]]) is a major consequence of semisimplicity.
