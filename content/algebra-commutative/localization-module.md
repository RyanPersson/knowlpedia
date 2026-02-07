---
title: "Localization of a module"
description: "Given S⊂R multiplicative, the module S^{-1}M obtained by inverting S in an R-module M."
---

Let $R$ be a {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}}, let $S\subseteq R$ be a {{< knowl id="multiplicative-set" text="multiplicative set" >}}, and let $M$ be an $R$-module. The **localization of $M$ at $S$** is an $S^{-1}R$-module, denoted $S^{-1}M$, constructed so that every $s\in S$ acts invertibly on $S^{-1}M$.

Here $S^{-1}R$ is the {{< knowl id="localization-ring" text="localized ring" >}}.

### Construction (fractions in a module)
Define $S^{-1}M$ as equivalence classes of pairs $(m,s)\in M\times S$ under
\[
(m,s)\sim (m',s') \quad \Longleftrightarrow \quad \exists\,t\in S \text{ such that } t(s'm-sm')=0 \text{ in }M.
\]
Write the class of $(m,s)$ as $\frac{m}{s}$. Addition is
\[
\frac{m}{s}+\frac{m'}{s'}=\frac{s'm+sm'}{ss'},
\]
and the scalar action of $S^{-1}R$ is given by
\[
\left(\frac{r}{s}\right)\!\left(\frac{m}{t}\right)=\frac{rm}{st}.
\]

The map $\iota_M:M\to S^{-1}M$ given by $\iota_M(m)=\frac{m}{1}$ is $R$-linear.

### Universal property
Let $N$ be an $S^{-1}R$-module. Viewing $N$ as an $R$-module via the canonical map $R\to S^{-1}R$, every $s\in S$ acts by an automorphism on $N$. The localization $S^{-1}M$ is characterized by:

For every $R$-linear map $f:M\to N$, there exists a unique $S^{-1}R$-linear map $\widetilde f:S^{-1}M\to N$ with $\widetilde f\circ\iota_M=f$.

In particular, localizing at a prime $\mathfrak p$ means taking $S=R\setminus\mathfrak p$ and writing
\[
M_{\mathfrak p}:=(R\setminus\mathfrak p)^{-1}M,
\]
in parallel with {{< knowl id="localization-at-prime" text="localization of rings at a prime" >}}.

Localization interacts well with exact sequences: it is an exact functor on modules (see {{< knowl id="localization-exact" text="exactness of localization" >}} and compare with the general notion of an {{< knowl id="exact-sequence-modules" section="algebra-modules" text="exact sequence" >}}).

Finally, localization can be expressed as a base change: via {{< knowl id="extension-of-scalars" text="extension of scalars" >}} there is a natural isomorphism
\[
S^{-1}M \cong (S^{-1}R)\otimes_R M.
\]

### Examples

1. **Localizing a quotient.** If $I\subseteq R$ is an ideal, then
   \[
   S^{-1}(R/I)\ \cong\ (S^{-1}R)/(S^{-1}I),
   \]
   where $S^{-1}I$ denotes the image of $I$ in $S^{-1}R$.

2. **Torsion killed by localization.** Take $R=\mathbb Z$, $M=\mathbb Z/n\mathbb Z$, and localize at $S=\mathbb Z\setminus (p)$ (so $S^{-1}\mathbb Z=\mathbb Z_{(p)}$).
   - If $p\nmid n$, then $n\in S$ becomes a unit, so $S^{-1}M=0$.
   - If $p\mid n$, then $S^{-1}M\cong \mathbb Z_{(p)}/n\mathbb Z_{(p)}$, which is generally nonzero.

3. **Making an element invertible forces a module to vanish.** Let $R=k[x]$, $M=R/(x)$, and $S=\{1,x,x^2,\dots\}$. In $S^{-1}R$ the element $x$ is a unit, but $x$ annihilates $M$, so $S^{-1}M=0$.
