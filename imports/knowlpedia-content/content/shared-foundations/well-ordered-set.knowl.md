+++
id = "shared-foundations/well-ordered-set"
title = "Well-ordered set"
kind = "knowl"
summary = "A totally ordered set in which every nonempty subset has a least element."
aliases = ["well-ordered-set", "Well-ordered set"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/well-ordered-set.md"
+++

A **well-ordered set** is a [[shared-foundations/set|set]] $X$ equipped with a [[shared-foundations/total-order|total order]] $\le$ such that every nonempty subset $A\subseteq X$ has a least element; that is, there exists $m\in A$ with $m\le a$ for all $a\in A$.

Well-orderings are central in statements like the [[shared-foundations/well-ordering-theorem|well-ordering theorem]], which asserts that every set can be well-ordered. The [[shared-foundations/well-ordering-principle|well-ordering principle]] is the special case asserting that $\mathbb{N}$ is well-ordered by its usual order.

**Examples:**
- With the usual $\le$, the [[shared-foundations/natural-numbers|natural numbers]] form a well-ordered set.
- Any finite set becomes well-ordered after choosing a total order; for instance, $\{a_1,\dots,a_n\}$ is well-ordered by declaring $a_1<a_2<\cdots<a_n$.
