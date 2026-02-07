---
title: "Method of types"
description: "Counting and probability estimates for sequences grouped by their empirical distribution."
---

The method of types is a set of counting and probability tools for sequences over a finite alphabet. It is foundational in information theory and large deviations: it turns questions about probabilities of empirical frequencies into entropy and divergence calculations.

It relies on the entropy–counting relationship in {{< knowl id="entropy-multinomial-coefficients" >}}.

## Types and type classes
Let $\mathcal{A}$ be a finite alphabet with $|\mathcal{A}|=m$, and let $x^n=(x_1,\dots,x_n)\in\mathcal{A}^n$.

- The **type** (empirical distribution) of $x^n$ is the probability mass function $P_{x^n}$ on $\mathcal{A}$ defined by
  $$
  P_{x^n}(a)=\frac{1}{n}\,\#\{i: x_i=a\}.
  $$

- For a type $P$ with denominator $n$ (i.e., all $nP(a)$ are integers), the **type class** is
  $$
  T(P)=\{x^n\in\mathcal{A}^n: P_{x^n}=P\}.
  $$

## Counting: size of a type class
Write $n_a = nP(a)$ for each $a\in\mathcal{A}$. Then
$$
|T(P)|=\frac{n!}{\prod_{a\in\mathcal{A}} n_a!},
$$
a multinomial coefficient.

Let
$$
H(P)=-\sum_{a\in\mathcal{A}} P(a)\log P(a)
$$
(natural-log entropy). Then the type class size satisfies the standard bounds
$$
(n+1)^{-m}\,e^{nH(P)} \;\le\; |T(P)| \;\le\; e^{nH(P)}.
$$

In particular, $\log |T(P)| = nH(P) + O(\log n)$.

## Counting: number of possible types
The number of distinct types on $\mathcal{A}$ with denominator $n$ is at most
$$
(n+1)^m,
$$

because each $P(a)$ must be in $\{0,1/n,2/n,\dots,1\}$.

## Probability of a type class under an i.i.d. law
Let $Q$ be a distribution on $\mathcal{A}$, and let $X^n\sim Q^{\otimes n}$ be i.i.d. draws.

For any fixed type $P$ with denominator $n$, every sequence $x^n\in T(P)$ has the same probability:
$$
Q^{\otimes n}(x^n)=\prod_{a\in\mathcal{A}} Q(a)^{nP(a)}.
$$
Therefore,
$$
Q^{\otimes n}(T(P)) = |T(P)| \prod_{a\in\mathcal{A}} Q(a)^{nP(a)}.
$$

Introduce the (natural-log) Kullback–Leibler divergence
$$
D(P\|Q)=\sum_{a\in\mathcal{A}} P(a)\log\frac{P(a)}{Q(a)}.
$$

Using $|T(P)|\approx e^{nH(P)}$ gives the characteristic exponential rate
$$
Q^{\otimes n}(T(P)) \approx e^{-nD(P\|Q)}
$$
(up to polynomial factors). A standard bound pair is
$$
(n+1)^{-m}\,e^{-nD(P\|Q)} \;\le\; Q^{\otimes n}(T(P)) \;\le\; e^{-nD(P\|Q)}.
$$

## Why this is useful
- Converts empirical-frequency events into entropy/divergence exponents.
- Provides finite-$n$ (non-asymptotic) bounds with only polynomial slack.
- Serves as a discrete, combinatorial route to large deviation principles (e.g., the intuition behind Sanov-type results).
