+++
id = "shared-foundations/sequence"
title = "Sequence"
kind = "knowl"
summary = "A function from the natural numbers to a set."
aliases = ["sequence"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/sequence.md"
+++

A **sequence** in a [[shared-foundations/set|set]] $X$ is a [[shared-foundations/function|function]] $a:\mathbb{N}\to X$, where $\mathbb{N}$ is the [[shared-foundations/natural-numbers|natural numbers]]. One writes $a_n$ for $a(n)$, so the sequence is denoted $(a_n)_{n\in\mathbb{N}}$.

Thus a sequence is a function with [[shared-foundations/domain|domain]] $\mathbb{N}$ and [[shared-foundations/codomain|codomain]] $X$, and it can be manipulated using standard function constructions such as [[shared-foundations/restriction-of-a-function|restriction]] and [[shared-foundations/composition|composition]].

**Examples:**
- The rule $a_n = 1/(n+1)$ defines a sequence of [[shared-foundations/rational-numbers|rational numbers]].
- The rule $a_n=7$ for all $n\in\mathbb{N}$ defines a constant sequence in $\mathbb{Z}$ (the [[shared-foundations/integers|integers]]).
