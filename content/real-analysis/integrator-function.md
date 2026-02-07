---
title: "Integrator function"
description: "The function whose increments weight the sums in a Riemann–Stieltjes integral."
---

An **integrator function** on $[a,b]$ is a function $\alpha:[a,b]\to\mathbb R$ used to weight increments in the definition of the {{< knowl id="riemann-stieltjes-integral" text="Riemann–Stieltjes integral" >}}: the associated sums use the differences $\alpha(x_i)-\alpha(x_{i-1})$ along partitions.

In most standard existence theorems, $\alpha$ is assumed to be {{< knowl id="monotone-function" text="monotone" >}} or, more generally, a {{< knowl id="bounded-variation-function" text="function of bounded variation" >}}, which guarantees good control of these increments.

**Examples:**
- $\alpha(x)=x$ recovers the usual {{< knowl id="riemann-integral" text="Riemann integral" >}} from the Riemann–Stieltjes integral.
- Any {{< knowl id="step-function" text="step function" >}} $\alpha$ on $[a,b]$ (for instance, one with a single jump) is an integrator function commonly used to model point-mass contributions.
