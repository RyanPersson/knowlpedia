+++
id = "real-analysis/monotone-sequence-convergence-theorem"
title = "Monotone Sequence Convergence Theorem"
kind = "knowl"
summary = "Every bounded monotone real sequence converges, with limit given by a supremum or infimum."
aliases = ["monotone-sequence-convergence-theorem", "Monotone Sequence Convergence Theorem"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/monotone-sequence-convergence-theorem.md"
+++

**Monotone sequence convergence theorem:** Let $(a_n)$ be a [[real-analysis/monotone-sequence|monotone sequence]] of real numbers.

- If $(a_n)$ is increasing and [[real-analysis/bounded-above|bounded above]], then $(a_n)$ converges and
\[
\lim_{n\to\infty} a_n=\sup\{a_n:\ n\in\mathbb{N}\}.
\]
- If $(a_n)$ is decreasing and [[real-analysis/bounded-below|bounded below]], then $(a_n)$ converges and
\[
\lim_{n\to\infty} a_n=\inf\{a_n:\ n\in\mathbb{N}\}.
\]

This theorem is a primary working form of the [[real-analysis/completeness-axiom|completeness axiom]] and is used throughout real analysis to produce limits from order and boundedness information.
