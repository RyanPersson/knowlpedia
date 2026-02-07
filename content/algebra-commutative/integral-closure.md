---
title: "Integral closure"
description: "The subring of an overring consisting of all elements integral over a given ring."
---

Let $R$ be a {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}}, and let $A$ be a commutative $R$-algebra (equivalently, a ring equipped with a homomorphism $R\to A$).

An element $a\in A$ is called an {{< knowl id="integral-element" text="integral element" >}} over $R$ if there exists a monic polynomial
\[
a^n + r_{n-1}a^{n-1}+\cdots + r_1 a + r_0 = 0 \quad \text{with } r_i\in R.
\]

## Definition (integral closure in an algebra)
The **integral closure of $R$ in $A$** is the subset
\[
\overline{R}^{\,A} \;=\; \{\, a\in A : a \text{ is integral over } R \,\}.
\]
It is a subring of $A$ containing the image of $R$.

When $R$ is a domain with fraction field $K$, the integral closure of $R$ **in $K$** is often called the *normalization* of $R$. The domain $R$ is {{< knowl id="integrally-closed-domain" text="integrally closed" >}} precisely when its integral closure in its fraction field equals $R$.

## Basic properties
- If $R\subseteq A$ is an {{< knowl id="integral-extension" text="integral extension" >}}, then every element of $A$ is integral over $R$, hence $\overline{R}^{\,A}=A$.
- If $B\subseteq A$ is any subring containing $R$ and consisting of elements integral over $R$, then $B\subseteq \overline{R}^{\,A}$ (maximality of the integral closure).

## Examples
1. **Integers inside rationals.**  
   Take $R=\mathbb{Z}$ and $A=\mathbb{Q}$. If $a/b\in \mathbb{Q}$ (in lowest terms) is integral over $\mathbb{Z}$, then it satisfies a monic polynomial with integer coefficients, forcing $b=\pm 1$. Hence $\overline{\mathbb{Z}}^{\,\mathbb{Q}}=\mathbb{Z}$.

2. **A non-normal affine subring.**  
   Let $k$ be a {{< knowl id="field" section="algebra-rings" text="field" >}} and consider $R=k[x^2,x^3]\subseteq A=k(x)$ (the rational function field in $x$). The element $x\in k(x)$ satisfies the monic equation $T^2-x^2=0$ with $x^2\in R$, so $x$ is integral over $R$. Thus the integral closure contains $k[x]$. In fact one checks $\overline{R}^{\,k(x)}=k[x]$.

3. **Localizing does not change “integrality in the fraction field.”**  
   If $R$ is a domain and $S$ is a {{< knowl id="multiplicative-set" text="multiplicative set" >}} of nonzero elements, then $S^{-1}R$ sits in the same fraction field as $R$. Elements of the fraction field integral over $S^{-1}R$ are exactly those integral over $R$ after clearing denominators, so integral closure interacts naturally with {{< knowl id="localization-ring" text="localization" >}}.
