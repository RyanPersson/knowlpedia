---
title: "Cauchy Criterion in Rk"
description: "In Euclidean space, a sequence converges exactly when it is Cauchy."
---

**Cauchy criterion in $\mathbb{R}^k$:** Let $(x_n)$ be a sequence in $\mathbb{R}^k$, with distance measured by the {{< knowl id="euclidean-norm" section="linear-algebra" text="Euclidean norm" >}} (equivalently, the Euclidean metric). Then $(x_n)$ converges in $\mathbb{R}^k$ if and only if it is a {{< knowl id="cauchy-sequence" section="topology" text="Cauchy sequence" >}}, meaning: for every $\varepsilon>0$ there exists $N$ such that for all $m,n\ge N$,
$\|x_n-x_m\|<\varepsilon$.

This is the completeness of Euclidean space, i.e. that $\mathbb{R}^k$ is a {{< knowl id="complete-metric-space" section="topology" text="complete metric space" >}}. In one dimension it is one of the standard consequences of the {{< knowl id="completeness-axiom" text="completeness axiom" >}}.
