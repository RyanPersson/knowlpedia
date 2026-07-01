+++
id = "real-analysis/uniform-convergence-implies-pointwise"
title = "Uniform convergence implies pointwise convergence"
kind = "knowl"
summary = "Uniform convergence guarantees pointwise convergence at every point."
aliases = ["uniform-convergence-implies-pointwise", "Uniform convergence implies pointwise convergence"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/uniform-convergence-implies-pointwise.md"
+++

**Uniform convergence implies pointwise convergence:** Let $E$ be a set and let $f_n:E\to\mathbb{R}$ (or $\mathbb{C}$) be functions. If $f_n\to f$ [[real-analysis/uniform-convergence|uniformly]] on $E$, then $f_n\to f$ [[real-analysis/pointwise-convergence|pointwise]] on $E$; that is, for every $x\in E$ we have $f_n(x)\to f(x)$.

The converse generally fails: [[real-analysis/pointwise-convergence|pointwise convergence]] alone is typically too weak to preserve analytic properties such as continuity.
