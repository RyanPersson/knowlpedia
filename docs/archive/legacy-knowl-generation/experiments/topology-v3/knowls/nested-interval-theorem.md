---
title: "Nested interval theorem"
description: "A nested sequence of nonempty closed bounded intervals has nonempty intersection."
---

**Nested interval theorem:** Let $[a_n,b_n]$ be a sequence of nonempty closed intervals in $\mathbb{R}$ such that $[a_{n+1},b_{n+1}]\subseteq [a_n,b_n]$ for all $n$. Then
\[
\bigcap_{n=1}^\infty [a_n,b_n]\neq\varnothing.
\]
Moreover, if $b_n-a_n\to 0$, then the intersection consists of exactly one point.

This is a special case of the {{{< knowl id="cantor-intersection-theorem" text="Cantor intersection theorem" >}}} (applied to nested closed sets whose {{{< knowl id="diameter" text="diameters" >}}} shrink to $0$) and reflects the completeness of the usual metric on $\mathbb{R}$.
