+++
id = "convex-analysis/strict-separation-by-a-closed-hyperplane"
title = "Strict Separation by a Closed Hyperplane"
kind = "knowl"
summary = "Strict separation means there is a positive gap between the two sets under a continuous functional."
aliases = ["strict-separation-by-a-closed-hyperplane", "Strict Separation by a Closed Hyperplane"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/strict-separation-by-a-closed-hyperplane.md"
+++

Let $X$ be a real [[convex-analysis/norm-normed-vector-space|normed space]] and let $\Omega_1,\Omega_2\subset X$ be nonempty.

We say that $\Omega_1$ and $\Omega_2$ can be **strictly separated by a closed hyperplane** if there exist $x^\ast \in X^\ast$ (see [[convex-analysis/dual-space-and-duality-pairing|dual space]]) and real numbers $\alpha<\beta$ such that
$$
\langle x^\ast ,x\rangle \le \alpha < \beta \le \langle x^\ast ,y\rangle
\quad\text{for all }x\in\Omega_1,\ y\in\Omega_2.
$$

Equivalently, strict separation holds iff there exists $x^\ast \in X^\ast $ with
$$
\sup_{x\in\Omega_1}\langle x^\ast ,x\rangle < \inf_{y\in\Omega_2}\langle x^\ast ,y\rangle.
$$

This notion strengthens [[convex-analysis/separation-by-a-closed-hyperplane|separation by a closed hyperplane]] by requiring a strict gap.
