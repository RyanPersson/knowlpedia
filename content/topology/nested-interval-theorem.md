---
title: "Nested interval theorem"
description: "A nested sequence of nonempty closed intervals in the real line has nonempty intersection"
---

**Nested interval theorem:** Let $(I_n)_{n\in\mathbb{N}}$ be a sequence of nonempty closed {{< knowl id="interval" section="real-analysis" text="intervals" >}} in $\mathbb{R}$ such that $I_{n+1}\subseteq I_n$ for all $n$. Then $\bigcap_{n\in\mathbb{N}} I_n\neq\varnothing$.

More precisely, if $I_n=[a_n,b_n]$, then $\bigcap_{n\in\mathbb{N}} I_n=[\sup_n a_n,\inf_n b_n]$, using {{< knowl id="supremum" section="real-analysis" text="supremum" >}} and {{< knowl id="infimum" section="real-analysis" text="infimum" >}}. If additionally $b_n-a_n\to 0$, then the intersection is a single point.

This can be viewed as a special case of the {{< knowl id="cantor-intersection-theorem" text="Cantor intersection theorem" >}} in the usual metric on $\mathbb{R}$.
