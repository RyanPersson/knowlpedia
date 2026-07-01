+++
id = "algebra-commutative/lasker-noether-theorem"
title = "Lasker–Noether theorem"
kind = "knowl"
summary = "Every ideal in a Noetherian ring can be written as a finite intersection of primary ideals."
aliases = ["lasker-noether-theorem", "Lasker–Noether theorem"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/lasker-noether-theorem.md"
+++

In a [[algebra-rings/commutative-ring|commutative ring]] $A$, an ideal $Q$ is *primary* if $ab\in Q$ implies $a\in Q$ or $b^n\in Q$ for some $n\ge 1$; equivalently, the zero-divisors in $A/Q$ are nilpotent. If $Q$ is primary and $\sqrt{Q}=\mathfrak p$ is prime, then $Q$ is called $\mathfrak p$-*primary*. A representation of an ideal as an intersection of primary ideals is a [[algebra-commutative/primary-decomposition|primary decomposition]].

**Theorem (Lasker–Noether).**
Let $A$ be a [[algebra-commutative/noetherian-ring|Noetherian ring]] and let $I\subseteq A$ be an ideal. Then there exist finitely many primary ideals $Q_1,\dots,Q_r\subseteq A$ such that
\[
I=\bigcap_{i=1}^r Q_i.
\]
Moreover, one can choose the decomposition so that the radicals $\mathfrak p_i=\sqrt{Q_i}$ are distinct prime ideals; in such a *minimal* primary decomposition, the set of primes $\{\mathfrak p_i\}$ is uniquely determined by $I$ (it is the set of prime ideals minimal over $I$).

Via the [[algebra-commutative/zariski-topology|Zariski topology]] on the [[algebra-commutative/prime-spectrum|prime spectrum]] $\operatorname{Spec}(A)$, the identity $I=\bigcap Q_i$ translates to the geometric union
\[
V(I)=\bigcup_{i=1}^r V(Q_i),
\]
so primary decomposition packages the "irreducible pieces" of $V(I)$.

### Examples
1. **Integers: prime-power pieces.**
   In $A=\mathbb Z$, every ideal is principal. For $I=(12)$ one has
   \[
   (12)=(4)\cap (3).
   \]
   Here $(4)$ is $(2)$-primary and $(3)$ is $(3)$-primary.

2. **A union of coordinate axes.**
   In $A=k[x,y]$ (with $k$ a [[algebra-rings/field|field]]), the ideal $I=(xy)$ decomposes as
   \[
   (xy)=(x)\cap (y).
   \]
   Both $(x)$ and $(y)$ are prime (hence primary), corresponding to the two axes in $V(xy)$.

3. **A primary component with embedded nilpotents.**
   In $A=k[x,y]$, the ideal $I=(x^2,xy)$ admits the decomposition
   \[
   (x^2,xy)=(x)\cap (x^2,y).
   \]
   The ideal $(x)$ is prime, while $(x^2,y)$ is $(x,y)$-primary since its radical is $(x,y)$ and $x$ becomes nilpotent modulo $(x^2,y)$.
