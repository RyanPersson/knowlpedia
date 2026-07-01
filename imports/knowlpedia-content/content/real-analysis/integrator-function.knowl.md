+++
id = "real-analysis/integrator-function"
title = "Integrator function"
kind = "knowl"
summary = "The function whose increments weight the sums in a Riemann–Stieltjes integral."
aliases = ["integrator-function", "Integrator function"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/integrator-function.md"
+++

An **integrator function** on $[a,b]$ is a function $\alpha:[a,b]\to\mathbb R$ used to weight increments in the definition of the [[real-analysis/riemann-stieltjes-integral|Riemann–Stieltjes integral]]: the associated sums use the differences $\alpha(x_i)-\alpha(x_{i-1})$ along partitions.

In most standard existence theorems, $\alpha$ is assumed to be [[real-analysis/monotone-function|monotone]] or, more generally, a [[real-analysis/bounded-variation-function|function of bounded variation]], which guarantees good control of these increments.

**Examples:**
- $\alpha(x)=x$ recovers the usual [[real-analysis/riemann-integral|Riemann integral]] from the Riemann–Stieltjes integral.
- Any [[real-analysis/step-function|step function]] $\alpha$ on $[a,b]$ (for instance, one with a single jump) is an integrator function commonly used to model point-mass contributions.
