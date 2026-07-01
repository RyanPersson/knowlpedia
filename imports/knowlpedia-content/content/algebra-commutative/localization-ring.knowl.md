+++
id = "algebra-commutative/localization-ring"
title = "Localization of a ring"
kind = "knowl"
summary = "The ring S^{-1}R obtained from a ring R by inverting a multiplicative set S."
aliases = ["localization-ring", "Localization of a ring"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/localization-ring.md"
+++

Let $R$ be a [[algebra-rings/commutative-ring|commutative ring]] and let $S\subseteq R$ be a [[algebra-commutative/multiplicative-set|multiplicative set]]. The **localization of $R$ at $S$** is a ring, denoted $S^{-1}R$, together with a ring map
\[
\iota:R\longrightarrow S^{-1}R
\]
such that every element of $S$ becomes a unit in $S^{-1}R$ (see [[algebra-commutative/localization-inverts-multiplicative-set|localization inverts the multiplicative set]]).

### Construction (fractions)
As a set, $S^{-1}R$ can be constructed from pairs $(r,s)\in R\times S$ modulo the equivalence relation
\[
(r,s)\sim (r',s') \quad \Longleftrightarrow \quad \exists\,t\in S\text{ such that } t(rs'-r's)=0 \text{ in }R.
\]
Write the class of $(r,s)$ as $\frac{r}{s}$. Addition and multiplication are defined by
\[
\frac{r}{s}+\frac{r'}{s'}=\frac{rs'+r's}{ss'},\qquad
\frac{r}{s}\cdot\frac{r'}{s'}=\frac{rr'}{ss'}.
\]
The canonical map is $\iota(r)=\frac{r}{1}$.

If $0\in S$, then $\iota(0)$ is invertible, hence $1=0$ in $S^{-1}R$; in this case $S^{-1}R$ is the zero ring.

### Universal property
The localization is characterized by the following universal mapping property:

If $A$ is any commutative ring and $\varphi:R\to A$ is a ring homomorphism such that $\varphi(s)$ is a unit of $A$ for every $s\in S$, then there exists a unique ring homomorphism $\widetilde\varphi:S^{-1}R\to A$ with $\widetilde\varphi\circ\iota=\varphi$. Explicitly,
\[
\widetilde\varphi\!\left(\frac{r}{s}\right)=\varphi(r)\,\varphi(s)^{-1}.
\]

This same “invert $S$” idea for modules is treated in [[algebra-commutative/localization-module|localization of a module]], and it can be viewed as a special case of [[algebra-commutative/extension-of-scalars|extension of scalars]].

A basic structural fact is that primes of $S^{-1}R$ correspond to primes of $R$ disjoint from $S$; see [[algebra-commutative/localization-prime-correspondence|prime correspondence under localization]].

### Examples

1. **Inverting a prime number.** Take $R=\mathbb Z$ and $S=\{1,p,p^2,\dots\}$. Then
   \[
   S^{-1}\mathbb Z \cong \mathbb Z\!\left[\frac{1}{p}\right]
   =\left\{\frac{a}{p^n}:a\in\mathbb Z,\ n\ge 0\right\}\subseteq\mathbb Q.
   \]

2. **Laurent polynomials.** If $R=k[x]$ and $S=\{1,x,x^2,\dots\}$, then
   \[
   S^{-1}R \cong k[x,x^{-1}],
   \]
   since $x$ becomes invertible.

3. **Localizing at a prime ideal.** If $\mathfrak p\subset R$ is prime and $S=R\setminus\mathfrak p$, then $S^{-1}R$ is the [[algebra-commutative/localization-at-prime|localization at the prime]] $R_{\mathfrak p}$, which is a [[algebra-commutative/local-ring|local ring]].
