+++
id = "convex-analysis/complete-metric-space-complete-subset"
title = "Complete metric space and complete subset"
kind = "knowl"
summary = "A metric space is complete if every Cauchy sequence converges (in the space)"
aliases = ["complete-metric-space-complete-subset", "Complete metric space and complete subset"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/complete-metric-space-complete-subset.md"
+++

A [[convex-analysis/metric-metric-space|metric space]] $(X,d)$ is **complete** if every [[topology/cauchy-sequence|Cauchy sequence]] $(x_n)$ in $X$ [[convex-analysis/convergence-of-a-sequence|converges]] to some point $x\in X$.

A subset $E\subset X$ is called **complete** if the restricted metric space $(E,d|_{E\times E})$ is complete; equivalently, every Cauchy sequence in $E$ converges to a point of $E$.

**Context.** Completeness is the property that "no limit points are missing." It is central in analysis (e.g., for existence theorems based on Cauchy sequences).

**Examples:**
- $(\mathbb{R}^k,d)$ with the usual Euclidean distance is complete (see [[convex-analysis/completeness-of-rk|Completeness of R^k]]).
- The open interval $(0,1)\subset\mathbb{R}$ with the usual distance is *not* complete: the Cauchy sequence $x_n=1/n$ converges to $0\notin(0,1)$.
- If $X$ is complete and $E\subset X$ is [[convex-analysis/closed-subset|closed]], then $E$ is complete (see [[convex-analysis/completeness-implies-closedness-closed-subsets-of-complete-spaces-are-complete|closed subsets of complete spaces are complete]]).
