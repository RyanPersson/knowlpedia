+++
id = "lie-groups/semisimple-lie-algebra"
title = "Semisimple Lie algebra"
kind = "knowl"
summary = "A Lie algebra with no nonzero solvable ideals; equivalently, one with nondegenerate Killing form (char 0)."
aliases = ["semisimple-lie-algebra", "Semisimple Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/semisimple-lie-algebra.md"
+++

A finite-dimensional Lie algebra $\mathfrak g$ (over a field of characteristic $0$) is **semisimple** if it has no nonzero solvable ideals. Equivalently, if $\mathrm{Rad}(\mathfrak g)$ denotes the solvable radical, then $\mathfrak g$ is semisimple exactly when $\mathrm{Rad}(\mathfrak g)=0$ (compare [[lie-groups/solvable-lie-algebra|solvable Lie algebra]] and [[lie-groups/ideal-lie-algebra|ideals]]).

A fundamental characterization is:

- **Cartan’s criterion / Killing form test:** in characteristic $0$, $\mathfrak g$ is semisimple if and only if its [[lie-groups/killing-form|Killing form]] is nondegenerate (see [[lie-groups/killing-form-nondegenerate-iff-semisimple|Killing form nondegenerate iff semisimple]], and compare [[lie-groups/cartans-criterion-semisimplicity|Cartan’s criterion]]).

Semisimple Lie algebras are the “non-abelian, non-solvable core” of general Lie algebras. The [[lie-groups/levi-decomposition-theorem|Levi decomposition]] expresses any finite-dimensional Lie algebra as a semidirect product of a semisimple Lie algebra with its solvable radical. Internally, every semisimple Lie algebra splits as a direct sum of [[lie-groups/simple-lie-algebra|simple]] ideals (see [[lie-groups/semisimple-direct-sum-simple|semisimple as a direct sum of simple ideals]]).

For complex semisimple Lie algebras, additional structure is encoded by roots (see [[lie-groups/root-lie-algebra|roots of a Lie algebra]]) and the associated [[lie-groups/root-system|root system]].
