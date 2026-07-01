+++
id = "real-analysis/completeness-equivalences"
title = "Completeness Equivalences"
kind = "knowl"
summary = "Several standard statements that are equivalent forms of completeness of the real numbers."
aliases = ["completeness-equivalences", "Completeness Equivalences"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/completeness-equivalences.md"
+++

**Completeness equivalences:** For an ordered field satisfying the [[real-analysis/field-axioms|field axioms]] and [[real-analysis/order-axioms|order axioms]], the following statements are equivalent (each implies the others):

1. (Least upper bound property) Every nonempty [[real-analysis/bounded-above|bounded above]] subset of $\mathbb{R}$ has a [[real-analysis/supremum|supremum]] (the [[real-analysis/completeness-axiom|completeness axiom]]).
2. (Cauchy completeness) Every [[topology/cauchy-sequence|Cauchy sequence]] in $\mathbb{R}$ is a [[topology/convergent-sequence|convergent sequence]].
3. (Monotone convergence) Every [[real-analysis/monotone-sequence|monotone sequence]] in $\mathbb{R}$ that is bounded converges (see [[real-analysis/monotone-sequence-convergence-theorem|monotone sequence convergence theorem]]).
4. (Nested intervals) If $(I_n)$ is a nested sequence of nonempty closed [[real-analysis/interval|intervals]] with lengths tending to $0$, then $\bigcap_{n=1}^\infty I_n$ consists of exactly one point.

These equivalent formulations let one choose the most convenient “completeness principle” for a given argument, depending on whether the problem is stated in terms of [[real-analysis/supremum|suprema]], sequences, or intervals.
