+++
id = "algebra-commutative/jacobson-radical-intersection-maximals"
title = "Jacobson radical as intersection of maximal ideals"
kind = "knowl"
summary = "In a commutative ring, the Jacobson radical equals the intersection of all maximal ideals."
aliases = ["jacobson-radical-intersection-maximals", "Jacobson radical as intersection of maximal ideals"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/jacobson-radical-intersection-maximals.md"
+++

The Jacobson radical measures how far a ring is from being “seen” by its simple quotients. In commutative algebra it has a concrete description in terms of maximal ideals, and it interacts cleanly with [[algebra-commutative/local-ring|local rings]] and residue fields.

## Statement

Let $R$ be a [[algebra-rings/commutative-ring|commutative ring]]. The **Jacobson radical** of $R$, denoted $J(R)$, satisfies
\[
J(R)=\bigcap_{\mathfrak m\in\operatorname{MaxSpec}(R)} \mathfrak m,
\]
the intersection of all maximal ideals of $R$. Here [[algebra-commutative/maximal-spectrum|MaxSpec(R)]] denotes the set of maximal ideals.

Equivalently, an element $r\in R$ lies in $J(R)$ if and only if its image in every residue field [[algebra-commutative/residue-field|$R/\mathfrak m$]] is zero (i.e. $r\in\mathfrak m$ for every maximal ideal $\mathfrak m$).

A particularly important consequence is: if $R$ is a [[algebra-commutative/local-ring|local ring]] with maximal ideal $\mathfrak m$ (see [[algebra-commutative/maximal-ideal-local-ring|the characterization of local rings by a unique maximal ideal]]), then
\[
J(R)=\mathfrak m.
\]

This description is compatible with the module-theoretic viewpoint: compare [[algebra-commutative/jacobson-annihilates-simples|Jacobson radical annihilates simples]].

## Examples

1. **The integers.**
   In $R=\mathbb Z$, maximal ideals are precisely $(p)$ for primes $p$. Their intersection is $(0)$, so $J(\mathbb Z)=0$.

2. **A local example from localization.**
   Let $R=\mathbb Z_{(p)}$ be the [[algebra-commutative/localization-at-prime|localization of $\mathbb Z$ at the prime $(p)$]]. This is a [[algebra-commutative/local-ring|local ring]] whose unique maximal ideal is $p\mathbb Z_{(p)}$, hence
   \[
   J(\mathbb Z_{(p)}) = p\mathbb Z_{(p)}.
   \]

3. **Dual numbers.**
   Let $R=k[\varepsilon]/(\varepsilon^2)$ for a field $k$. The ideal $(\bar\varepsilon)$ is maximal (indeed $R/(\bar\varepsilon)\cong k$ is a field), and it is the unique maximal ideal. Therefore $J(R)=(\bar\varepsilon)$. In particular, $\bar\varepsilon$ lies in every maximal ideal, so it lies in the intersection.

These examples illustrate the philosophy: $J(R)$ consists of the elements that vanish in every residue field (and, in a local ring, precisely the nonunits).
