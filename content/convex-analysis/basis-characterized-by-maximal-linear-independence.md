---
title: "Bases are maximal linearly independent sets"
description: "A nonempty set is a basis iff it is linearly independent and maximal for inclusion"
---

**Proposition (Maximal linear independence characterization).**
Let $X$ be a vector space and let $B\subset X$ be nonempty. Then $B$ is a {{< knowl id="basis-hamel-basis-and-dimension" text="basis" >}} of $X$ if and only if:

1. $B$ is {{< knowl id="linearly-independent-and-linearly-dependent-sets" text="linearly independent" >}}, and
2. every strict superset $M\supsetneq B$ is linearly dependent.

**Context.** This proposition identifies bases with "maximal independent sets": you cannot add any new vector to $B$ without creating a nontrivial linear dependence.

**Proof sketch.**
- ($\Rightarrow$) If $B$ is a basis and $x\notin B$, then $x$ is a linear combination of elements of $B$, so $\{x\}\cup B$ is dependent; hence any strict superset of $B$ is dependent.
- ($\Leftarrow$) If $B$ is independent and maximal, then for any $x\in X\setminus B$, the set $B\cup\{x\}$ is dependent, so one can solve for $x$ as a linear combination of finitely many elements of $B$; thus $B$ spans $X$.
