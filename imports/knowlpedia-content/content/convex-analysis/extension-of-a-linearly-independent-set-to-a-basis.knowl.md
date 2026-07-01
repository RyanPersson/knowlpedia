+++
id = "convex-analysis/extension-of-a-linearly-independent-set-to-a-basis"
title = "Extension of a linearly independent set to a basis"
kind = "knowl"
summary = "Any nonempty linearly independent set sits inside some Hamel basis"
aliases = ["extension-of-a-linearly-independent-set-to-a-basis", "Extension of a linearly independent set to a basis"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/extension-of-a-linearly-independent-set-to-a-basis.md"
+++

**Theorem (Extension to a basis).**
Let $X$ be a vector space and let $M\subset X$ be a nonempty [[convex-analysis/linearly-independent-and-linearly-dependent-sets|linearly independent]] set. Then there exists a [[convex-analysis/basis-hamel-basis-and-dimension|basis]] $B$ of $X$ such that $B\supset M$.

**Context.** The standard proof uses Zorn's Lemma (and hence the Axiom of Choice). Combined with the characterization of bases as maximal independent sets (see [[convex-analysis/basis-characterized-by-maximal-linear-independence|maximal independence]]), it yields the existence of bases in general vector spaces.

**Proof sketch.** Consider the collection of all linearly independent subsets of $X$ that contain $M$, ordered by inclusion. Any chain has an upper bound given by the union of the chain, which is still independent. Zorn's Lemma gives a maximal element $B$. Maximality and the cited proposition imply that $B$ is a basis containing $M$.
