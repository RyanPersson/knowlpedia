---
title: "Prime avoidance lemma"
description: "If an ideal is contained in a finite union of prime ideals, then it is contained in one of them."
---

Let $R$ be a {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}}. The **prime avoidance lemma** is a basic tool for producing elements outside finitely many prime ideals (and is used constantly in arguments about {{< knowl id="prime-spectrum" text="Spec(R)" >}}, localizations, and dimension theory).

## Statement

Let $I,\mathfrak a_1,\dots,\mathfrak a_n$ be ideals of $R$. Assume that $\mathfrak a_2,\dots,\mathfrak a_n$ are prime ideals (no hypothesis on $\mathfrak a_1$). If
\[
I \subseteq \mathfrak a_1 \cup \mathfrak a_2 \cup \cdots \cup \mathfrak a_n,
\]
then $I \subseteq \mathfrak a_j$ for some $j\in\{1,\dots,n\}$.

A common special case (often the only one needed) is:

> If $\mathfrak p_1,\dots,\mathfrak p_n$ are prime ideals and
> \[
> I \subseteq \mathfrak p_1\cup\cdots\cup \mathfrak p_n,
> \]
> then $I\subseteq \mathfrak p_i$ for some $i$.

Equivalently (and often how it is used): if $I$ is an ideal **not** contained in any of the prime ideals $\mathfrak p_1,\dots,\mathfrak p_n$, then there exists an element $x\in I$ such that $x\notin \mathfrak p_1\cup\cdots\cup \mathfrak p_n$.

This “element-choosing” form underlies many constructions, for example when passing to a {{< knowl id="localization-ring" text="localization" >}} to avoid certain primes or when proving facts about basic open sets in {{< knowl id="zariski-topology" text="the Zariski topology" >}}.

## Examples

1. **In $\mathbb Z$.**  
   Take $R=\mathbb Z$, $I=(6)$, and $\mathfrak p_1=(2)$, $\mathfrak p_2=(3)$ (both prime ideals). Then
   \[
   (6)\subseteq (2)\cup(3)
   \]
   because every multiple of $6$ is divisible by $2$ (and also by $3$). Prime avoidance correctly concludes that $(6)\subseteq (2)$ or $(6)\subseteq (3)$ (in fact both hold).

2. **Choosing an element outside a finite union.**  
   In $R=k[x,y]$ over a field $k$, let $\mathfrak p_1=(x)$ and $\mathfrak p_2=(y)$, both prime. The ideal $I=(x,y)$ is **not** contained in $\mathfrak p_1$ and is **not** contained in $\mathfrak p_2$. Prime avoidance therefore guarantees an element of $I$ outside $\mathfrak p_1\cup\mathfrak p_2$; concretely, $x+y\in (x,y)$ but $x+y\notin (x)$ and $x+y\notin (y)$.

3. **Why finiteness matters (failure for infinite unions).**  
   Let $R=k[x_1,x_2,\dots]$ be a polynomial ring in infinitely many variables over a field $k$, and let
   \[
   I=(x_1,x_2,\dots).
   \]
   For each $n$, the ideal $\mathfrak p_n=(x_1,\dots,x_n)$ is prime. Every element of $I$ involves only finitely many variables, so it belongs to $\mathfrak p_n$ for some $n$, hence
   \[
   I \subseteq \bigcup_{n\ge 1}\mathfrak p_n.
   \]
   But $I$ is not contained in any single $\mathfrak p_n$ (since $x_{n+1}\in I$ but $x_{n+1}\notin \mathfrak p_n$). This shows the lemma is genuinely a **finite**-union phenomenon.
