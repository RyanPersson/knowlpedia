+++
id = "convex-analysis/basis-characterized-by-maximal-linear-independence"
title = "Bases are maximal linearly independent sets"
kind = "knowl"
summary = "A nonempty set is a basis iff it is linearly independent and maximal for inclusion"
aliases = ["basis-characterized-by-maximal-linear-independence", "Bases are maximal linearly independent sets"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/basis-characterized-by-maximal-linear-independence.md"
+++

**Proposition (Maximal linear independence characterization).**
Let $X$ be a vector space and let $B\subset X$ be nonempty. Then $B$ is a [[convex-analysis/basis-hamel-basis-and-dimension|basis]] of $X$ if and only if:

1. $B$ is [[convex-analysis/linearly-independent-and-linearly-dependent-sets|linearly independent]], and
2. every strict superset $M\supsetneq B$ is linearly dependent.

**Context.** This proposition identifies bases with "maximal independent sets": you cannot add any new vector to $B$ without creating a nontrivial linear dependence.

**Proof sketch.**
- ($\Rightarrow$) If $B$ is a basis and $x\notin B$, then $x$ is a linear combination of elements of $B$, so $\{x\}\cup B$ is dependent; hence any strict superset of $B$ is dependent.
- ($\Leftarrow$) If $B$ is independent and maximal, then for any $x\in X\setminus B$, the set $B\cup\{x\}$ is dependent, so one can solve for $x$ as a linear combination of finitely many elements of $B$; thus $B$ spans $X$.
