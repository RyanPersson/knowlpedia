+++
id = "shared-foundations/indexed-family-of-sets"
title = "Indexed family of sets"
kind = "knowl"
summary = "A collection of sets labeled by elements of an index set."
aliases = ["indexed-family-of-sets", "Indexed family of sets"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/indexed-family-of-sets.md"
+++

An **indexed family of sets** is a [[shared-foundations/function|function]] $A\colon I\to V$ whose domain $I$ is a set (the **index set**) and such that for each $i\in I$, the value $A(i)$ is a set. One writes the family as $(A_i)_{i\in I}$, where $A_i:=A(i)$.

Indexed families unify the notation for operations like [[shared-foundations/union|union]] $\bigcup_{i\in I}A_i$ and [[shared-foundations/intersection|intersection]] $\bigcap_{i\in I}A_i$, which depend on an index set and a set assigned to each index.

**Examples:**
- For $I=\mathbb{N}$, the assignment $n\mapsto\{n\}$ defines a family $(\{n\})_{n\in\mathbb{N}}$.
- For $I=\mathbb{R}$, the assignment $x\mapsto (x,x+1)$ defines a family of intervals $( (x,x+1) )_{x\in\mathbb{R}}$.
