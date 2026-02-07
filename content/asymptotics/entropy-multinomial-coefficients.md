---
title: "Entropy and multinomial coefficients"
description: "Approximations and bounds relating multinomial coefficients to Shannon entropy."
---

Multinomial coefficients have exponential growth rates governed by entropy. This connection underlies many results in information theory and large deviations, including the {{< knowl id="method-of-types" >}}.

## Multinomial coefficient and empirical proportions
Let $n_1,\dots,n_k$ be nonnegative integers with $\sum_{i=1}^k n_i = n$. The multinomial coefficient is
$$
{n \choose n_1,\dots,n_k} \;=\; \frac{n!}{\prod_{i=1}^k n_i!},
$$

where $n! = n(n-1)\cdots 1$ is the factorial.

Define proportions $p_i = n_i/n$ (so $\sum_i p_i = 1$). The (natural-log) Shannon entropy is
$$
H(p) = -\sum_{i=1}^k p_i \log p_i.
$$

(Using base-2 logarithms multiplies all entropy expressions by $\log 2$.)

## Main asymptotic principle
Using {{< knowl id="stirlings-approximation" >}}, one obtains
$$
\log {n \choose n_1,\dots,n_k} = n H(p) + O(\log n)
\quad (n\to\infty),
$$

as long as the number of categories $k$ is fixed (and typically assuming each $p_i$ is bounded away from $0$ to avoid singular prefactors).

A more detailed approximation (when all $p_i>0$) is
$$
{n \choose n_1,\dots,n_k}
\approx
\frac{e^{nH(p)}}{(2\pi n)^{(k-1)/2}\sqrt{p_1p_2\cdots p_k}},
$$

where “$\approx$” means the ratio tends to $1$ under standard regularity conditions.

## Simple entropy bounds (polynomial accuracy)
There are widely used bounds that capture the correct exponential rate without tracking constants:
$$
(n+1)^{-k}\,e^{nH(p)}
\;\le\;
{n \choose n_1,\dots,n_k}
\;\le\;
e^{nH(p)}.
$$
These bounds are especially convenient when only exponential rates matter (e.g., in large deviation estimates).

### Proof idea for the upper bound
Apply the multinomial theorem with weights $p_i$:
$$
1 = \Bigl(\sum_{i=1}^k p_i\Bigr)^n = \sum_{\sum n_i=n} {n \choose n_1,\dots,n_k}\prod_{i=1}^k p_i^{n_i}.
$$

Every term is nonnegative, so for the particular $(n_1,\dots,n_k)$,
$$
{n \choose n_1,\dots,n_k}\prod_{i=1}^k p_i^{n_i} \le 1,
$$
hence
$$
{n \choose n_1,\dots,n_k} \le \prod_{i=1}^k p_i^{-n_i} = e^{nH(p)}.
$$

## Why this matters
- The exponential size of a “type class” (all sequences with the same empirical proportions) is controlled by $e^{nH(p)}$, up to polynomial factors; this is the core counting step in the {{< knowl id="method-of-types" >}}.
- Many probability bounds reduce to comparing $e^{nH(p)}$ with likelihood terms, producing Kullback–Leibler divergence rates.
