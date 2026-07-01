+++
id = "algebra-commutative/multiplicative-set"
title = "Multiplicative set"
kind = "knowl"
summary = "A subset of a ring closed under multiplication and containing 1, used to form localizations."
aliases = ["multiplicative-set", "Multiplicative set"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/multiplicative-set.md"
+++

Let $R$ be a [[algebra-rings/commutative-ring|commutative ring]]. A subset $S\subseteq R$ is a **multiplicative set** if

1. $1\in S$, and
2. whenever $s,t\in S$, then $st\in S$.

Often one also assumes $0\notin S$ when the goal is to form the [[algebra-commutative/localization-ring|localization of a ring]] $S^{-1}R$; if $0\in S$, then $0$ becomes invertible in $S^{-1}R$, forcing $1=0$ and hence $S^{-1}R$ is the zero ring.

A key source of multiplicative sets is complements of primes: if $\mathfrak p\subset R$ is prime, then $R\setminus \mathfrak p$ is multiplicative, and this choice produces the [[algebra-commutative/localization-at-prime|localization at a prime]].

### Examples

1. **Powers of an element.** For $f\in R$, the set
   \[
   S=\{1,f,f^2,f^3,\dots\}
   \]
   is multiplicative. (If $f$ is nilpotent, then $0\in S$ and the corresponding localization collapses to the zero ring.)

2. **Complement of a prime ideal.** If $\mathfrak p$ is a prime ideal of $R$, then
   \[
   S=R\setminus \mathfrak p
   \]
   is multiplicative (primality ensures $st\notin\mathfrak p$ whenever $s,t\notin\mathfrak p$). Localizing at this $S$ gives $R_{\mathfrak p}$.

3. **Inverting a prime number in $\mathbb Z$.** In $R=\mathbb Z$, the subset $S=\{1,p,p^2,\dots\}$ (for a prime $p$) is multiplicative. The localization $S^{-1}\mathbb Z$ is the subring of $\mathbb Q$ consisting of fractions whose denominator is a power of $p$.
