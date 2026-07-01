+++
id = "probability/event-probability"
title = "Probability of an event"
kind = "knowl"
summary = "The number assigned by a probability measure to an event."
aliases = ["event-probability", "Probability of an event"]
domains = ["probability"]
legacy_source_path = "probability/event-probability.md"
+++

A **probability of an event** in a [[probability/probability-space|probability space]] $(\Omega,\mathcal{F},\mathbb{P})$ is the number $\mathbb{P}(A)$ assigned to an event $A\in\mathcal{F}$.

Because events are [[measure-theory/measurable-set|measurable sets]] and $\mathbb{P}$ is a [[probability/probability-measure|probability measure]], event probabilities satisfy the usual axioms (nonnegativity, countable additivity on disjoint events, and normalization).

**Examples:**
- In a fair coin toss space, the event $A=\{H\}$ has probability $\mathbb{P}(A)=1/2$.
- In the uniform space on $[0,1]$, the event $A=[0,1/2]$ has probability $\mathbb{P}(A)=1/2$.
