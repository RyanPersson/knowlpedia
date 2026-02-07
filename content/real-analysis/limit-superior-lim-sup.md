---
title: "Limit superior (lim sup)"
description: "The largest limit point of a bounded sequence, or equivalently the infimum of suprema of tails."
---

The **limit superior** (or **lim sup**) of a bounded sequence \((x_n)\) in \(\mathbb{R}\) is
$$
\limsup_{n \to \infty} x_n = \lim_{n \to \infty} \sup_{k \geq n} x_k = \inf_{n \geq 1} \sup_{k \geq n} x_k.
$$

## Characterizations
For a {{< knowl id="bounded-sequence" text="bounded sequence" >}} \((x_n)\), the lim sup equals:

1. The largest {{< knowl id="limit-point" section="topology" text="limit point" >}} of the sequence.
2. The supremum of the set of all {{< knowl id="subsequence" text="subsequential" >}} limits.

## Properties
- \(\liminf x_n \leq \limsup x_n\) always.
- The sequence converges if and only if \(\liminf x_n = \limsup x_n\), and then the limit equals this common value.
- \(\limsup(-x_n) = -\liminf(x_n)\).

## Extended values
For unbounded sequences: \(\limsup x_n = +\infty\) if \((x_n)\) is unbounded above, and \(\limsup x_n = -\infty\) if \(x_n \to -\infty\).

## Example
For \(x_n = (-1)^n(1 + 1/n)\): \(\limsup x_n = 1\), \(\liminf x_n = -1\).
