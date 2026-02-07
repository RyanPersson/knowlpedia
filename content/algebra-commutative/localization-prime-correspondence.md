---
title: "Prime correspondence under localization"
description: "Prime ideals in a localization S^{-1}R correspond to primes of R disjoint from S via extension and contraction."
---

Let $R$ be a {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}} and let $S\subseteq R$ be a {{< knowl id="multiplicative-set" text="multiplicative set" >}}. Write $S^{-1}R$ for the {{< knowl id="localization-ring" text="localization" >}}.

## Theorem (prime correspondence)
The map
\[
\mathfrak p \longmapsto S^{-1}\mathfrak p
\]
induces an inclusion-preserving bijection between:
- prime ideals $\mathfrak p\subseteq R$ with $\mathfrak p\cap S=\varnothing$, and
- prime ideals $\mathfrak q\subseteq S^{-1}R$.

The inverse bijection is **contraction**:
\[
\mathfrak q \longmapsto \mathfrak q^c := \{\, r\in R : r/1 \in \mathfrak q \,\}.
\]

In other words, “primes survive localization exactly when they do not meet the set of denominators.” This refines the fact that localization {{< knowl id="localization-preserves-primality" text="preserves primality" >}}.

### Geometric form
On the {{< knowl id="prime-spectrum" text="prime spectrum" >}}, this correspondence identifies $\operatorname{Spec}(S^{-1}R)$ with the open subset
\[
\{\,\mathfrak p\in \operatorname{Spec}(R) : \mathfrak p\cap S=\varnothing\,\}
\]
for the {{< knowl id="zariski-topology" text="Zariski topology" >}}. For $S=\{1,f,f^2,\dots\}$, this is the basic open set $D(f)$.

### Special case: localization at a prime
If $S=R\setminus \mathfrak p$ for a prime ideal $\mathfrak p$, then $S^{-1}R$ is the ring {{< knowl id="localization-at-prime" text="$R_\mathfrak p$" >}}. The primes of $R_\mathfrak p$ correspond exactly to primes $\mathfrak q\subseteq R$ with $\mathfrak q\subseteq \mathfrak p$.

## Examples
1. **Inverting a prime in $\mathbb{Z}$.**  
   Take $R=\mathbb{Z}$ and $S=\{1,p,p^2,\dots\}$. Then $S^{-1}R=\mathbb{Z}[1/p]$. A prime ideal of $\mathbb{Z}$ meets $S$ iff it contains $p$, so the primes of $\mathbb{Z}[1/p]$ correspond to $(0)$ and $(\ell)$ for primes $\ell\neq p$.

2. **Localizing away from a hypersurface.**  
   Let $R=k[x,y]$ and $S=\{1,x,x^2,\dots\}$, so $S^{-1}R=R_x$. Primes of $R_x$ correspond to primes of $k[x,y]$ that do **not** contain $x$. For instance, $(y)$ survives (since $x\notin(y)$), while $(x,y)$ does not survive (since it contains $x$).

3. **Localization at a maximal ideal.**  
   In $R=k[x,y]$, localize at $\mathfrak m=(x,y)$ to get {{< knowl id="localization-at-prime" text="$R_\mathfrak m$" >}}. The primes of $R_\mathfrak m$ correspond to primes contained in $(x,y)$, namely $(0)$, $(x)$, $(y)$, and $(x,y)$.
