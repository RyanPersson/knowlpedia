---
title: "Noetherian ring"
description: "A ring in which ascending chains of ideals stabilize (equivalently, every ideal is finitely generated)."
---

Let $R$ be a {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}}.

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
- If $R$ is Noetherian and $S$ is a {{< knowl id="multiplicative-set" text="multiplicative set" >}}, then the localization $S^{-1}R$ is Noetherian; see {{< knowl id="localization-noetherian" text="localization preserves Noetherianity" >}}.
- If $R$ is Noetherian, then $R[x_1,\dots,x_n]$ is Noetherian (Hilbert basis theorem); a common formulation appears as {{< knowl id="hilbert-basis-corollary" text="Hilbert basis corollary" >}}.

Noetherian hypotheses are the natural setting for finiteness results such as {{< knowl id="primary-decomposition" text="primary decomposition" >}} via the {{< knowl id="lasker-noether-theorem" text="Lasker–Noether theorem" >}}.

## Examples
1. **Basic arithmetic and algebra.**  
   $\mathbb{Z}$ is Noetherian (every ideal is principal). If $k$ is a {{< knowl id="field" section="algebra-rings" text="field" >}}, then $k[x_1,\dots,x_n]$ is Noetherian.

2. **Quotients and finitely generated algebras.**  
   If $R$ is Noetherian, then so is $R/I$ for any ideal $I$, and so is any finitely generated $R$-algebra of the form $R[x_1,\dots,x_n]/J$.

3. **Localizations.**  
   $\mathbb{Z}_{(p)}$ (localization of $\mathbb{Z}$ at the prime $(p)$, i.e. inverting all integers not divisible by $p$) is Noetherian by {{< knowl id="localization-ring" text="localization" >}} and the permanence above.

## Non-example
- The polynomial ring in countably many variables $k[x_1,x_2,x_3,\dots]$ is not Noetherian: the chain of ideals
  \[
  (x_1) \subset (x_1,x_2) \subset (x_1,x_2,x_3) \subset \cdots
  \]
  never stabilizes.
