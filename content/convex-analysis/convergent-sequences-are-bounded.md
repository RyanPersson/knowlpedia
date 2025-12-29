---
title: "Convergent sequences are bounded"
description: "A convergent sequence in a metric space must lie in some ball"
---

**Proposition.**
Any {{< knowl id="convergence-of-a-sequence" text="convergent sequence" >}} in a metric space is bounded.

**Proof sketch.** If $x_n\to a$, then for $\varepsilon=1$ there exists $N$ such that $x_n\in B(a;1)$ for all $n\ge N$. The finitely many initial terms $\{x_1,\dots,x_{N-1}\}$ lie in some closed ball around $a$ of radius $r:=\max\{d(x_1,a),\dots,d(x_{N-1},a),1\}$. Hence all terms lie in $B'(a;r)$, proving boundedness (in the sense of {{< knowl id="bounded-set-and-bounded-sequence" text="bounded sequences" >}}).
