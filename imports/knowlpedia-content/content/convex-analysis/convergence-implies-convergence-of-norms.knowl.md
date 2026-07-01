+++
id = "convex-analysis/convergence-implies-convergence-of-norms"
title = "Convergence implies convergence of norms"
kind = "knowl"
summary = "If x_n→x, then ||x_n||→||x||"
aliases = ["convergence-implies-convergence-of-norms", "Convergence implies convergence of norms"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/convergence-implies-convergence-of-norms.md"
+++

**Proposition.**
If $(x_n)$ [[convex-analysis/convergence-in-normed-spaces|converges in norm]] to $x$ in a normed space, then
$$
\|x_n\|\to \|x\|.
$$

**Context.** This expresses continuity of the norm map $x\mapsto\|x\|$.

**Proof sketch.** By the [[real-analysis/reverse-triangle-inequality|reverse triangle inequality]],
$$
\big|\|x_n\|-\|x\|\big|\le \|x_n-x\|\to 0,
$$

hence $\|x_n\|\to \|x\|$.
