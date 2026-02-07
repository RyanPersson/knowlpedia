---
title: "Primary decomposition"
description: "Expressing an ideal as an intersection of primary ideals, with existence guaranteed in Noetherian rings."
---

Let $R$ be a {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}} and let $I\subseteq R$ be an ideal.

## Definition (primary ideal)
An ideal $Q\subsetneq R$ is **primary** if for all $a,b\in R$,
\[
ab\in Q \;\Rightarrow\; \bigl(a\in Q \text{ or } b^n\in Q \text{ for some } n\ge 1\bigr).
\]
Equivalently, $Q$ is primary if $R/Q$ has the property that every zero-divisor is nilpotent.

If $Q$ is primary, then its radical $\sqrt{Q}$ is a prime ideal; one often says that $Q$ is **$\mathfrak p$-primary** when $\sqrt{Q}=\mathfrak p$.

## Definition (primary decomposition)
A **primary decomposition** of $I$ is an expression
\[
I = Q_1\cap \cdots \cap Q_r
\]
where each $Q_i$ is a primary ideal of $R$.

A primary decomposition is called *minimal* if (i) the radicals $\sqrt{Q_i}$ are pairwise distinct and (ii) no $Q_i$ can be omitted without changing the intersection. The primes $\sqrt{Q_i}$ that occur in a minimal decomposition are intrinsic invariants (the “associated primes” of $I$), even though the $Q_i$ themselves need not be unique.

## Existence in Noetherian rings
Primary decompositions do not exist in arbitrary rings. The fundamental existence theorem is the {{< knowl id="lasker-noether-theorem" text="Lasker–Noether theorem" >}}, often packaged as {{< knowl id="noetherian-primary-decomposition" text="primary decomposition in Noetherian rings" >}}: if $R$ is a {{< knowl id="noetherian-ring" text="Noetherian ring" >}}, then every ideal $I\subseteq R$ admits a primary decomposition.

## Examples
1. **In $\mathbb{Z}$.**  
   In the PID $\mathbb{Z}$, primary ideals are exactly $(p^n)$ for primes $p$. Using $(a)\cap(b)=(\mathrm{lcm}(a,b))$, one gets
   \[
   (12) = (4)\cap(3),
   \]
   where $(4)$ is $(2)$-primary and $(3)$ is $(3)$-primary.

2. **A squarefree monomial ideal.**  
   Over a field $k$, in $k[x,y]$ one has
   \[
   (xy) = (x)\cap(y).
   \]
   Here $(x)$ and $(y)$ are prime (hence primary), so this is a primary decomposition.

3. **A “one-piece” primary decomposition.**  
   In $k[x,y]$, the ideal $Q=(x,y)^2=(x^2,xy,y^2)$ is $(x,y)$-primary. Thus it is already a primary decomposition of itself:
   \[
   (x,y)^2 = Q.
   \]
