+++
id = "lie-groups/baker-campbell-hausdorff-formula"
title = "Baker–Campbell–Hausdorff formula"
kind = "knowl"
summary = "A Lie series for the product exp(X)exp(Y) expressed as exp(BCH(X,Y))."
aliases = ["baker-campbell-hausdorff-formula", "Baker–Campbell–Hausdorff formula"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/baker-campbell-hausdorff-formula.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] with Lie algebra $\mathfrak{g}$ and [[lie-groups/exponential-map-lie-group|exponential map]] $\exp:\mathfrak{g}\to G$. For $X,Y\in\mathfrak{g}$ sufficiently small, there is a unique $Z\in\mathfrak{g}$ near $0$ such that $\exp(X)\exp(Y)=\exp(Z)$; write $Z=\mathrm{BCH}(X,Y)$.

**Theorem (BCH).** In a neighborhood of $0\in\mathfrak{g}$,
$$
\mathrm{BCH}(X,Y)
= X+Y+\frac12[X,Y]+\frac1{12}[X,[X,Y]]-\frac1{12}[Y,[X,Y]]+\cdots,
$$

where the omitted terms are (universal) Lie polynomials in iterated [[fiber-bundles/lie-bracket|brackets]] of total degree $\ge 4$.

Moreover, if $\mathfrak{g}$ is [[lie-groups/nilpotent-lie-algebra|nilpotent]], then all sufficiently deep iterated brackets vanish and the BCH series truncates to a finite sum.

**Context.** BCH is the mechanism by which $\mathfrak{g}$ determines the local group law: via the [[lie-groups/logarithm-map|logarithm map]] (local inverse to $\exp$), it turns multiplication in $G$ into an explicit Lie series on $\mathfrak{g}$. This is central to the [[lie-groups/lie-correspondence|Lie correspondence]] and to computations in exponential coordinates, especially for nilpotent and solvable groups.
