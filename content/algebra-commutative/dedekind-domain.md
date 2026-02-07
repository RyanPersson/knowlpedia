---
title: "Dedekind domain"
description: "A Noetherian, integrally closed domain of Krull dimension one; equivalently, a domain with unique factorization of ideals into primes."
---

A **Dedekind domain** is a central object in commutative algebra and algebraic number theory.

An integral domain $R$ is a **Dedekind domain** if:
1. $R$ is a {{< knowl id="noetherian-ring" text="Noetherian ring" >}};
2. $R$ is an {{< knowl id="integrally-closed-domain" text="integrally closed domain" >}};
3. $R$ has {{< knowl id="krull-dimension" text="Krull dimension" >}} $1$ (equivalently, every nonzero prime ideal has {{< knowl id="height-of-prime" text="height" >}} $1$, hence is maximal).

Condition (3) can be read as: “the only prime ideals properly contained in a nonzero prime are $(0)$.”

## Equivalent and characteristic properties
For a domain $R$, the following are standard characterizations of Dedekind domains:
- Every nonzero proper ideal factors as a product of prime ideals, and this factorization is unique up to ordering.
- For every nonzero prime ideal $\mathfrak p$, the localization $R_\mathfrak p$ (see {{< knowl id="localization-at-prime" text="localization at a prime" >}}) is a {{< knowl id="dvr" text="discrete valuation ring" >}}. In fact, this local DVR structure controls the prime-power factorization of ideals.

## Examples
1. **The integers.**  
   $\mathbb{Z}$ is a Dedekind domain: it is Noetherian, integrally closed in $\mathbb{Q}$, and has dimension $1$. (More generally, any PID that is not a field is Dedekind; for instance, any {{< knowl id="euclidean-domain" section="algebra-rings" text="Euclidean domain" >}} is a PID by {{< knowl id="euclidean-implies-pid" section="algebra-rings" text="Euclidean ⇒ PID" >}} and hence Dedekind.)

2. **A principal ideal domain of dimension one.**  
   For a field $k$, the polynomial ring $k[t]$ is a PID, hence Dedekind.

3. **Rings of integers in number fields.**  
   If $K/\mathbb{Q}$ is a number field and $\mathcal O_K$ is its ring of integers, then $\mathcal O_K$ is a Dedekind domain (a key reason prime ideal factorization replaces unique factorization of elements).

## Non-example
- $k[x,y]$ (two variables over a field $k$) is Noetherian and integrally closed, but it has Krull dimension $2$, so it is not Dedekind.
