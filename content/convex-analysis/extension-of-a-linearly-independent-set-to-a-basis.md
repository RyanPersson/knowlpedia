---
title: "Extension of a linearly independent set to a basis"
description: "Any nonempty linearly independent set sits inside some Hamel basis"
---

**Theorem (Extension to a basis).**
Let $X$ be a vector space and let $M\subset X$ be a nonempty {{< knowl id="linearly-independent-and-linearly-dependent-sets" text="linearly independent" >}} set. Then there exists a {{< knowl id="basis-hamel-basis-and-dimension" text="basis" >}} $B$ of $X$ such that $B\supset M$.

**Context.** The standard proof uses Zorn's Lemma (and hence the Axiom of Choice). Combined with the characterization of bases as maximal independent sets (see {{< knowl id="basis-characterized-by-maximal-linear-independence" text="maximal independence" >}}), it yields the existence of bases in general vector spaces.

**Proof sketch.** Consider the collection of all linearly independent subsets of $X$ that contain $M$, ordered by inclusion. Any chain has an upper bound given by the union of the chain, which is still independent. Zorn's Lemma gives a maximal element $B$. Maximality and the cited proposition imply that $B$ is a basis containing $M$.
