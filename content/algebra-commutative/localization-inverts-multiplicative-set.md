---
title: "Localization inverts a multiplicative set"
description: "In the localization S^{-1}R, every element of S becomes a unit, and S^{-1}R is universal with that property."
---

Let $R$ be a {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}} and let $S\subseteq R$ be a {{< knowl id="multiplicative-set" text="multiplicative set" >}}. The {{< knowl id="localization-ring" text="localization" >}} $S^{-1}R$ comes with a canonical ring homomorphism
\[
\iota:R\to S^{-1}R,\qquad r\mapsto \frac{r}{1}.
\]

**Theorem (Elements of $S$ become units).**  
For every $s\in S$, the element $\iota(s)=s/1$ is a unit in $S^{-1}R$, with inverse $1/s$. In particular, every fraction can be rewritten as
\[
\frac{r}{s}=\iota(r)\,\iota(s)^{-1}.
\]

**Universal property (often used as the definition).**  
If $T$ is any {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}} and $\varphi:R\to T$ is a homomorphism such that every $\varphi(s)$ (for $s\in S$) is a unit of $T$, then there exists a unique homomorphism $\psi:S^{-1}R\to T$ with $\psi\circ \iota=\varphi$. Concretely, $\psi$ is forced to satisfy $\psi(r/s)=\varphi(r)\varphi(s)^{-1}$.

This perspective explains why {{< knowl id="localization-at-prime" text="localizing at a prime" >}} produces a {{< knowl id="local-ring" text="local ring" >}}: inverting all elements outside a prime ideal forces exactly those elements to become units.

### Examples
1. **Inverting a single integer.**  
   Take $R=\mathbb Z$ and $S=\{1,2,2^2,2^3,\dots\}$. Then $S^{-1}R\cong \mathbb Z[1/2]$, and $2$ becomes a unit with inverse $1/2$.

2. **Laurent polynomials by inverting a variable.**  
   Take $R=k[x]$ and $S=\{1,x,x^2,\dots\}$. Then $S^{-1}R\cong k[x,x^{-1}]$, and $x$ becomes a unit. Every element looks like a Laurent polynomial because denominators are powers of $x$.

3. **Localizing at a prime ideal.**  
   If $\mathfrak p$ is a prime ideal of $R$, set $S=R\setminus \mathfrak p$. Then the localization $S^{-1}R$ is the {{< knowl id="localization-at-prime" text="localization $R_{\mathfrak p}$" >}}, where every element not in $\mathfrak p$ becomes invertible; this is the basic way to construct a {{< knowl id="local-ring" text="local ring" >}} from $R$.
