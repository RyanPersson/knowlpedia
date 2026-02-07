---
title: "Uniqueness of limits"
description: "A sequence in a metric space has at most one limit"
---

**Proposition.**
A sequence in a {{< knowl id="metric-metric-space" text="metric space" >}} has at most one limit.

More precisely: if $(x_n)$ converges to $a$ and also converges to $b$, then $a=b$.

**Proof sketch.** Fix $\varepsilon>0$. For large $n$, both $d(x_n,a)<\varepsilon/2$ and $d(x_n,b)<\varepsilon/2$. Then
$$
d(a,b)\le d(a,x_n)+d(x_n,b)<\varepsilon.
$$

Since this holds for all $\varepsilon>0$, the lemma {{< knowl id="nonnegative-real-less-than-every-0-must-be-zero" text="nonnegative below every epsilon" >}} gives $d(a,b)=0$, hence $a=b$.
