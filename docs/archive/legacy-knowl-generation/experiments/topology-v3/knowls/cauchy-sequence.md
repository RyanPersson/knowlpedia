---
title: "Cauchy sequence"
description: "A sequence whose terms eventually become arbitrarily close to each other."
---

A **Cauchy sequence** in a metric space $(X,d)$ is a sequence $(x_n)$ such that for every $\varepsilon>0$ there exists $N$ with $d(x_m,x_n)<\varepsilon$ for all $m,n\ge N$.

Every {{{< knowl id="convergent-sequence" text="convergent sequence" >}}} is Cauchy (see {{{< knowl id="convergent-sequence-is-cauchy" text="convergent implies Cauchy" >}}}), and every Cauchy sequence is {{{< knowl id="bounded-set" text="bounded" >}}} (see {{{< knowl id="every-cauchy-sequence-is-bounded" text="Cauchy implies bounded" >}}}). Cauchy sequences converge precisely in a {{{< knowl id="complete-metric-space" text="complete metric space" >}}}.

**Examples:**
- In $\mathbb{Q}$ with the usual metric, a sequence of rational approximations to $\sqrt{2}$ is Cauchy but does not converge in $\mathbb{Q}$ (its limit lies in $\mathbb{R}$), illustrating non-completeness.
