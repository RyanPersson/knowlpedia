---
title: "Sequentially compact set"
description: "A set in which every sequence has a convergent subsequence with limit in the set"
---

A **sequentially compact set** $K$ in a {{< knowl id="metric-space" section="topology-metric" text="metric space" >}} is a set such that every sequence $(x_n)$ in $K$ has a subsequence $(x_{n_k})$ that {{< knowl id="convergent-sequence" section="topology-metric" text="converges" >}} to a limit $x\in K$.

In metric spaces this is closely tied to {{< knowl id="compact-set" text="compactness" >}} via {{< knowl id="sequential-compactness-equals-compactness" text="the equivalence theorem" >}}.

**Examples:**
- The interval $[0,1]\subset\mathbb R$ is sequentially compact.
- Any finite set in a metric space is sequentially compact.
- The set $(0,1)\subset\mathbb R$ is not sequentially compact (e.g. $x_n=1/n$ has no subsequence converging to a point of $(0,1)$).
