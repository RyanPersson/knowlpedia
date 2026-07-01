+++
id = "linear-algebra/compact-operator"
title = "Compact operator"
kind = "knowl"
summary = "A linear operator whose unit ball image has compact closure."
aliases = ["compact-operator", "Compact operator"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/compact-operator.md"
+++

A **compact operator** is a [[linear-algebra/linear-operator|linear operator]] $T:X\to Y$ between [[linear-algebra/normed-vector-space|normed vector spaces]] such that the image of the closed unit ball
\[
B_X=\{x\in X:\|x\|\le 1\}
\]
has compact closure in $Y$.

Equivalently, for every bounded sequence $(x_n)$ in $X$, the sequence $(Tx_n)$ has a [[real-analysis/subsequence|subsequence]] that is a [[topology/convergent-sequence|convergent sequence]] in $Y$. In finite-dimensional normed spaces, every linear operator is compact; compactness becomes a restrictive and useful condition primarily in infinite-dimensional settings.

**Examples:**
- Any operator with finite-dimensional range (a “finite-rank” operator) is compact; for instance, a projection onto the span of finitely many vectors in a [[linear-algebra/hilbert-space|Hilbert space]] is compact.
- Any [[linear-algebra/linear-map|linear map]] between finite-dimensional normed vector spaces is compact.
