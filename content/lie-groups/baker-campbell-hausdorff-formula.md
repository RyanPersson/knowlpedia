---
title: "Baker–Campbell–Hausdorff formula"
description: "A Lie series for the product exp(X)exp(Y) expressed as exp(BCH(X,Y))."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} with Lie algebra $\mathfrak{g}$ and {{< knowl id="exponential-map-lie-group" text="exponential map" >}} $\exp:\mathfrak{g}\to G$. For $X,Y\in\mathfrak{g}$ sufficiently small, there is a unique $Z\in\mathfrak{g}$ near $0$ such that $\exp(X)\exp(Y)=\exp(Z)$; write $Z=\mathrm{BCH}(X,Y)$.

**Theorem (BCH).** In a neighborhood of $0\in\mathfrak{g}$,
$$
\mathrm{BCH}(X,Y)
= X+Y+\frac12[X,Y]+\frac1{12}[X,[X,Y]]-\frac1{12}[Y,[X,Y]]+\cdots,
$$

where the omitted terms are (universal) Lie polynomials in iterated {{< knowl id="lie-bracket" text="brackets" section="fiber-bundles">}} of total degree $\ge 4$.

Moreover, if $\mathfrak{g}$ is {{< knowl id="nilpotent-lie-algebra" text="nilpotent" >}}, then all sufficiently deep iterated brackets vanish and the BCH series truncates to a finite sum.

**Context.** BCH is the mechanism by which $\mathfrak{g}$ determines the local group law: via the {{< knowl id="logarithm-map" text="logarithm map" >}} (local inverse to $\exp$), it turns multiplication in $G$ into an explicit Lie series on $\mathfrak{g}$. This is central to the {{< knowl id="lie-correspondence" text="Lie correspondence" >}} and to computations in exponential coordinates, especially for nilpotent and solvable groups.
