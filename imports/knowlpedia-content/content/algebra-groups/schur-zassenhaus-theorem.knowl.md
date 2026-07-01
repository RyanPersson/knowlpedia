+++
id = "algebra-groups/schur-zassenhaus-theorem"
title = "Schur–Zassenhaus Theorem"
kind = "knowl"
summary = "A normal Hall subgroup has a complement, unique up to conjugacy"
aliases = ["schur-zassenhaus-theorem", "Schur–Zassenhaus Theorem"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/schur-zassenhaus-theorem.md"
+++

**Schur–Zassenhaus Theorem.**
Let $G$ be a finite [[algebra-groups/group|group]] and let $N \trianglelefteq G$ be a [[algebra-groups/normal-subgroup|normal subgroup]] that is a [[algebra-groups/hall-subgroup|Hall subgroup]] (equivalently, $\gcd(|N|,[G:N])=1$). Then:

1. (**Existence of complements**) There exists a subgroup $H \le G$ such that $G = NH$ and $N \cap H = \{e\}$. Equivalently, $G$ is a [[algebra-groups/semidirect-product|semidirect product]] $G \cong N \rtimes H$.
2. (**Conjugacy of complements**) If $H_1$ and $H_2$ are two such complements, then $H_1$ and $H_2$ are conjugate in $G$ (they lie in the same orbit under the [[algebra-groups/conjugation-action|conjugation action]]).

This theorem is often phrased as: a short exact sequence with coprime kernel and quotient [[algebra-groups/split-extension|splits]]. It is a central tool for analyzing group structure when orders factor into coprime parts.
