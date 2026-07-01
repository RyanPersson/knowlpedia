+++
id = "real-analysis/local-extremum"
title = "Local extremum"
kind = "knowl"
summary = "A point where a function attains a local maximum or local minimum."
aliases = ["local-extremum", "Local extremum"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/local-extremum.md"
+++

A **local extremum** of a function $f:I\to\mathbb{R}$ at a point $a\in I$ means either a local maximum or a local minimum: $a$ is a local maximum if there exists $\delta>0$ such that $f(a)\ge f(x)$ for all $x\in I$ with $|x-a|<\delta$, and a local minimum if there exists $\delta>0$ such that $f(a)\le f(x)$ for all such $x$.

Local extrema are closely connected to [[real-analysis/critical-point|critical points]] and the [[real-analysis/derivative|derivative]] (when it exists). Criteria such as the [[real-analysis/second-derivative-tests|second derivative tests]] help distinguish maxima from minima.

**Examples:**
- For $f(x)=x^2$, the point $a=0$ is a local minimum.
- For $f(x)=-x^2$, the point $a=0$ is a local maximum.
