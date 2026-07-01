+++
id = "stat-mech/laplace-principle-lemma"
title = "Laplace Principle"
kind = "knowl"
summary = "Asymptotic evaluation of log-integrals of exp(n f) by the supremum of f; a deterministic precursor to Varadhan’s lemma."
aliases = ["laplace-principle-lemma", "Laplace Principle"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/laplace-principle-lemma.md"
+++

This lemma is a deterministic prototype for [[large-deviations/varadhans-lemma|Varadhan's lemma]] and is closely related to the [[large-deviations/large-deviation-principle|large deviation principle]]. It is frequently used to approximate partition functions and free energies via maximization.

## Statement
Let $K$ be a compact topological space and let $\mu$ be a finite Borel measure on $K$ such that every nonempty open set has positive $\mu$-measure. If $f:K\to\mathbb{R}$ is continuous, then
$$
\lim_{n\to\infty}\frac{1}{n}\log\!\int_K e^{n f(x)}\,\mu(dx)
={}
\max_{x\in K} f(x).
$$

More generally, if $f$ is upper semicontinuous and bounded above on compact $K$, the same conclusion holds with $\max$ replaced by $\sup$.

## Key hypotheses and conclusions
**Hypotheses**
- Compactness of $K$ (ensures $f$ attains its maximum when $f$ is continuous).
- $\mu$ does not ignore neighborhoods of maximizers (positivity on open sets).
- Regularity of $f$ (at least continuity for the simplest version).

**Conclusions**
- Exponential integrals are governed at leading order by the **global maximum** of $f$:
  the integral behaves like $\exp\big(n\max f\big)$ up to subexponential factors.
- A discrete analogue: for finitely many numbers $\{a_i\}$,
  $\lim_{n\to\infty}\frac1n\log\sum_i e^{n a_i}=\max_i a_i$.

In statistical mechanics, this principle explains why a partition function (an integral or sum of exponentials) yields a free energy that can often be expressed as a variational supremum. It is the leading-order version of the more refined [[stat-mech/saddle-point-lemma|saddle-point method]], which also provides prefactors.
