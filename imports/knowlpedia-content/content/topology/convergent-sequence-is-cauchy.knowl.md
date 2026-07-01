+++
id = "topology/convergent-sequence-is-cauchy"
title = "Convergent sequence is Cauchy"
kind = "knowl"
summary = "In a metric space, every convergent sequence is Cauchy"
aliases = ["convergent-sequence-is-cauchy", "Convergent sequence is Cauchy"]
domains = ["topology"]
legacy_source_path = "topology/convergent-sequence-is-cauchy.md"
+++

**Convergent sequence is Cauchy:** Let $(X,d)$ be a [[topology/metric-space|metric space]] and let $(x_n)$ be a [[topology/convergent-sequence|convergent sequence]] with $x_n\to x$ in $X$. Then $(x_n)$ is a [[topology/cauchy-sequence|Cauchy sequence]]; that is, for every $\varepsilon>0$ there exists $N$ such that if $m,n\ge N$ then $d(x_m,x_n)<\varepsilon$.

Together with the converse implication in [[topology/complete-metric-space|complete metric spaces]], this links limits to intrinsic “eventual closeness” of sequence terms.
