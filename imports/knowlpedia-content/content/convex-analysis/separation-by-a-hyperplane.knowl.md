+++
id = "convex-analysis/separation-by-a-hyperplane"
title = "Separation by a Hyperplane"
kind = "knowl"
summary = "Two sets are separable if a nonzero linear functional orders them."
aliases = ["separation-by-a-hyperplane", "Separation by a Hyperplane"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/separation-by-a-hyperplane.md"
+++

Let $X$ be a real [[linear-algebra/vector-space|vector space]] and let $\Omega_1,\Omega_2\subset X$ be nonempty.

We say that $\Omega_1$ and $\Omega_2$ can be **separated by a hyperplane** if there exists a nonzero linear functional $f:X\to\mathbb{R}$ such that
$$
f(x)\le f(y)\quad\text{whenever }x\in\Omega_1,\ y\in\Omega_2.
$$

Geometrically, picking any $\alpha$ with $\sup_{\Omega_1}f\le \alpha\le \inf_{\Omega_2}f$ produces the [[convex-analysis/hyperplane|hyperplane]] $\{x\mid f(x)=\alpha\}$ lying between the two sets; see [[convex-analysis/separation-by-hyperplanes-via-supinf-inequality|the sup/inf characterization]].
