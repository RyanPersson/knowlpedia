+++
id = "probability/probability-space"
title = "Probability space"
kind = "knowl"
summary = "A sample space with a sigma-algebra of events and a probability measure."
aliases = ["probability-space", "Probability space"]
domains = ["probability"]
legacy_source_path = "probability/probability-space.md"
+++

A **probability space** is a triple $(\Omega,\mathcal{F},\mathbb{P})$ where $\Omega$ is a [[shared-foundations/set|set]], $\mathcal{F}$ is a [[measure-theory/sigma-algebra|sigma-algebra]] on $\Omega$, and $\mathbb{P}$ is a [[probability/probability-measure|probability measure]] on $(\Omega,\mathcal{F})$.

Elements of $\mathcal{F}$ are the events whose [[probability/event-probability|probabilities]] are evaluated by $\mathbb{P}$, and a [[probability/random-variable|random variable]] is a measurable function defined on $(\Omega,\mathcal{F},\mathbb{P})$.

**Examples:**
- Fair coin toss: $\Omega=\{H,T\}$, $\mathcal{F}=2^\Omega$, and $\mathbb{P}(\{H\})=\mathbb{P}(\{T\})=1/2$.
- Uniform draw from $[0,1]$: $\Omega=[0,1]$, $\mathcal{F}$ is the Borel $\sigma$-algebra, and $\mathbb{P}(A)=\lambda(A)$ where $\lambda$ is [[measure-theory/lebesgue-measure|Lebesgue measure]].
