---
title: "Fenchel-Moreau theorem"
description: "A closed proper convex function equals its Fenchel biconjugate."
---

**Fenchel-Moreau theorem:** Let $f:\mathbb{R}^n\to(-\infty,+\infty]$ be a proper {{< knowl id="function" section="shared-foundations" text="function" >}}, and let $f^{**}$ denote its {{< knowl id="biconjugate" text="biconjugate" >}} (defined using the {{< knowl id="convex-conjugate-fenchel" text="Fenchel conjugate" >}}). Then $f^{**}$ is a {{< knowl id="closed-convex-function" text="closed convex function" >}} and satisfies
$$
f^{**}(x)\le f(x)\quad\text{for all }x\in\mathbb{R}^n.
$$

Moreover, $f=f^{**}$ pointwise if and only if $f$ is closed and convex.

This result justifies representing closed convex functions as suprema of affine minorants and is a structural cornerstone for {{< knowl id="convex-duality-primal-dual" text="convex duality" >}}.
