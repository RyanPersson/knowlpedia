+++
id = "probability/maximum-entropy-principle"
title = "Maximum entropy principle"
kind = "knowl"
summary = "A rule for selecting a probability distribution by maximizing entropy subject to known constraints."
aliases = ["maximum-entropy-principle", "Maximum entropy principle"]
domains = ["probability"]
legacy_source_path = "probability/maximum-entropy-principle.md"
+++

A **maximum entropy principle** is the prescription: given a nonempty set $\mathcal C$ of candidate probability distributions, select a distribution $P^\star$ satisfying
$$
P^\star \in \operatorname*{arg\,max}_{P\in\mathcal C} H(P),
$$

where $H$ is [[probability/shannon-entropy|Shannon entropy]] for discrete laws (and typically [[probability/differential-entropy|differential entropy]] for absolutely continuous laws). In applications, $\mathcal C$ is usually defined by constraints such as normalization, support restrictions, or moment/expectation constraints of the form $\mathbb E_P[g_i(X)]=c_i$ for a [[probability/random-variable|random variable]] $X$ and given functions $g_i$ (using [[probability/expectation|expectation]]).

The guiding idea is to choose the least-committal distribution consistent with the stated information. In many common settings, maximum-entropy problems can be reformulated in terms of minimizing [[probability/relative-entropy-kl-divergence|KL divergence]] to a reference distribution, with [[probability/gibbs-inequality-kl|Gibbs' inequality]] guaranteeing nonnegativity of the objective.

**Examples:**
- On a finite set of $n$ outcomes, if the only constraint is that the distribution is supported on those outcomes, the maximizer of Shannon entropy is the uniform distribution.
- Among all distributions on $\mathbb R$ with fixed mean and variance, the maximizer of differential entropy is the normal distribution with those parameters.
