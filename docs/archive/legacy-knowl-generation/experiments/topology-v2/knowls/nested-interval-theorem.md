---
title: "Nested interval theorem"
description: "A decreasing sequence of nonempty closed intervals in the real line has nonempty intersection"
---

**Nested interval theorem:** Let $(I_n)_{n\ge 1}$ be a sequence of nonempty closed intervals in $\mathbb{R}$, where $I_n=[a_n,b_n]$, such that
\[
I_{n+1}\subseteq I_n \quad\text{for all }n.
\]
Then $\bigcap_{n=1}^\infty I_n\neq\varnothing$. Moreover, if $b_n-a_n\to 0$, then $\bigcap_{n=1}^\infty I_n$ consists of exactly one point.

This is a special case of the {{< knowl id="cantor-intersection-theorem" text="Cantor intersection theorem" >}} because $(\mathbb{R},|x-y|)$ is a {{< knowl id="complete-metric-space" text="complete metric space" >}}.
