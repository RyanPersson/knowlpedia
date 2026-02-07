---
title: "Function of bounded variation"
description: "A function whose total variation on an interval is finite."
---

A **function of bounded variation** on $[a,b]$ is a function $\alpha:[a,b]\to\mathbb R$ whose {{< knowl id="total-variation" text="total variation" >}} on $[a,b]$ is finite, i.e.
\[
V_a^b(\alpha)=\sup_P \sum_{i=1}^n |\alpha(x_i)-\alpha(x_{i-1})|<\infty,
\]
where the supremum is taken over all {{< knowl id="partition-of-an-interval" text="partitions" >}} $P=\{x_0,\dots,x_n\}$ of $[a,b]$.

Functions of bounded variation are important because they provide a broad class of {{< knowl id="integrator-function" text="integrator functions" >}} for the {{< knowl id="riemann-stieltjes-integral" text="Riemann–Stieltjes integral" >}} and admit structural decompositions such as the {{< knowl id="jordan-decomposition-lemma" text="Jordan decomposition" >}}.

**Examples:**
- Any {{< knowl id="monotone-function" text="monotone function" >}} on $[a,b]$ has bounded variation.
- The function $\alpha(x)=\sin x$ has bounded variation on $[0,2\pi]$.
