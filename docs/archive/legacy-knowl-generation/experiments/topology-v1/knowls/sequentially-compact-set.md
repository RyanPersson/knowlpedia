---
title: "Sequentially compact set"
description: "A set in which every sequence has a convergent subsequence with limit in the set"
---

A set $K$ in a {{< knowl id="metric-space" text="metric space" >}} $(X,d)$ is **sequentially compact** if every sequence $(x_n)$ with $x_n\in K$ has a subsequence $(x_{n_k})$ that is a {{< knowl id="convergent-sequence" text="convergent sequence" >}} in $X$, and whose limit belongs to $K$.

Sequential compactness is the “sequence-based” version of compactness. In metric spaces it agrees with {{< knowl id="compact-set" text="compactness" >}}; see {{< knowl id="sequential-compactness-equals-compactness" text="sequential compactness equals compactness" >}}.

**Examples:**
- The interval $[0,1]\subset\mathbb{R}$ is sequentially compact.
- Any finite set in any metric space is sequentially compact.
- The set $(0,1)\subset\mathbb{R}$ is not sequentially compact: the sequence $x_n=1/n$ converges to $0\notin (0,1)$.
