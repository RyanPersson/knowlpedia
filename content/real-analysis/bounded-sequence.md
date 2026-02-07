---
title: "Bounded sequence"
description: "A sequence whose terms all lie within some fixed distance from the origin."
---

A sequence \((x_n)\) in a {{< knowl id="metric-space" section="topology" text="metric space" >}} \((X, d)\) is **bounded** if its range \(\{x_n : n \in \mathbb{N}\}\) is a {{< knowl id="bounded-set" section="topology" text="bounded set" >}}.

## In \(\mathbb{R}\)
A real sequence \((x_n)\) is bounded if there exists \(M > 0\) such that \(|x_n| \leq M\) for all \(n\).

Equivalently, \((x_n)\) is bounded if it is both bounded above and bounded below:
$$
\inf_n x_n > -\infty \quad \text{and} \quad \sup_n x_n < \infty.
$$

## Key results
- Every {{< knowl id="convergent-sequence" section="topology" text="convergent sequence" >}} is bounded (but not conversely).
- Every bounded sequence in \(\mathbb{R}^n\) has a convergent {{< knowl id="subsequence" text="subsequence" >}} ({{< knowl id="bolzano-weierstrass-theorem" section="topology" text="Bolzano-Weierstrass" >}}).
- Every bounded monotone sequence in \(\mathbb{R}\) converges.

## Examples
- \(((-1)^n)\) is bounded but not convergent.
- \((1/n)\) is bounded and convergent.
- \((n)\) is unbounded.
