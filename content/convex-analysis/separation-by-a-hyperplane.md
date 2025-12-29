---
title: "Separation by a Hyperplane"
description: "Two sets are separable if a nonzero linear functional orders them."
---

Let $X$ be a real {{< knowl id="vector-space" text="vector space" >}} and let $\Omega_1,\Omega_2\subset X$ be nonempty.

We say that $\Omega_1$ and $\Omega_2$ can be **separated by a hyperplane** if there exists a nonzero linear functional $f:X\to\mathbb{R}$ such that
$$
f(x)\le f(y)\quad\text{whenever }x\in\Omega_1,\ y\in\Omega_2.
$$

Geometrically, picking any $\alpha$ with $\sup_{\Omega_1}f\le \alpha\le \inf_{\Omega_2}f$ produces the {{< knowl id="hyperplane" text="hyperplane" >}} $\{x\mid f(x)=\alpha\}$ lying between the two sets; see {{< knowl id="separation-by-hyperplanes-via-supinf-inequality" text="the sup/inf characterization" >}}.
