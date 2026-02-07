---
title: "Primary ideal"
description: "An ideal Q such that ab in Q forces a in Q or a power of b in Q."
---

Let $R$ be a commutative ring. A **primary ideal** $Q\subsetneq R$ is an {{< knowl id="ideal" text="ideal" >}} such that whenever $ab\in Q$ (with $a,b\in R$), then either $a\in Q$ or $b^n\in Q$ for some integer $n\ge 1$.

Primary ideals interpolate between prime ideals and powers: the {{< knowl id="radical-of-ideal" text="radical" >}} $\sqrt{Q}$ is always a {{< knowl id="prime-ideal" text="prime ideal" >}}, and elements outside $\sqrt{Q}$ act as non-zerodivisors on $R/Q$ up to {{< knowl id="nilpotent-element" text="nilpotence" >}}.

**Examples:**
- In $\mathbb{Z}$, the ideal $(p^n)$ is primary for any prime $p$ and $n\ge 1$.
- In $k[x,y]$, the ideal $(x^2,y)$ is primary; its radical is $(x,y)$.
- The ideal $(xy)\subset k[x,y]$ is not primary: $x\cdot y\in (xy)$ but $x\notin (xy)$ and $y^n\notin (xy)$ for all $n\ge 1$.