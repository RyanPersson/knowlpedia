+++
id = "algebra-modules/simple-module"
title = "Simple module"
kind = "knowl"
summary = "A nonzero module with no proper nontrivial submodules."
aliases = ["simple-module", "Simple module"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/simple-module.md"
+++

A (left) $R$-[[algebra-modules/module|module]] $M\ne 0$ is **simple** if its only [[algebra-modules/submodule|submodules]] are $0$ and $M$. Equivalently, $M$ has no [[shared-foundations/proper-subset|proper]] nonzero submodule.

Simple modules are the analogs of "atoms" in module theory: they appear as factors in [[algebra-modules/composition-series-module|composition series]], and semisimplicity is built from direct sums of simples. Over a commutative ring, simple modules are precisely $R/\mathfrak m$ where $\mathfrak m$ is a [[algebra-rings/maximal-ideal|maximal ideal]], hence are vector spaces over the field $R/\mathfrak m$ (compare [[algebra-modules/quotient-module|quotients]]).

**Examples:**
- As a $\mathbb Z$-module, $\mathbb Z/p\mathbb Z$ is simple for prime $p$.
- If $k$ is a field, then any 1-dimensional $k$-vector space is a simple $k$-module.
- (Nonexample) $\mathbb Z/4\mathbb Z$ is not simple as a $\mathbb Z$-module because it has the nontrivial submodule $2\mathbb Z/4\mathbb Z$.
