---
title: "Compact operator"
description: "A linear operator whose unit ball image has compact closure."
---

A **compact operator** is a {{< knowl id="linear-operator" text="linear operator" >}} $T:X\to Y$ between {{< knowl id="normed-vector-space" text="normed vector spaces" >}} such that the image of the closed unit ball
\[
B_X=\{x\in X:\|x\|\le 1\}
\]
has compact closure in $Y$.

Equivalently, for every bounded sequence $(x_n)$ in $X$, the sequence $(Tx_n)$ has a {{< knowl id="subsequence" section="real-analysis" text="subsequence" >}} that is a {{< knowl id="convergent-sequence" section="topology" text="convergent sequence" >}} in $Y$. In finite-dimensional normed spaces, every linear operator is compact; compactness becomes a restrictive and useful condition primarily in infinite-dimensional settings.

**Examples:**
- Any operator with finite-dimensional range (a “finite-rank” operator) is compact; for instance, a projection onto the span of finitely many vectors in a {{< knowl id="hilbert-space" text="Hilbert space" >}} is compact.
- Any {{< knowl id="linear-map" text="linear map" >}} between finite-dimensional normed vector spaces is compact.
