+++
id = "real-analysis/continuity-via-sequences"
title = "Continuity via sequences"
kind = "knowl"
summary = "In metric spaces, f is continuous at x iff it preserves limits of sequences converging to x"
aliases = ["continuity-via-sequences", "Continuity via sequences"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/continuity-via-sequences.md"
+++

**Continuity via sequences**: Let $(X,d_X)$ and $(Y,d_Y)$ be [[topology/metric-space|metric spaces]] and let $f:X\to Y$. Then $f$ is [[real-analysis/continuity-at-a-point|continuous at]] $x\in X$ if and only if for every sequence $(x_n)$ in $X$,
$x_n\to x \quad\Longrightarrow\quad f(x_n)\to f(x).$

This is one of the most-used characterizations of continuity in analysis: it converts an $\varepsilon$–$\delta$ condition into a limit-preservation property.
