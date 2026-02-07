---
title: "Set"
description: "A fundamental object determined entirely by which elements it contains."
---

A **set** is an object $A$ for which statements of the form $x\in A$ (read “$x$ is an element of $A$”) are meaningful, and whose identity is determined by **extensionality**: for sets $A,B$,
$$
A=B \iff \forall x\,\bigl(x\in A \Leftrightarrow x\in B\bigr).
$$

Many basic constructions in set theory are specified by describing their elements, such as {{< knowl id="union" text="union" >}}, {{< knowl id="intersection" text="intersection" >}}, and the {{< knowl id="power-set" text="power set" >}}.

**Examples:**
- The set of natural numbers $\mathbb{N}$ (see {{< knowl id="natural-numbers" text="natural numbers" >}}).
- For a real number $a$, the singleton $\{a\}=\{x : x=a\}$ is the set containing exactly the element $a$.
