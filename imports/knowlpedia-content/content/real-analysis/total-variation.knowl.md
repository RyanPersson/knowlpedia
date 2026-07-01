+++
id = "real-analysis/total-variation"
title = "Total variation"
kind = "knowl"
summary = "The supremum of sums of absolute increments over all partitions."
aliases = ["total-variation", "Total variation"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/total-variation.md"
+++

A **total variation** of a function $\alpha:[a,b]\to\mathbb R$ on $[a,b]$ is the number
\[
V_a^b(\alpha)=\sup_P \sum_{i=1}^n |\alpha(x_i)-\alpha(x_{i-1})|,
\]
where the supremum is taken over all [[real-analysis/partition-of-an-interval|partitions]] $P=\{x_0,\dots,x_n\}$ of $[a,b]$.

Total variation measures how much $\alpha$ accumulates change along the interval and is the defining quantity for a [[real-analysis/bounded-variation-function|function of bounded variation]]. For [[real-analysis/monotone-function|monotone]] functions it reduces to the net change.

**Examples:**
- If $\alpha$ is increasing on $[a,b]$, then $V_a^b(\alpha)=\alpha(b)-\alpha(a)$.
- For $\alpha(x)=\sin x$ on $[0,2\pi]$, one has $V_0^{2\pi}(\alpha)=4$.
