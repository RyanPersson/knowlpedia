+++
id = "convex-analysis/existence-of-a-basis-hamel-basis"
title = "Existence of a basis"
kind = "knowl"
summary = "Every nonzero vector space admits a Hamel basis"
aliases = ["existence-of-a-basis-hamel-basis", "Existence of a basis"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/existence-of-a-basis-hamel-basis.md"
+++

**Corollary (Existence of a Hamel basis).**
If $X$ is a vector space with $X\neq\{0\}$, then $X$ has a [[convex-analysis/basis-hamel-basis-and-dimension|basis]], i.e., a Hamel basis.

**Connection to the extension theorem.** Pick any nonzero $x\in X$. Then $\{x\}$ is linearly independent, so [[convex-analysis/extension-of-a-linearly-independent-set-to-a-basis|the extension theorem]] produces a basis containing $\{x\}$.

**Remark.** If $X=\{0\}$ is the trivial vector space, it is standard to declare the empty set to be a basis of $X$ (so that "every vector space has a basis" holds uniformly).

**Examples:**
- $\mathbb{R}^n$ has the standard basis.
- Infinite-dimensional examples (like all sequences) have a Hamel basis, but it typically cannot be written down explicitly.
