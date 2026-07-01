+++
id = "topology/nested-interval-theorem"
title = "Nested interval theorem"
kind = "knowl"
summary = "A nested sequence of nonempty closed intervals in the real line has nonempty intersection"
aliases = ["nested-interval-theorem", "Nested interval theorem"]
domains = ["topology"]
legacy_source_path = "topology/nested-interval-theorem.md"
+++

**Nested interval theorem:** Let $(I_n)_{n\in\mathbb{N}}$ be a sequence of nonempty closed [[real-analysis/interval|intervals]] in $\mathbb{R}$ such that $I_{n+1}\subseteq I_n$ for all $n$. Then $\bigcap_{n\in\mathbb{N}} I_n\neq\varnothing$.

More precisely, if $I_n=[a_n,b_n]$, then $\bigcap_{n\in\mathbb{N}} I_n=[\sup_n a_n,\inf_n b_n]$, using [[real-analysis/supremum|supremum]] and [[real-analysis/infimum|infimum]]. If additionally $b_n-a_n\to 0$, then the intersection is a single point.

This can be viewed as a special case of the [[topology/cantor-intersection-theorem|Cantor intersection theorem]] in the usual metric on $\mathbb{R}$.
