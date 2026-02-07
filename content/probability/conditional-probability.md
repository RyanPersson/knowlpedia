---
title: "Conditional probability"
description: "Probability of an event given another event or a sigma-algebra representing available information"
---

A **conditional probability** is the probability of an event after restricting to information in another event or in a sub-{{< knowl id="sigma-algebra" section="measure-theory" text="sigma-algebra" >}}.  On a {{< knowl id="probability-space" text="probability space" >}} $(\Omega,\mathcal F,\mathbb P)$, for events $A,B\in\mathcal F$ with $\mathbb P(B)>0$, the conditional probability of $A$ given $B$ is
$$
\mathbb P(A\mid B)\;=\;\frac{\mathbb P(A\cap B)}{\mathbb P(B)}.
$$

More generally, for a sub-$\sigma$-algebra $\mathcal G\subseteq\mathcal F$, the conditional probability of $A$ given $\mathcal G$ is the $\mathcal G$-measurable {{< knowl id="random-variable" text="random variable" >}} defined by
$$
\mathbb P(A\mid \mathcal G)\;=\;\mathbb E[\mathbf 1_A\mid \mathcal G],
$$

where $\mathbb E[\cdot\mid \mathcal G]$ denotes {{< knowl id="conditional-expectation" text="conditional expectation" >}}.

Conditioning on an event $B$ can be viewed as conditioning on the $\sigma$-algebra $\sigma(B)=\{\varnothing,B,B^c,\Omega\}$; conditional probability is central to {{< knowl id="independence-events" text="independence of events" >}} and Bayesian updating.

**Examples:**
- If a fair die is rolled, $A=\{\text{even}\}$ and $B=\{\text{roll}>3\}$, then $\mathbb P(A\mid B)=\frac{2/6}{3/6}=\frac{2}{3}$.
- If $A$ and $B$ are {{< knowl id="independence-events" text="independent events" >}} with $\mathbb P(B)>0$, then $\mathbb P(A\mid B)=\mathbb P(A)$.
- For a sub-$\sigma$-algebra $\mathcal G$, if $A\in\mathcal G$ then $\mathbb P(A\mid \mathcal G)=\mathbf 1_A$ almost surely, while if $\mathcal G=\{\varnothing,\Omega\}$ then $\mathbb P(A\mid \mathcal G)=\mathbb P(A)$.
