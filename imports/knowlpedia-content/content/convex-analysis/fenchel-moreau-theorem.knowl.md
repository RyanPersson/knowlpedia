+++
id = "convex-analysis/fenchel-moreau-theorem"
title = "Fenchel-Moreau theorem"
kind = "knowl"
summary = "A closed proper convex function equals its Fenchel biconjugate."
aliases = ["fenchel-moreau-theorem", "Fenchel-Moreau theorem"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/fenchel-moreau-theorem.md"
+++

**Fenchel-Moreau theorem:** Let $f:\mathbb{R}^n\to(-\infty,+\infty]$ be a proper [[shared-foundations/function|function]], and let $f^{**}$ denote its [[convex-analysis/biconjugate|biconjugate]] (defined using the [[convex-analysis/convex-conjugate-fenchel|Fenchel conjugate]]). Then $f^{**}$ is a [[convex-analysis/closed-convex-function|closed convex function]] and satisfies
$$
f^{**}(x)\le f(x)\quad\text{for all }x\in\mathbb{R}^n.
$$

Moreover, $f=f^{**}$ pointwise if and only if $f$ is closed and convex.

This result justifies representing closed convex functions as suprema of affine minorants and is a structural cornerstone for [[convex-analysis/convex-duality-primal-dual|convex duality]].
