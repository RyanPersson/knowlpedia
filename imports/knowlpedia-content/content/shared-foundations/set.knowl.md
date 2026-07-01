+++
id = "shared-foundations/set"
title = "Set"
kind = "knowl"
summary = "A fundamental object determined entirely by which elements it contains."
aliases = ["set"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/set.md"
+++

A **set** is an object $A$ for which statements of the form $x\in A$ (read “$x$ is an element of $A$”) are meaningful, and whose identity is determined by **extensionality**: for sets $A,B$,
$$
A=B \iff \forall x\,\bigl(x\in A \Leftrightarrow x\in B\bigr).
$$

Many basic constructions in set theory are specified by describing their elements, such as [[shared-foundations/union|union]], [[shared-foundations/intersection|intersection]], and the [[shared-foundations/power-set|power set]].

**Examples:**
- The set of natural numbers $\mathbb{N}$ (see [[shared-foundations/natural-numbers|natural numbers]]).
- For a real number $a$, the singleton $\{a\}=\{x : x=a\}$ is the set containing exactly the element $a$.
