+++
id = "real-analysis/bounded-variation-function"
title = "Function of bounded variation"
kind = "knowl"
summary = "A function whose total variation on an interval is finite."
aliases = ["bounded-variation-function", "Function of bounded variation"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/bounded-variation-function.md"
+++

A **function of bounded variation** on $[a,b]$ is a function $\alpha:[a,b]\to\mathbb R$ whose [[real-analysis/total-variation|total variation]] on $[a,b]$ is finite, i.e.
\[
V_a^b(\alpha)=\sup_P \sum_{i=1}^n |\alpha(x_i)-\alpha(x_{i-1})|<\infty,
\]
where the supremum is taken over all [[real-analysis/partition-of-an-interval|partitions]] $P=\{x_0,\dots,x_n\}$ of $[a,b]$.

Functions of bounded variation are important because they provide a broad class of [[real-analysis/integrator-function|integrator functions]] for the [[real-analysis/riemann-stieltjes-integral|Riemann–Stieltjes integral]] and admit structural decompositions such as the [[real-analysis/jordan-decomposition-lemma|Jordan decomposition]].

**Examples:**
- Any [[real-analysis/monotone-function|monotone function]] on $[a,b]$ has bounded variation.
- The function $\alpha(x)=\sin x$ has bounded variation on $[0,2\pi]$.
