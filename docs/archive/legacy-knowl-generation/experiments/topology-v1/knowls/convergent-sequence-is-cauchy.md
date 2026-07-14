---
title: "Convergent sequence is Cauchy"
description: "Any convergent sequence in a metric space is automatically Cauchy."
---

**Convergent sequence is Cauchy**: Let $(X,d)$ be a metric space. If $(x_n)$ is a {{< knowl id="convergent-sequence" text="convergent sequence" >}} in $X$, then it is a {{< knowl id="cauchy-sequence" text="Cauchy sequence" >}}.

This gives one direction of the relationship between convergence and the Cauchy property; the converse holds exactly in a {{< knowl id="complete-metric-space" text="complete metric space" >}}.

**Proof sketch** *(optional, include for major theorems)*:  
If $x_n\to x$, choose $N$ so that $d(x_n,x)<\varepsilon/2$ for all $n\ge N$. Then for $m,n\ge N$, the triangle inequality gives $d(x_m,x_n)\le d(x_m,x)+d(x,x_n)<\varepsilon$.
