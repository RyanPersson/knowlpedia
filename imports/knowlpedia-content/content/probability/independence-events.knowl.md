+++
id = "probability/independence-events"
title = "Independence of events"
kind = "knowl"
summary = "A condition ensuring knowledge of one event does not change the probability of another"
aliases = ["independence-events", "Independence of events"]
domains = ["probability"]
legacy_source_path = "probability/independence-events.md"
+++

Two **events are independent** if, on a [[probability/probability-space|probability space]] $(\Omega,\mathcal F,\mathbb P)$, they satisfy
$$
\mathbb P(A\cap B)\;=\;\mathbb P(A)\,\mathbb P(B).
$$

A finite or countable family of events $(A_i)_{i\in I}$ is **independent** if for every finite subset $\{i_1,\dots,i_n\}\subseteq I$,
$$
\mathbb P\!\left(\bigcap_{k=1}^n A_{i_k}\right)\;=\;\prod_{k=1}^n \mathbb P(A_{i_k}).
$$

Independence can be expressed in terms of [[probability/conditional-probability|conditional probability]]: if $\mathbb P(B)>0$, then $A$ and $B$ are independent exactly when $\mathbb P(A\mid B)=\mathbb P(A)$.  This notion extends from events to [[probability/independence-sigma-algebras|independence of sigma-algebras]] and to [[probability/independence-random-variables|independence of random variables]].

**Examples:**
- In two independent coin flips, let $A=\{\text{first flip is H}\}$ and $B=\{\text{second flip is H}\}$. Then $\mathbb P(A)=\mathbb P(B)=1/2$ and $\mathbb P(A\cap B)=1/4$, so $A$ and $B$ are independent.
- For one fair die roll, let $A=\{\text{even}\}$ and $B=\{\text{roll}\le 3\}$. Then $\mathbb P(A)=1/2$, $\mathbb P(B)=1/2$, but $\mathbb P(A\cap B)=\mathbb P(\{2\})=1/6\ne 1/4$, so $A$ and $B$ are not independent.
