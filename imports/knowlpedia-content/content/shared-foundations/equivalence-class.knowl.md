+++
id = "shared-foundations/equivalence-class"
title = "Equivalence class"
kind = "knowl"
summary = "The set of all elements equivalent to a given element under an equivalence relation."
aliases = ["equivalence-class", "Equivalence class"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/equivalence-class.md"
+++

An **equivalence class** of an element $a\in A$ (with respect to an [[shared-foundations/equivalence-relation|equivalence relation]] $\sim$ on $A$) is the set
$$
[a]=\{x\in A : x\sim a\}.
$$

Equivalence classes are subsets of $A$ that bundle together elements deemed “the same” by $\sim$. The collection of all equivalence classes is the [[shared-foundations/quotient-set|quotient set]] $A/{\sim}=\{[a]: a\in A\}$, and it is a [[shared-foundations/partition|partition]] of $A$.

**Examples:**
- If $\sim$ is congruence modulo $3$ on $\mathbb{Z}$, then $[1]=\{\dots,-5,-2,1,4,7,\dots\}$.
- If $\sim$ is equality on a set $A$, then for each $a\in A$ one has $[a]=\{a\}$.
