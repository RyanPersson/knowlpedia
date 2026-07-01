+++
id = "topology/curve"
title = "Curve"
kind = "knowl"
summary = "A continuous map from an interval of real numbers into a space."
aliases = ["curve"]
domains = ["topology"]
legacy_source_path = "topology/curve.md"
+++

A **curve** in a [[topology/topological-space|topological space]] $X$ is a [[topology/continuous-map|continuous map]] $\gamma\colon I\to X$, where $I\subseteq\mathbb{R}$ is an [[real-analysis/interval|interval]] (with its usual topology).

A [[topology/path|path]] is a curve with domain $[0,1]$. Curves allow other parameter intervals, which is convenient for describing parametrizations and restrictions.

**Examples:**
- The map $\gamma(t)=(t,t^2)$ (for $t\in\mathbb{R}$) is a curve in $\mathbb{R}^2$ tracing a parabola.
- If $\gamma\colon [0,2]\to X$ is continuous, then its restriction to $[0,1]$ is a curve (and in fact a path) in $X$.
