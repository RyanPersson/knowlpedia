---
title: "Biconjugate"
description: "The conjugate of the conjugate, which produces a canonical closed convex minorant of a function."
---

A **biconjugate** of an extended-real-valued {{< knowl id="function" section="shared-foundations" text="function" >}} $f:\mathbb{R}^n\to(-\infty,+\infty]$ is the function
$$
f^{**} \;=\; (f^*)^*,
$$

where $f^*$ is the {{< knowl id="convex-conjugate-fenchel" text="Fenchel conjugate" >}} of $f$.

The biconjugate $f^{**}$ is always a {{< knowl id="closed-convex-function" text="closed convex function" >}}, and it satisfies $f^{**}\le f$ pointwise. The key characterization is given by the {{< knowl id="fenchel-moreau-theorem" text="Fenchel–Moreau theorem" >}}: under standard hypotheses (e.g. $f$ {{< knowl id="domain-and-epigraph-proper-function" text="proper" >}}), one has $f=f^{**}$ exactly when $f$ is closed and convex.

**Examples:**
- If $f$ is closed and convex (for instance a norm or a quadratic), then $f^{**}=f$.
- If $f=\delta_C$ is the indicator of a set $C\subseteq\mathbb{R}^n$, then $\delta_C^{**}=\delta_{\overline{\mathrm{conv}}(C)}$, the indicator of the closed convex hull of $C$ (e.g. for $C=\{-1,1\}\subset\mathbb{R}$, one gets $\delta_C^{**}=\delta_{[-1,1]}$).
