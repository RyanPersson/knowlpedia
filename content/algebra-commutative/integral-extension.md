---
title: "Integral extension"
description: "A ring extension A→B is integral if every element of B is integral over A."
---

Let $A\to B$ be a homomorphism of {{< knowl id="commutative-ring" section="algebra-rings" text="commutative rings" >}}. The map (or the extension) is called **integral** if every element $b\in B$ is {{< knowl id="integral-element" text="integral over A" >}}; equivalently, for each $b\in B$ there is a monic polynomial in $A[T]$ having $b$ as a root.

A frequently used sufficient condition is:

**Finite algebra implies integral.**  
If $B$ is finitely generated as an $A$-module, then $A\to B$ is integral.

Integral extensions behave well with localization: localizing an integral extension at any multiplicative set preserves integrality (compare {{< knowl id="localization-ring" text="localization" >}}). They also satisfy strong prime ideal behavior, formalized by results such as {{< knowl id="lying-over-theorem" text="lying over" >}} and {{< knowl id="going-up-theorem" text="going up" >}}.

### Examples

1. **Adjoining a root of a monic polynomial.**  
   For any ring $A$ and monic $f(T)\in A[T]$, the quotient
   \[
   B := A[T]/(f)
   \]
   is integral over $A$: the class of $T$ in $B$ satisfies the monic equation $f(T)=0$.

2. **Classical quadratic extensions.**  
   The inclusion $\mathbb{Z}\subseteq \mathbb{Z}[i]$ is integral since $i$ satisfies $T^2+1=0$ over $\mathbb{Z}$, and every element of $\mathbb{Z}[i]$ is a polynomial in $i$ with integer coefficients.

3. **A cusp subring inside a polynomial ring.**  
   Let $k$ be a field, $A=k[x^2,x^3]\subseteq B=k[x]$. Then $B$ is integral over $A$ because $x\in B$ satisfies the monic equation $T^2-x^2=0$ with $x^2\in A$, and hence every polynomial in $x$ is integral over $A$.

4. **Non-example: polynomial extensions are not integral.**  
   The inclusion $A\subseteq A[x]$ is typically not integral: the element $x$ does not satisfy any monic polynomial with coefficients in $A$.
