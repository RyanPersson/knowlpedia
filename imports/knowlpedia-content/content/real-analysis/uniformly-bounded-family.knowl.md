+++
id = "real-analysis/uniformly-bounded-family"
title = "Uniformly bounded family"
kind = "knowl"
summary = "A family of functions bounded by a single constant on the whole domain."
aliases = ["uniformly-bounded-family", "Uniformly bounded family"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/uniformly-bounded-family.md"
+++

A family $\mathcal{F}$ of functions $f:X\to\mathbb{R}$ is **uniformly bounded** if there exists $M<\infty$ such that
\[
|f(x)|\le M \quad \text{for all } f\in\mathcal{F}\text{ and all } x\in X.
\]
Equivalently, if every $f\in\mathcal{F}$ is bounded, then $\sup_{f\in\mathcal{F}}\|f\|_\infty<\infty$ in terms of the [[real-analysis/supremum-norm|supremum norm]].

Uniform boundedness implies [[real-analysis/pointwise-bounded-family|pointwise boundedness]] and is a natural hypothesis when working with the [[real-analysis/uniform-metric|uniform metric]]. It is also one of the typical ingredients in compactness criteria alongside [[real-analysis/equicontinuity|equicontinuity]].

**Examples:**
- On $\mathbb{R}$, the family $f_n(x)=\sin(nx)$ is uniformly bounded with $M=1$.
- On $[0,1]$, the family $f_n(x)=n x$ is not uniformly bounded.
