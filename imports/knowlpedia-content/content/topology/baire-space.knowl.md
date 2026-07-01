+++
id = "topology/baire-space"
title = "Baire space"
kind = "knowl"
summary = "A topological space in which countable intersections of dense open sets are dense"
aliases = ["baire-space", "Baire space"]
domains = ["topology"]
legacy_source_path = "topology/baire-space.md"
+++

A **Baire space** is a [[topology/topological-space|topological space]] $X$ such that for every sequence $(U_n)_{n\in\mathbb{N}}$ of [[topology/open-set|open sets]] that are [[topology/dense-set|dense]], the intersection $\bigcap_{n\in\mathbb{N}} U_n$ is dense in $X$.

This is the setting for [[topology/baire-category-theorem|Baire category arguments]]: in a Baire space, “large” sets are often expressed as [[topology/residual-set|residual sets]], and “small” sets as [[topology/meager-set|meager sets]] (countable unions of [[topology/nowhere-dense-set|nowhere dense sets]]).

**Examples:**
- Any [[topology/complete-metric-space|complete metric space]] is a Baire space (see [[topology/complete-metric-space-is-baire|complete metric spaces are Baire]]).
- Any [[linear-algebra/banach-space|Banach space]] (with its metric from the norm) is a Baire space.
