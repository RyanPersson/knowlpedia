---
title: "Special linear group"
description: "The matrix Lie group SL(n,F) of determinant-1 invertible matrices."
---

For a field $\mathbb F$ equal to $\mathbb R$ or $\mathbb C$, the **special linear group** is
\[
SL(n,\mathbb F)=\{A\in GL(n,\mathbb F): \det(A)=1\},
\]
viewed as a matrix Lie group inside the {{< knowl id="general-linear-group" text="general linear group" >}}. It is a closed Lie subgroup (see {{< knowl id="lie-subgroup" text="Lie subgroup" >}} and {{< knowl id="closed-subgroup-lie-group" text="closed subgroup" >}}), hence a Lie group in its own right. As a manifold, it has dimension $n^2-1$.

Its Lie algebra is the trace-zero matrices,
the {{< knowl id="special-linear-lie-algebra" text="special linear Lie algebra" >}} $\mathfrak{sl}_n(\mathbb F)$, and the exponential map restricts to $\exp:\mathfrak{sl}_n(\mathbb F)\to SL(n,\mathbb F)$ (see {{< knowl id="exponential-map-lie-group" text="exponential map" >}}). The determinant condition differentiates to the trace condition:
\[
\left.\frac{d}{dt}\right|_{t=0}\det(I+tX)=\mathrm{tr}(X).
\]

The groups $SL(n,\mathbb R)$ and $SL(n,\mathbb C)$ are basic examples of connected linear Lie groups, and they play a central role in semisimple theory (compare {{< knowl id="semisimple-lie-algebra" text="semisimple Lie algebras" >}} and the root-theoretic framework starting at {{< knowl id="root-system" text="root systems" >}}).
