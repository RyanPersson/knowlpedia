---
title: "Compactness implies completeness"
description: "Every compact metric space is complete"
---

**Compactness implies completeness**: If $(X,d)$ is a {{< knowl id="metric-space" text="metric space" >}} and $K\subseteq X$ is {{< knowl id="compact-set" text="compact" >}}, then $K$ is {{< knowl id="complete-metric-space" text="complete" >}} with the restricted metric.

**Proof sketch**: Let $(x_n)$ be a {{< knowl id="cauchy-sequence" text="Cauchy sequence" >}} in $K$. Compactness gives a {{< knowl id="convergent-sequence" text="convergent subsequence" >}} $x_{n_k}\to x$ with $x\in K$. A Cauchy sequence has at most one possible limit point, so the entire sequence converges to $x$ in $K$. Hence every Cauchy sequence in $K$ converges, so $K$ is complete.

**Examples:**
- Any compact subset of $\mathbb{R}^n$ is complete.
- The open interval $(0,1)$ is not complete (e.g. $1/n$ is Cauchy but converges to $0\notin(0,1)$), consistent with it not being compact.
