+++
id = "real-analysis/local-maximum-local-minimum"
title = "Local maximum and local minimum"
kind = "knowl"
summary = "A point where a function attains a maximum/minimum relative to nearby points."
aliases = ["local-maximum-local-minimum", "Local maximum and local minimum"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/local-maximum-local-minimum.md"
+++

Let $f:E\to\mathbb{R}$ with $E\subseteq X$ where $(X,d)$ is a [[topology/metric-space|metric space]], and let $a\in E$.

- The point $a$ is a **local maximum** of $f$ if there exists $r>0$ such that for all $x\in E\cap B(a,r)$,
  $$f(x)\le f(a).$$

- The point $a$ is a **local minimum** of $f$ if there exists $r>0$ such that for all $x\in E\cap B(a,r)$,
  $$f(a)\le f(x).$$

Local extrema are "nearby" maxima/minima. In one-variable calculus, local extrema in the interior of an [[real-analysis/interval|interval]] are closely tied to [[real-analysis/critical-point|critical points]] and [[real-analysis/derivative|derivative]] tests.

**Examples:**
- For $f(x)=x^2$ on $\mathbb{R}$, $0$ is a local minimum.
- For $f(x)=-x^2$ on $\mathbb{R}$, $0$ is a local maximum.
- For $f(x)=x^3$ on $\mathbb{R}$, there are no local maxima or minima (even though $f'(0)=0$).
