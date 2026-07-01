+++
id = "shared-foundations/binary-operation"
title = "Binary operation"
kind = "knowl"
summary = "A function that combines two elements of a set to produce another element of the same set"
aliases = ["binary-operation", "Binary operation"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/binary-operation.md"
+++

A **binary operation** on a set $S$ is a [[shared-foundations/function|function]] $*:S\times S\to S$, where $S\times S$ is the [[shared-foundations/cartesian-product|Cartesian product]] of $S$ with itself. The value of $*(x,y)$ is usually written $x*y$.

Binary operations are functions with two inputs that are “closed” in the sense that combining two elements of $S$ produces an element of $S$ again. Many algebraic structures begin with a set equipped with a binary operation.

**Examples:**
- Addition $+:\mathbb{Z}\times\mathbb{Z}\to\mathbb{Z}$ is a binary operation on [[shared-foundations/integers|the integers]].
- For a fixed set $A$, the union map $(S,T)\mapsto S\cup T$ is a binary operation on the [[shared-foundations/power-set|power set]] $\mathcal{P}(A)$, using [[shared-foundations/union|union]] of subsets.
