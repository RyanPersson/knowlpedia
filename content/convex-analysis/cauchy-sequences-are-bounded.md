---
title: "Cauchy sequences are bounded"
description: "A Cauchy sequence must lie in some ball"
---

**Proposition.**
Every {{< knowl id="cauchy-sequence" section="topology" text="Cauchy sequence" >}} in a metric space is bounded.

**Proof sketch.** Take $\varepsilon=1$ in the Cauchy condition to get $N$ with $d(x_n,x_N)<1$ for all $n\ge N$, so the tail lies in $B(x_N;1)$. The finitely many initial terms are bounded, so all terms lie in some closed ball $B'(x_N;r)$ for $r=\max\{d(x_1,x_N),\dots,d(x_{N-1},x_N),1\}$.
