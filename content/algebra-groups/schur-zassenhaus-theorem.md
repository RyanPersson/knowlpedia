---
title: "Schur–Zassenhaus Theorem"
description: "A normal Hall subgroup has a complement, unique up to conjugacy"
---

**Schur–Zassenhaus Theorem.**
Let $G$ be a finite {{< knowl id="group" text="group" >}} and let $N \trianglelefteq G$ be a {{< knowl id="normal-subgroup" text="normal subgroup" >}} that is a {{< knowl id="hall-subgroup" text="Hall subgroup" >}} (equivalently, $\gcd(|N|,[G:N])=1$). Then:

1. (**Existence of complements**) There exists a subgroup $H \le G$ such that $G = NH$ and $N \cap H = \{e\}$. Equivalently, $G$ is a {{< knowl id="semidirect-product" text="semidirect product" >}} $G \cong N \rtimes H$.
2. (**Conjugacy of complements**) If $H_1$ and $H_2$ are two such complements, then $H_1$ and $H_2$ are conjugate in $G$ (they lie in the same orbit under the {{< knowl id="conjugation-action" text="conjugation action" >}}).

This theorem is often phrased as: a short exact sequence with coprime kernel and quotient {{< knowl id="split-extension" text="splits" >}}. It is a central tool for analyzing group structure when orders factor into coprime parts.

**Proof sketch.**
One proves existence by induction on $|G|$, using coprimality to force fixed points in appropriate actions and to build a complement step-by-step. Conjugacy of complements is obtained by a similar induction argument, comparing two complements via their actions on $N$ and exploiting the coprime condition to solve a conjugacy equation.
