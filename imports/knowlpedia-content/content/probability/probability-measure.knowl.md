+++
id = "probability/probability-measure"
title = "Probability measure"
kind = "knowl"
summary = "A measure on a sigma-algebra with total mass 1."
aliases = ["probability-measure", "Probability measure"]
domains = ["probability"]
legacy_source_path = "probability/probability-measure.md"
+++

A **probability measure** is a function $\mathbb{P}:\mathcal{F}\to[0,1]$ defined on a [[measure-theory/sigma-algebra|sigma-algebra]] $\mathcal{F}$ of subsets of a [[shared-foundations/set|set]] $\Omega$ such that $\mathbb{P}(\varnothing)=0$, $\mathbb{P}\!\left(\bigcup_{n=1}^\infty A_n\right)=\sum_{n=1}^\infty \mathbb{P}(A_n)$ for every pairwise disjoint sequence $(A_n)_{n\ge1}\subseteq\mathcal{F}$, and $\mathbb{P}(\Omega)=1$.

A probability measure is a special case of a [[measure-theory/measure|measure]] and is the key ingredient in a [[probability/probability-space|probability space]]; it assigns [[probability/event-probability|probabilities to events]] (measurable sets).

**Examples:**
- If $\Omega=\{1,2,\dots,n\}$ and $\mathcal{F}=2^\Omega$, the uniform probability measure is $\mathbb{P}(A)=|A|/n$.
- If $\Omega=[0,1]$, $\mathcal{F}$ is the Borel $\sigma$-algebra, and $\lambda$ is [[measure-theory/lebesgue-measure|Lebesgue measure]], then $\mathbb{P}(A)=\lambda(A)$ defines the uniform probability measure on $[0,1]$.
