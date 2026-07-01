+++
id = "real-analysis/m-test-continuity-integration-corollary"
title = "M-test continuity and integration corollary"
kind = "knowl"
summary = "Under the M-test, a function series converges uniformly, giving continuity and term-by-term integration"
aliases = ["m-test-continuity-integration-corollary", "M-test continuity and integration corollary"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/m-test-continuity-integration-corollary.md"
+++

Let $X$ be a set and let $f_n:X\to\mathbb{R}$ (or $\mathbb{C}$). Suppose:
- each $f_n$ is [[real-analysis/continuity-on-a-set|continuous]] on $X$ (when $X$ is a [[topology/metric-space|metric space]]), and
- there exist $M_n\ge 0$ with $|f_n(x)|\le M_n$ for all $x\in X$, and $\sum M_n$ [[real-analysis/convergent-series|converges]].

**Corollary**:
- The series $\sum f_n$ [[real-analysis/uniform-convergence-of-a-sequence-of-functions|converges uniformly]] on $X$ ([[real-analysis/weierstrass-m-test|Weierstrass M-test]]).
- Hence its sum $f=\sum f_n$ is continuous ([[real-analysis/uniform-limit-theorem|uniform limit of continuous functions]]).
- If $X=[a,b]$ and each $f_n$ is [[real-analysis/riemann-integrable-function|Riemann integrable]], then
  $
  \int_a^b \sum_{n=1}^\infty f_n(x)\,dx=\sum_{n=1}^\infty \int_a^b f_n(x)\,dx
  $
  (term-by-term integration).

**Connection to parent theorems**:
Combine the Weierstrass M-test with the uniform limit theorem for continuity and the [[real-analysis/uniform-limit-of-integrable-functions|uniform convergence-and-integration theorem]].
