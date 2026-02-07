---
title: "Limit inferior (lim inf)"
description: "The smallest limit point of a bounded sequence, or equivalently the supremum of infima of tails."
---

The **limit inferior** (or **lim inf**) of a bounded sequence \((x_n)\) in \(\mathbb{R}\) is
$$
\liminf_{n \to \infty} x_n = \lim_{n \to \infty} \inf_{k \geq n} x_k = \sup_{n \geq 1} \inf_{k \geq n} x_k.
$$

## Characterizations
For a {{< knowl id="bounded-sequence" text="bounded sequence" >}} \((x_n)\), the lim inf equals:

1. The smallest {{< knowl id="limit-point" section="topology" text="limit point" >}} of the sequence.
2. The infimum of the set of all {{< knowl id="subsequence" text="subsequential" >}} limits.

## Properties
- \(\liminf x_n \leq \limsup x_n\) always.
- The sequence converges if and only if \(\liminf x_n = \limsup x_n\).
- \(\liminf(-x_n) = -\limsup(x_n)\).
- \(\liminf(x_n + y_n) \geq \liminf x_n + \liminf y_n\) (superadditivity).

## Extended values
For unbounded sequences: \(\liminf x_n = -\infty\) if \((x_n)\) is unbounded below, and \(\liminf x_n = +\infty\) if \(x_n \to +\infty\).

## Example
For \(x_n = (-1)^n + 1/n\): \(\liminf x_n = -1\), \(\limsup x_n = 1\).
