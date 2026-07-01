+++
id = "real-analysis/bounded-sequence"
title = "Bounded sequence"
kind = "knowl"
summary = "A sequence whose terms all lie within some fixed distance from the origin."
aliases = ["bounded-sequence", "Bounded sequence"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/bounded-sequence.md"
+++

A sequence \((x_n)\) in a [[topology/metric-space|metric space]] \((X, d)\) is **bounded** if its range \(\{x_n : n \in \mathbb{N}\}\) is a [[topology/bounded-set|bounded set]].

## In \(\mathbb{R}\)
A real sequence \((x_n)\) is bounded if there exists \(M > 0\) such that \(|x_n| \leq M\) for all \(n\).

Equivalently, \((x_n)\) is bounded if it is both bounded above and bounded below:
$$
\inf_n x_n > -\infty \quad \text{and} \quad \sup_n x_n < \infty.
$$

## Key results
- Every [[topology/convergent-sequence|convergent sequence]] is bounded (but not conversely).
- Every bounded sequence in \(\mathbb{R}^n\) has a convergent [[real-analysis/subsequence|subsequence]] ([[topology/bolzano-weierstrass-theorem|Bolzano-Weierstrass]]).
- Every bounded monotone sequence in \(\mathbb{R}\) converges.

## Examples
- \(((-1)^n)\) is bounded but not convergent.
- \((1/n)\) is bounded and convergent.
- \((n)\) is unbounded.
