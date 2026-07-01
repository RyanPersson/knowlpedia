+++
id = "convex-analysis/strict-separation-of-compact-and-closed-convex-sets"
title = "Strict Separation of Compact and Closed Convex Sets"
kind = "knowl"
summary = "Disjoint compact convex and closed convex sets in a normed space admit strict separation by a continuous functional."
aliases = ["strict-separation-of-compact-and-closed-convex-sets", "Strict Separation of Compact and Closed Convex Sets"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/strict-separation-of-compact-and-closed-convex-sets.md"
+++

Let $X$ be a real [[convex-analysis/norm-normed-vector-space|normed space]]. Let $K,F\subset X$ be nonempty [[convex-analysis/convex-set|convex sets]] and assume:
- $K$ is compact,
- $F$ is [[convex-analysis/closed-subset|closed]], and
- $K\cap F=\emptyset$.

**Theorem**: The sets $K$ and $F$ can be [[convex-analysis/strict-separation-by-a-closed-hyperplane|strictly separated by a closed hyperplane]]. Equivalently, there exists $x^\ast \in X^\ast$ (see [[convex-analysis/dual-space-and-duality-pairing|dual space]]) such that
$$
\sup_{x\in K}\langle x^\ast ,x\rangle < \inf_{y\in F}\langle x^\ast ,y\rangle.
$$

**Context:**
This is a strong separation result in normed spaces. The proof in the notes applies [[convex-analysis/separation-by-closed-hyperplane-under-interior-condition|closed hyperplane separation]] to a ball around $0$ and a translated difference set $F-K$, using compactness/closedness to guarantee closedness and a positive gap.
