---
title: "M-test continuity and integration corollary"
description: "Under the M-test, a function series converges uniformly, giving continuity and term-by-term integration"
---

Let $X$ be a set and let $f_n:X\to\mathbb{R}$ (or $\mathbb{C}$). Suppose:
- each $f_n$ is {{< knowl id="continuity-on-a-set" text="continuous" >}} on $X$ (when $X$ is a {{< knowl id="metric-space" section="topology" text="metric space" >}}), and
- there exist $M_n\ge 0$ with $|f_n(x)|\le M_n$ for all $x\in X$, and $\sum M_n$ {{< knowl id="convergent-series" text="converges" >}}.

**Corollary**:
- The series $\sum f_n$ {{< knowl id="uniform-convergence-of-a-sequence-of-functions" text="converges uniformly" >}} on $X$ ({{< knowl id="weierstrass-m-test" text="Weierstrass M-test" >}}).
- Hence its sum $f=\sum f_n$ is continuous ({{< knowl id="uniform-limit-theorem" text="uniform limit of continuous functions" >}}).
- If $X=[a,b]$ and each $f_n$ is {{< knowl id="riemann-integrable-function" text="Riemann integrable" >}}, then
  $
  \int_a^b \sum_{n=1}^\infty f_n(x)\,dx=\sum_{n=1}^\infty \int_a^b f_n(x)\,dx
  $
  (term-by-term integration).

**Connection to parent theorems**:
Combine the Weierstrass M-test with the uniform limit theorem for continuity and the {{< knowl id="uniform-limit-of-integrable-functions" text="uniform convergence-and-integration theorem" >}}.
