+++
id = "real-analysis/supremum-norm"
title = "Supremum norm"
kind = "knowl"
summary = "A norm on bounded functions given by the supremum of absolute values."
aliases = ["supremum-norm", "Supremum norm"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/supremum-norm.md"
+++

The **supremum norm** of a bounded function $f:X\to\mathbb{R}$ is
\[
\|f\|_\infty=\sup_{x\in X} |f(x)|.
\]
Here $\sup$ denotes the [[real-analysis/supremum|supremum]] and $|\cdot|$ is the [[real-analysis/absolute-value|absolute value]].

The supremum norm is the standard way to measure uniform size of functions and underlies the [[real-analysis/uniform-metric|uniform metric]]. On many domains of interest (for example, a closed interval), continuous functions lie in the [[real-analysis/space-of-continuous-functions|space of continuous functions]] and are bounded, so $\|\cdot\|_\infty$ is finite.

**Examples:**
- For $f(x)=\sin x$ on $\mathbb{R}$, $\|f\|_\infty=1$.
- For $f(x)=x^2$ on $[-1,1]$, $\|f\|_\infty=1$ (the maximum is attained at $x=\pm 1$).
