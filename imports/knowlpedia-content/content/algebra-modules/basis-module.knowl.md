+++
id = "algebra-modules/basis-module"
title = "Basis of a free module"
kind = "knowl"
summary = "A set of elements giving unique finite linear combinations in a free module."
aliases = ["basis-module", "Basis of a free module"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/basis-module.md"
+++

Let $F$ be a [[algebra-modules/free-module|free]] $R$-[[algebra-modules/module|module]]. A **basis** of $F$ is a subset $B\subseteq F$ such that every $x\in F$ can be written uniquely as a finite sum
\[
x=\sum_{b\in B} r_b\, b
\]
with coefficients $r_b\in R$, where all but finitely many $r_b$ are zero. Uniqueness is equivalent to the familiar notions of [[convex-analysis/linearly-independent-and-linearly-dependent-sets|linear independence]] and spanning (compare [[convex-analysis/linear-combination|linear combinations]] in linear algebra).

Bases generalize the concept of a basis in a [[linear-algebra/vector-space|vector space]], but over rings bases can fail to exist even for finitely generated modules.

**Examples:**
- The standard vectors $e_1,\dots,e_n$ form a basis of $R^n$.
- $\{1\}$ is a basis of the free $R$-module $R$.
- (Nonexample) The $\mathbb Z$-module $\mathbb Z/2\mathbb Z$ has no basis, so it is not free.
