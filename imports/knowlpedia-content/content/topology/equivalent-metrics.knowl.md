+++
id = "topology/equivalent-metrics"
title = "Equivalent metrics"
kind = "knowl"
summary = "Two metrics on the same set that generate the same open sets, hence the same topology."
aliases = ["equivalent-metrics", "Equivalent metrics"]
domains = ["topology"]
legacy_source_path = "topology/equivalent-metrics.md"
+++

Two **equivalent metrics** $d$ and $d'$ on the same set $X$ are metrics that induce the same [[topology/metric-induced-topology|metric-induced topology]] on $X$; equivalently, a set $U\subseteq X$ is [[topology/open-set|open]] with respect to $d$ if and only if it is open with respect to $d'$.

Equivalently, the identity map $\mathrm{id}\colon (X,d)\to (X,d')$ is a [[topology/homeomorphism|homeomorphism]]. Equivalent metrics have the same open sets and therefore the same convergent sequences, but they may differ in which sequences are [[topology/cauchy-sequence|Cauchy]] and whether the space is [[topology/complete-metric-space|complete]].

**Examples:**
- For any metric $d$ on $X$, the metric $d'(x,y)=\min\{1,d(x,y)\}$ is equivalent to $d$.
- On $\mathbb{R}^n$, the Euclidean metric and the taxicab metric $d_1(x,y)=\sum_{i=1}^n |x_i-y_i|$ are equivalent.
