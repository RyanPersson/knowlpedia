+++
id = "real-analysis/pointwise-bounded-family"
title = "Pointwise bounded family"
kind = "knowl"
summary = "A family of functions that is bounded at each fixed point of the domain."
aliases = ["pointwise-bounded-family", "Pointwise bounded family"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/pointwise-bounded-family.md"
+++

A family $\mathcal{F}$ of functions $f:X\to\mathbb{R}$ is **pointwise bounded** if for every $x\in X$ the set of values $\{f(x): f\in\mathcal{F}\}$ is bounded in $\mathbb{R}$, equivalently
\[
\forall x\in X,\quad \sup_{f\in\mathcal{F}} |f(x)| < \infty.
\]

Pointwise boundedness is weaker than being [[real-analysis/uniformly-bounded-family|uniformly bounded]] (which requires one bound to work for all $x$ at once). Together with [[real-analysis/equicontinuous-family|equicontinuity]] hypotheses, it appears in compactness results for subsets of [[real-analysis/space-of-continuous-functions|spaces of continuous functions]] such as [[real-analysis/arzela-ascoli-theorem|Arzelà–Ascoli]].

**Examples:**
- On $[0,1]$, the family $\{f_n\}_{n\ge 1}$ with $f_n(x)=x^n$ is pointwise bounded since $0\le f_n(x)\le 1$ for all $x$ and $n$.
- On $[0,1]$, the family $f_n(x)=n x$ is not pointwise bounded (for any fixed $x>0$, the values $n x$ are unbounded as $n\to\infty$).
