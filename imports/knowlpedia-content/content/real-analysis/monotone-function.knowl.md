+++
id = "real-analysis/monotone-function"
title = "Monotone function"
kind = "knowl"
summary = "A function that preserves or reverses order on an interval."
aliases = ["monotone-function", "Monotone function"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/monotone-function.md"
+++

A **monotone function** on an [[real-analysis/interval|interval]] $I\subseteq\mathbb{R}$ is a function $f:I\to\mathbb{R}$ that is either nondecreasing (if $x\le y$ implies $f(x)\le f(y)$) or nonincreasing (if $x\le y$ implies $f(x)\ge f(y)$); it is strictly increasing or strictly decreasing if the inequalities are strict whenever $x<y$.

Monotonicity rests on the [[real-analysis/order-axioms|order axioms]] for $\mathbb{R}$ and is often proved using [[real-analysis/derivative-sign-implies-monotonicity|derivative sign implies monotonicity]]. Monotone functions on compact intervals have good integration behavior, for example [[real-analysis/riemann-integrability-monotone|monotone implies Riemann integrable]].

**Examples:**
- The function $f(x)=x^3$ is strictly increasing on $\mathbb{R}$.
- The function $f(x)=\frac{1}{x}$ is strictly decreasing on $(0,\infty)$.
