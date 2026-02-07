---
title: "Fubini theorem for Riemann integrals"
description: "For continuous functions on a rectangle, iterated integrals exist and agree with the double Riemann integral."
---

**Fubini theorem (Riemann):** 

Let $a<b$ and $c<d$, and let $f:[a,b]\times[c,d]\to\mathbb{R}$ be continuous. Then $f$ is {{< knowl id="multiple-riemann-integral" text="Riemann integrable on the rectangle" >}}, the two {{< knowl id="iterated-integral" text="iterated integrals" >}} exist, and
$$
\int_a^b\left(\int_c^d f(x,y)\,dy\right)dx = \int_c^d\left(\int_a^b f(x,y)\,dx\right)dy =
$$
$$
\iint_{[a,b]\times[c,d]} f(x,y)\,dA.
$$

This allows one to compute a {{< knowl id="multiple-riemann-integral" text="double Riemann integral" >}} by integrating one variable at a time, and it is a key tool for evaluating many {{< knowl id="multiple-riemann-integral" text="multiple integrals" >}} in practice.
