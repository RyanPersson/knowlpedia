---
title: "Nested interval theorem"
description: "A decreasing sequence of closed bounded intervals has a nonempty intersection."
---

**Nested interval theorem**: Let $[a_1,b_1] \supseteq [a_2,b_2] \supseteq [a_3,b_3] \supseteq \cdots$ be a nested sequence of closed bounded intervals in $\mathbb{R}$. Then
$$
\bigcap_{n=1}^\infty [a_n,b_n]
$$
(their {{< knowl id="intersection" text="intersection" >}}) is nonempty.

Moreover, if $b_n-a_n \to 0$, then the intersection consists of exactly one point.

This can be viewed as a special case of the {{< knowl id="cantor-intersection-theorem" text="Cantor intersection theorem" >}} together with completeness of the real line (an instance of a {{< knowl id="complete-metric-space" text="complete metric space" >}}).

**Proof sketch** *(optional, include for major theorems)*:  
Let $a=\sup\{a_n\}$. One checks that $a\in[a_n,b_n]$ for every $n$, so $a$ lies in the intersection. If additionally $b_n-a_n\to 0$, then any two points in the intersection must be arbitrarily close (since both lie in every interval), forcing uniqueness.
