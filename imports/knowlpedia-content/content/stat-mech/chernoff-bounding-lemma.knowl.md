+++
id = "stat-mech/chernoff-bounding-lemma"
title = "Chernoff bounding lemma"
kind = "knowl"
summary = "Exponential-moment (Laplace transform) bounds for tail probabilities: P(X ≥ a) ≤ e^{-t a} E[e^{tX}] and optimization over t."
aliases = ["chernoff-bounding-lemma", "Chernoff bounding lemma"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/chernoff-bounding-lemma.md"
+++

## Definitions and notation

- [[probability/probability-measure|Probability measure]], [[probability/expectation|expectation]].
- [[probability/moment-generating-function|Moment generating function]] (exponential moments).
- [[convex-analysis/legendre-transform|Legendre transform]] and [[large-deviations/rate-function|rate function]] (for the optimized form).

## Statement

Let $X$ be a real-valued random variable. Fix $a\in\mathbb R$.

1. **Upper tail.** For any $t>0$ such that $\mathbb E[e^{tX}]<\infty$,
$$
\mathbb P(X \ge a) \le e^{-t a}\,\mathbb E[e^{tX}].
$$

2. **Lower tail.** For any $t<0$ such that $\mathbb E[e^{tX}]<\infty$,
$$
\mathbb P(X \le a) \le e^{-t a}\,\mathbb E[e^{tX}].
$$

Equivalently, for the upper tail,
$$
\mathbb P(X \ge a) \le \inf_{t>0}\exp\!\big(-t a + \log \mathbb E[e^{tX}]\big),
$$

whenever the infimum is over $t$ with finite exponential moment.

## Key hypotheses and conclusions

**Hypotheses**
- Exponential moment exists at the chosen tilt $t$: $\mathbb E[e^{tX}]<\infty$.
- $t>0$ for upper tails, $t<0$ for lower tails.

**Conclusions**
- Tail probabilities are controlled by exponential moments.
- Optimizing over $t$ yields the tightest Chernoff bound available from the moment generating function (often expressed via a Legendre transform of $\log \mathbb E[e^{tX}]$).
The optimized bound connects directly to large deviations: the function $t\mapsto \log \mathbb E[e^{tX}]$ is convex, and its Legendre transform often appears as the candidate [[large-deviations/rate-function|rate function]] in a [[large-deviations/large-deviation-principle|large deviation principle]].

In statistical mechanics, the same mechanism controls fluctuations of extensive observables via exponential tilting of ensembles.
