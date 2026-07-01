+++
id = "algebra-modules/free-module"
title = "Free module"
kind = "knowl"
summary = "A module admitting a basis; equivalently, a direct sum of copies of the ring."
aliases = ["free-module", "Free module"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/free-module.md"
+++

A left $R$-[[algebra-modules/module|module]] $F$ is **free** if it has a [[algebra-modules/basis-module|basis]] $B\subseteq F$, i.e. every element of $F$ admits a unique expression as a finite $R$-linear combination of elements of $B$. Equivalently, $F$ is isomorphic to a [[algebra-modules/direct-sum-modules|direct sum]]
of copies of $R$ indexed by $B$.

Free modules are characterized by the [[algebra-modules/free-module-universal-property|universal property of free modules]]: functions from a basis extend uniquely to module homomorphisms. Over a field, free modules coincide with vector spaces and their bases agree with linear-algebra bases.

**Examples:**
- $R^n$ is a free $R$-module with basis $\{e_1,\dots,e_n\}$.
- $\mathbb Z^n$ is a free $\mathbb Z$-module of rank $n$.
- (Nonexample) $\mathbb Z/2\mathbb Z$ is not free as a $\mathbb Z$-module (it has torsion).
