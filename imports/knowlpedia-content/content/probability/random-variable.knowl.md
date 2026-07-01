+++
id = "probability/random-variable"
title = "Random variable"
kind = "knowl"
summary = "A measurable real-valued function on a probability space."
aliases = ["random-variable", "Random variable"]
domains = ["probability"]
legacy_source_path = "probability/random-variable.md"
+++

A **random variable** is a [[measure-theory/measurable-function|measurable function]] $X:(\Omega,\mathcal{F})\to(\mathbb{R},\mathcal{B}(\mathbb{R}))$ defined on a [[probability/probability-space|probability space]] $(\Omega,\mathcal{F},\mathbb{P})$, meaning that for every Borel set $B\subseteq\mathbb{R}$ one has $X^{-1}(B)\in\mathcal{F}$.

A random variable induces a [[probability/distribution-law|distribution (law)]] on [[shared-foundations/real-numbers|the real numbers]] via $\mathbb{P}_X(B)=\mathbb{P}(X\in B)$, and quantities such as [[probability/expectation|expectation]] and [[probability/variance|variance]] are defined from this law.

**Examples:**
- For an event $A\in\mathcal{F}$, the indicator $X=\mathbf{1}_A$ (equal to $1$ on $A$ and $0$ on $A^c$) is a random variable.
- In a fair coin toss space, the function $X(H)=1$ and $X(T)=0$ is a random variable taking values in $\{0,1\}$.
