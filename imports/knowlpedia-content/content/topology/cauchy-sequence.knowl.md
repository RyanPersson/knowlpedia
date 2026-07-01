+++
id = "topology/cauchy-sequence"
title = "Cauchy sequence"
kind = "knowl"
summary = "A sequence in a metric space whose terms become arbitrarily close to each other."
aliases = ["cauchy-sequence", "Cauchy sequence"]
domains = ["topology"]
legacy_source_path = "topology/cauchy-sequence.md"
+++

A **Cauchy sequence** $(x_n)$ in a metric space $(X,d)$ is a sequence such that for every $\varepsilon>0$ there exists $N$ with
\[
d(x_m,x_n)<\varepsilon \quad\text{for all } m,n\ge N.
\]

Every [[topology/convergent-sequence|convergent sequence]] in a metric space is Cauchy (see [[topology/convergent-sequence-is-cauchy|convergent implies Cauchy]]). The converse holds precisely in a [[topology/complete-metric-space|complete metric space]].

**Examples:**
- In $\mathbb{R}$, the sequence $x_n=1/n$ is Cauchy.
- In $\mathbb{Q}$ with the usual metric, a sequence of rational approximations to $\sqrt{2}$ is Cauchy in $\mathbb{Q}$ but does not converge in $\mathbb{Q}$.
