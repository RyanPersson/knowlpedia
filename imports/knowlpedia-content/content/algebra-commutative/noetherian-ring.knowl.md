+++
id = "algebra-commutative/noetherian-ring"
title = "Noetherian ring"
kind = "knowl"
summary = "A ring in which ascending chains of ideals stabilize (equivalently, every ideal is finitely generated)."
aliases = ["noetherian-ring", "Noetherian ring"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/noetherian-ring.md"
+++

Let $R$ be a [[algebra-rings/commutative-ring|commutative ring]].

$R$ is **Noetherian** if it satisfies the *ascending chain condition* (ACC) on ideals: for every chain
\[
I_1 \subseteq I_2 \subseteq I_3 \subseteq \cdots
\]
there exists $N$ such that $I_n=I_N$ for all $n\ge N$.

## Equivalent characterizations
The following are equivalent:
1. $R$ is Noetherian (ACC on ideals).
2. Every ideal of $R$ is finitely generated.
3. Every nonempty set of ideals of $R$ has a maximal element under inclusion.

The equivalence of (1) and (2) is the most used in practice.

## Standard permanence properties
- If $R$ is Noetherian and $I\subseteq R$ is an ideal, then $R/I$ is Noetherian.
- If $R$ is Noetherian and $S$ is a [[algebra-commutative/multiplicative-set|multiplicative set]], then the localization $S^{-1}R$ is Noetherian; see [[algebra-commutative/localization-noetherian|localization preserves Noetherianity]].
- If $R$ is Noetherian, then $R[x_1,\dots,x_n]$ is Noetherian (Hilbert basis theorem); a common formulation appears as [[algebra-commutative/hilbert-basis-corollary|Hilbert basis corollary]].

Noetherian hypotheses are the natural setting for finiteness results such as [[algebra-commutative/primary-decomposition|primary decomposition]] via the [[algebra-commutative/lasker-noether-theorem|Lasker–Noether theorem]].

## Examples
1. **Basic arithmetic and algebra.**
   $\mathbb{Z}$ is Noetherian (every ideal is principal). If $k$ is a [[algebra-rings/field|field]], then $k[x_1,\dots,x_n]$ is Noetherian.

2. **Quotients and finitely generated algebras.**
   If $R$ is Noetherian, then so is $R/I$ for any ideal $I$, and so is any finitely generated $R$-algebra of the form $R[x_1,\dots,x_n]/J$.

3. **Localizations.**
   $\mathbb{Z}_{(p)}$ (localization of $\mathbb{Z}$ at the prime $(p)$, i.e. inverting all integers not divisible by $p$) is Noetherian by [[algebra-commutative/localization-ring|localization]] and the permanence above.

## Non-example
- The polynomial ring in countably many variables $k[x_1,x_2,x_3,\dots]$ is not Noetherian: the chain of ideals
  \[
  (x_1) \subset (x_1,x_2) \subset (x_1,x_2,x_3) \subset \cdots
  \]
  never stabilizes.
