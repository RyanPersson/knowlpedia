+++
id = "convex-analysis/biconjugate"
title = "Biconjugate"
kind = "knowl"
summary = "The conjugate of the conjugate, which produces a canonical closed convex minorant of a function."
aliases = ["biconjugate"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/biconjugate.md"
+++

A **biconjugate** of an extended-real-valued [[shared-foundations/function|function]] $f:\mathbb{R}^n\to(-\infty,+\infty]$ is the function
$$
f^{**} \;=\; (f^*)^*,
$$

where $f^*$ is the [[convex-analysis/convex-conjugate-fenchel|Fenchel conjugate]] of $f$.

The biconjugate $f^{**}$ is always a [[convex-analysis/closed-convex-function|closed convex function]], and it satisfies $f^{**}\le f$ pointwise. The key characterization is given by the [[convex-analysis/fenchel-moreau-theorem|Fenchel–Moreau theorem]]: under standard hypotheses (e.g. $f$ [[convex-analysis/domain-and-epigraph-proper-function|proper]]), one has $f=f^{**}$ exactly when $f$ is closed and convex.

**Examples:**
- If $f$ is closed and convex (for instance a norm or a quadratic), then $f^{**}=f$.
- If $f=\delta_C$ is the indicator of a set $C\subseteq\mathbb{R}^n$, then $\delta_C^{**}=\delta_{\overline{\mathrm{conv}}(C)}$, the indicator of the closed convex hull of $C$ (e.g. for $C=\{-1,1\}\subset\mathbb{R}$, one gets $\delta_C^{**}=\delta_{[-1,1]}$).
