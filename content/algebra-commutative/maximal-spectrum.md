---
title: "Maximal spectrum"
description: "The set MaxSpec(R) of maximal ideals of a commutative ring, with the induced Zariski topology."
---

Let $R$ be a {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}}. A **maximal ideal** of $R$ is a proper ideal $\mathfrak m\subsetneq R$ such that there is no ideal strictly between $\mathfrak m$ and $R$; equivalently, $R/\mathfrak m$ is a {{< knowl id="field" section="algebra-rings" text="field" >}}.

The **maximal spectrum** of $R$ is the set
\[
\operatorname{MaxSpec}(R) := \{\mathfrak m \subset R \mid \mathfrak m \text{ is a maximal ideal}\}.
\]

There is always an inclusion $\operatorname{MaxSpec}(R)\subseteq \operatorname{Spec}(R)$ (see {{< knowl id="prime-spectrum" text="prime spectrum" >}}), since every maximal ideal is prime. One typically topologizes $\operatorname{MaxSpec}(R)$ by the subspace topology induced from the {{< knowl id="zariski-topology" text="Zariski topology on \operatorname{Spec}(R)" >}}. Concretely, for an ideal $I\subseteq R$ the corresponding closed subset of $\operatorname{MaxSpec}(R)$ is
\[
V(I)\cap \operatorname{MaxSpec}(R)=\{\mathfrak m\in \operatorname{MaxSpec}(R)\mid I\subseteq \mathfrak m\}.
\]

A point $\mathfrak m\in \operatorname{MaxSpec}(R)$ has residue field $R/\mathfrak m$, which agrees with the {{< knowl id="residue-field" text="residue field" >}} at $\mathfrak m$.

### Examples

1. **Local rings.**  
   If $R$ is a {{< knowl id="local-ring" text="local ring" >}}, it has a unique maximal ideal (see {{< knowl id="maximal-ideal-local-ring" text="the characterization of local rings by a unique maximal ideal" >}}), hence $\operatorname{MaxSpec}(R)$ is a single point.

2. **The integers.**  
   For $R=\mathbb{Z}$, the maximal ideals are exactly $(p)$ for primes $p$. Thus
   \[
   \operatorname{MaxSpec}(\mathbb{Z})=\{(p)\mid p\ \text{prime}\},
   \]
   which is $\operatorname{Spec}(\mathbb{Z})$ with the generic point $(0)$ removed.

3. **Polynomial rings over an algebraically closed field.**  
   If $k$ is algebraically closed and $R=k[x_1,\dots,x_n]$, then the {{< knowl id="nullstellensatz-variety-correspondence" text="Nullstellensatz" >}} identifies maximal ideals with points $a=(a_1,\dots,a_n)\in k^n$ via
   \[
   a \longleftrightarrow (x_1-a_1,\dots,x_n-a_n).
   \]
   In this sense, $\operatorname{MaxSpec}(k[x_1,\dots,x_n])$ recovers affine $n$-space over $k$ as a set, and its induced topology is the classical Zariski topology on $k^n$.
