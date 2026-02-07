---
title: "Convergent sequences are Cauchy"
description: "Convergence implies the Cauchy property in any metric space"
---

**Proposition.**
If $(x_n)$ is a convergent sequence in a metric space, then it is a {{< knowl id="cauchy-sequence" section="topology" text="Cauchy sequence" >}}.

**Proof sketch.** If $x_n\to a$, then for $\varepsilon>0$ choose $N$ such that $d(x_n,a)<\varepsilon/2$ for all $n\ge N$. For $m,n\ge N$,
$$
d(x_m,x_n)\le d(x_m,a)+d(a,x_n)<\varepsilon/2+\varepsilon/2=\varepsilon
$$
by the triangle inequality.
