---
title: "Chernoff bounding lemma"
description: "Exponential-moment (Laplace transform) bounds for tail probabilities: P(X ≥ a) ≤ e^{-t a} E[e^{tX}] and optimization over t."
---

## Definitions and notation

- {{< knowl id="probability-measure" section="probability" text="Probability measure" >}}, {{< knowl id="expectation" section="probability" text="expectation" >}}.
- {{< knowl id="moment-generating-function" section="probability" text="Moment generating function" >}} (exponential moments).
- {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transform" >}} and {{< knowl id="rate-function" section="large-deviations" text="rate function" >}} (for the optimized form).

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
The optimized bound connects directly to large deviations: the function $t\mapsto \log \mathbb E[e^{tX}]$ is convex, and its Legendre transform often appears as the candidate {{< knowl id="rate-function" section="large-deviations" text="rate function" >}} in a {{< knowl id="large-deviation-principle" section="large-deviations" text="large deviation principle" >}}.

In statistical mechanics, the same mechanism controls fluctuations of extensive observables via exponential tilting of ensembles.
