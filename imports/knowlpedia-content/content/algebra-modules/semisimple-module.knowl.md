+++
id = "algebra-modules/semisimple-module"
title = "Semisimple module"
kind = "knowl"
summary = "A module that is a direct sum of simple modules; equivalently, all short exact sequences split."
aliases = ["semisimple-module", "Semisimple module"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/semisimple-module.md"
+++

A module $M$ is **semisimple** if it is (isomorphic to) a [[algebra-modules/direct-sum-modules|direct sum]] of [[algebra-modules/simple-module|simple modules]]. Equivalently, every short exact sequence $0\to A\to M\to B\to 0$ is [[algebra-modules/split-exact-sequence|split]]. Another standard characterization is that every submodule of $M$ is a direct summand; see [[algebra-modules/semisimple-direct-summand|semisimple implies direct summand]].

Semisimple modules are precisely those with completely reducible submodule structure; they are the module-theoretic analog of diagonalizable operators in linear algebra.

**Examples:**
- Any vector space over a field is semisimple (as a module over that field).
- As a $\mathbb Z$-module, $(\mathbb Z/p\mathbb Z)^n$ is semisimple for any prime $p$ and integer $n\ge 1$.
- (Nonexample) $\mathbb Z/p^2\mathbb Z$ is not semisimple as a $\mathbb Z$-module.
