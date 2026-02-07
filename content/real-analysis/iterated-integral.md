---
title: "Iterated integral"
description: "A repeated one-variable integration over a rectangle or product of intervals."
---

An **iterated integral** of a function $f$ on a rectangle $[a,b]\times[c,d]$ is an integral obtained by integrating in one variable first and then integrating the resulting function in the other variable. For example, the $y$-then-$x$ iterated integral is
\[
\int_a^b\left(\int_c^d f(x,y)\,dy\right)dx,
\]
provided that for each $x\in[a,b]$ the inner {{< knowl id="riemann-integral" text="Riemann integral" >}} $\int_c^d f(x,y)\,dy$ exists and the resulting function of $x$ is Riemann integrable on $[a,b]$.

Iterated integrals are compared with the {{< knowl id="multiple-riemann-integral" text="multiple Riemann integral" >}}; under appropriate hypotheses they agree by {{< knowl id="fubini-theorem-riemann" text="Fubini's theorem (Riemann)" >}}.

**Examples:**
- For $f(x,y)=xy$ on $[0,1]\times[0,1]$, one gets $\int_0^1\left(\int_0^1 xy\,dy\right)dx=\int_0^1 (x/2)\,dx=1/4$.
- If $f(x,y)=g(x)h(y)$ where $g$ is Riemann integrable on $[a,b]$ and $h$ is Riemann integrable on $[c,d]$, then the iterated integral (when defined) equals $\left(\int_a^b g(x)\,dx\right)\left(\int_c^d h(y)\,dy\right)$.
