---
title: "Cantor intersection theorem"
description: "Nested closed sets with shrinking diameter meet in exactly one point in a complete space."
---

**Cantor intersection theorem**: Let $(X,d)$ be a {{< knowl id="complete-metric-space" text="complete metric space" >}} and let $F_1 \supseteq F_2 \supseteq F_3 \supseteq \cdots$ be a nested sequence of nonempty {{< knowl id="closed-set" text="closed sets" >}} in $X$. If the {{< knowl id="diameter" text="diameters" >}} satisfy $\operatorname{diam}(F_n)\to 0$, then
$$
\bigcap_{n=1}^\infty F_n
$$
(where the operation is {{< knowl id="intersection" text="intersection" >}}) consists of exactly one point.

This is a metric-space generalization of the {{< knowl id="nested-interval-theorem" text="nested interval theorem" >}}.

**Proof sketch** *(optional, include for major theorems)*:  
Pick $x_n\in F_n$. The nesting and shrinking diameter condition imply $(x_n)$ is Cauchy. By completeness it converges to some $x\in X$. Closedness of each $F_n$ forces $x\in F_n$ for all $n$, hence $x$ lies in the intersection. If $y$ is another point in the intersection, then $d(x,y)\le \operatorname{diam}(F_n)$ for every $n$, so $d(x,y)=0$ and $x=y$.
