+++
id = "real-analysis/uniform-convergence-supnorm"
title = "Uniform convergence in supremum norm"
kind = "knowl"
summary = "For bounded real-valued functions, uniform convergence is equivalent to convergence in the supremum norm."
aliases = ["uniform-convergence-supnorm", "Uniform convergence in supremum norm"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/uniform-convergence-supnorm.md"
+++

**Uniform convergence in supremum norm:** Let $E$ be a set and let $f_n,f:E\to\mathbb{R}$ be bounded functions. Then $f_n\to f$ [[real-analysis/uniform-convergence|uniformly]] on $E$ if and only if
\[
\|f_n-f\|_\infty \longrightarrow 0,
\]
where $\|g\|_\infty=\sup_{x\in E}|g(x)|$ is the [[real-analysis/supremum-norm|supremum norm]].

In particular, uniform convergence is exactly convergence in the metric induced by the supremum norm, which underlies the [[real-analysis/space-of-continuous-functions|space of continuous functions]] equipped with $\|\cdot\|_\infty$.
