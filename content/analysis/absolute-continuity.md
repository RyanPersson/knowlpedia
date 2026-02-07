---
title: "Absolute continuity"
description: "A strong continuity condition on an interval controlling total change over collections of small subintervals"
---

A function $f:[a,b]\to\mathbb{R}$ is **absolutely continuous** if for every $\varepsilon>0$ there exists $\delta>0$ such that for every finite collection of pairwise disjoint subintervals $(a_k,b_k)\subseteq [a,b]$ with $\sum_k (b_k-a_k)<\delta$, one has
\[
\sum_k |f(b_k)-f(a_k)|<\varepsilon.
\]

Absolute continuity is stronger than {{< knowl id="uniform-continuity" section="real-analysis" text="uniform continuity" >}} and implies {{< knowl id="bounded-variation-function" section="real-analysis" text="bounded variation" >}}. A key characterization is that $f$ is absolutely continuous if and only if there exists a {{< knowl id="lebesgue-integrable-function" section="measure-theory" text="Lebesgue integrable function" >}} $g$ on $[a,b]$ such that $f(x)=f(a)+\int_a^x g(t)\,dt$ for all $x\in[a,b]$ (with the integral taken as the {{< knowl id="lebesgue-integral" section="measure-theory" text="Lebesgue integral" >}}); in that case the {{< knowl id="derivative" section="real-analysis" text="derivative" >}} satisfies $f'(x)=g(x)$ {{< knowl id="almost-everywhere" section="measure-theory" text="almost everywhere" >}}.

**Examples:**
- If $g$ is Lebesgue integrable on $[a,b]$ and $f(x)=\int_a^x g(t)\,dt$, then $f$ is absolutely continuous.
- Every {{< knowl id="lipschitz-continuity" section="topology" text="Lipschitz continuous" >}} function on $[a,b]$ is absolutely continuous.
- The Cantor function is continuous and of bounded variation but not absolutely continuous; it increases on a {{< knowl id="set-of-measure-zero-in-rk" section="measure-theory" text="set of measure zero" >}}.
