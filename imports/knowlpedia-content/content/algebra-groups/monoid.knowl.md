+++
id = "algebra-groups/monoid"
title = "Monoid"
kind = "knowl"
summary = "A semigroup with an identity element"
aliases = ["monoid"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/monoid.md"
+++

A **monoid** is a [[algebra-groups/semigroup|semigroup]] $(M,\cdot)$ together with an element $e\in M$ (called an identity element) such that for every $a\in M$,
$
e\cdot a = a \quad\text{and}\quad a\cdot e = a.
$

Monoids generalize [[algebra-groups/group|groups]] by dropping the requirement that elements have inverses. Many monoids arise from [[shared-foundations/composition|composition]] of endomorphisms (self-maps).

**Examples:**
- $(\mathbb{N},+,0)$ is a monoid.
- $(\mathbb{N},\times,1)$ is a monoid.
- For any set $X$, the set of all [[shared-foundations/function|functions]] $X\to X$ is a monoid under composition, with identity $\mathrm{id}_X$.
- The set of all $n\times n$ real matrices is a monoid under multiplication, with identity matrix $I_n$; it is not a group because not every matrix is invertible.
