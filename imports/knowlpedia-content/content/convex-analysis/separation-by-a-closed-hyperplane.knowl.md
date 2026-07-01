+++
id = "convex-analysis/separation-by-a-closed-hyperplane"
title = "Separation by a Closed Hyperplane"
kind = "knowl"
summary = "Separation using a nonzero continuous functional in the dual space."
aliases = ["separation-by-a-closed-hyperplane", "Separation by a Closed Hyperplane"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/separation-by-a-closed-hyperplane.md"
+++

Let $X$ be a real [[convex-analysis/norm-normed-vector-space|normed space]] and let $\Omega_1,\Omega_2\subset X$ be nonempty.

We say that $\Omega_1$ and $\Omega_2$ can be **separated by a closed hyperplane** if there exists a nonzero functional $x^\ast \in X^\ast$ (see [[convex-analysis/dual-space-and-duality-pairing|dual space]]) such that
$$
\langle x^\ast ,x\rangle \le \langle x^\ast ,y\rangle \quad\text{whenever }x\in\Omega_1,\ y\in\Omega_2.
$$

Here "closed [[convex-analysis/hyperplane|hyperplane]]" emphasizes that $x^\ast $ is continuous, so each level set $\{x\mid \langle x^\ast ,x\rangle=\alpha\}$ is [[convex-analysis/closed-subset|closed]]; see [[convex-analysis/continuity-of-linear-functionals-via-closed-level-sets|continuity via closed level sets]].
