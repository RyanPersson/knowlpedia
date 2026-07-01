+++
id = "algebra-commutative/integrally-closed-domain"
title = "Integrally closed domain"
kind = "knowl"
summary = "A domain that already contains every element of its fraction field that is integral over it."
aliases = ["integrally-closed-domain", "Integrally closed domain"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/integrally-closed-domain.md"
+++

Let $R$ be an integral domain with fraction field $K$ (a [[algebra-rings/field|field]]).

The domain $R$ is **integrally closed** if whenever $x\in K$ is integral over $R$ (in the sense of [[algebra-commutative/integral-element|integrality]]), then $x\in R$.

Equivalently, if one forms the [[algebra-commutative/integral-closure|integral closure]] of $R$ inside $K$, then $R$ is integrally closed exactly when
\[
\overline{R}^{\,K} = R.
\]

This condition is often phrased as: “$R$ has no new integral elements in its fraction field.”

## Useful perspective
Because $K$ is the localization $S^{-1}R$ with $S=R\setminus\{0\}$, integrally closedness can be viewed as a statement about integrality after [[algebra-commutative/localization-ring|inverting]] all nonzero elements.

In many situations, integrally closedness behaves well under [[algebra-commutative/localization-at-prime|localization at primes]]: roughly, $R$ is integrally closed if and only if all localizations $R_\mathfrak p$ are integrally closed.

## Examples
1. **Principal ideal domains (e.g. $\mathbb{Z}$).**
   The ring $\mathbb{Z}$ is integrally closed in $\mathbb{Q}$: any rational number integral over $\mathbb{Z}$ must be an integer (as in the [[algebra-commutative/integral-closure|integral closure]] example).

2. **Polynomial rings over a field.**
   If $k$ is a field, then $k[x_1,\dots,x_n]$ is integrally closed in its fraction field $k(x_1,\dots,x_n)$. (More generally, unique factorization domains are integrally closed.)

3. **Discrete valuation rings.**
   Any [[algebra-commutative/dvr|discrete valuation ring]] is integrally closed. Concretely, $k[[t]]$ is integrally closed in $k((t))$.

## Non-examples
- **A cusp subring.**
  $R=k[x^2,x^3]\subset k(x)$ is *not* integrally closed because $x\in k(x)$ is integral over $R$ (it satisfies $T^2-x^2=0$ with $x^2\in R$) but $x\notin R$. Its integral closure in $k(x)$ is $k[x]$.

- **A classical quadratic example.**
  $R=\mathbb{Z}[\sqrt5]$ is not integrally closed in $\mathbb{Q}(\sqrt5)$: the element $\frac{1+\sqrt5}{2}$ is integral over $R$ (it satisfies $T^2-T-1=0$) but is not in $R$.
