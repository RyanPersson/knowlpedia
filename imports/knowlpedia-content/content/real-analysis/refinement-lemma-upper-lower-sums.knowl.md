+++
id = "real-analysis/refinement-lemma-upper-lower-sums"
title = "Refinement lemma for upper and lower sums"
kind = "knowl"
summary = "Refining a partition decreases upper sums and increases lower sums."
aliases = ["refinement-lemma-upper-lower-sums", "Refinement lemma for upper and lower sums"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/refinement-lemma-upper-lower-sums.md"
+++

**Refinement lemma:** Let $a<b$ and let $f:[a,b]\to\mathbb{R}$ be bounded. If $P'$ is a [[real-analysis/refinement-of-a-partition|refinement]] of a [[real-analysis/partition-of-an-interval|partition]] $P$, then
$$
U(f,P')\le U(f,P)
\quad\text{and}\quad
L(f,P')\ge L(f,P),
$$

where $U(f,P)$ and $L(f,P)$ denote the [[real-analysis/upper-sum|upper sum]] and [[real-analysis/lower-sum|lower sum]] of $f$ with respect to $P$.

This monotonicity under refinement underlies the definition of the [[real-analysis/riemann-integral|Riemann integral]] as the common value of the infimum of upper sums and the supremum of lower sums.
