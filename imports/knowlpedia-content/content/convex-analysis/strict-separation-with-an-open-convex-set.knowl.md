+++
id = "convex-analysis/strict-separation-with-an-open-convex-set"
title = "Strict Separation When One Set is Open"
kind = "knowl"
summary = "An open convex set can be separated from a convex set with a strict inequality gap."
aliases = ["strict-separation-with-an-open-convex-set", "Strict Separation When One Set is Open"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/strict-separation-with-an-open-convex-set.md"
+++

Let $X$ be a real [[convex-analysis/norm-normed-vector-space|normed space]]. Let $G,\Omega\subset X$ be nonempty [[convex-analysis/convex-set|convex sets]] and assume that $G$ is [[convex-analysis/open-subset|open]].

**Corollary**: There exist $x^\ast \in X^\ast$ (see [[convex-analysis/dual-space-and-duality-pairing|dual space]]) and $\beta\in\mathbb{R}$ such that
$$
\langle x^\ast ,x\rangle < \beta \le \langle x^\ast ,y\rangle \quad \text{whenever }x\in G,\ y\in\Omega.
$$

This follows from [[convex-analysis/separation-by-closed-hyperplane-under-interior-condition|closed hyperplane separation under an interior condition]] together with the openness of $G$, which allows a strict inequality on the $G$ side.
