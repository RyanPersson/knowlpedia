+++
id = "convex-analysis/closure-of-a-set"
title = "Closure"
kind = "knowl"
summary = "The smallest closed set containing a given set"
aliases = ["closure-of-a-set", "Closure"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/closure-of-a-set.md"
+++

Let $(X,d)$ be a metric space and let $E\subset X$.

The **closure** of $E$, denoted $\overline{E}$, is defined as
$$
\overline{E}:=\bigcap\{\,F\subset X \mid F \text{ is closed and } E\subset F\,\}.
$$

Equivalently, $\overline{E}$ is the **smallest** [[convex-analysis/closed-subset|closed set]] containing $E$.

A useful pointwise characterization is given by [[convex-analysis/closure-characterized-by-ball-intersections|ball intersections]], and in metric spaces there is also a sequence characterization (see [[convex-analysis/closure-characterized-by-convergent-sequences|closure via sequences]]).

**Examples:**
- In $\mathbb{R}$, $\overline{(0,1)}=[0,1]$.
- If $E$ is closed, then $\overline{E}=E$.
- If $E$ is dense in $X$ (e.g., $\mathbb{Q}$ in $\mathbb{R}$), then $\overline{E}=X$.
