+++
id = "algebra-commutative/maximal-spectrum"
title = "Maximal spectrum"
kind = "knowl"
summary = "The set MaxSpec(R) of maximal ideals of a commutative ring, with the induced Zariski topology."
aliases = ["maximal-spectrum", "Maximal spectrum"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/maximal-spectrum.md"
+++

Let $R$ be a [[algebra-rings/commutative-ring|commutative ring]]. A **maximal ideal** of $R$ is a proper ideal $\mathfrak m\subsetneq R$ such that there is no ideal strictly between $\mathfrak m$ and $R$; equivalently, $R/\mathfrak m$ is a [[algebra-rings/field|field]].

The **maximal spectrum** of $R$ is the set
\[
\operatorname{MaxSpec}(R) := \{\mathfrak m \subset R \mid \mathfrak m \text{ is a maximal ideal}\}.
\]

There is always an inclusion $\operatorname{MaxSpec}(R)\subseteq \operatorname{Spec}(R)$ (see [[algebra-commutative/prime-spectrum|prime spectrum]]), since every maximal ideal is prime. One typically topologizes $\operatorname{MaxSpec}(R)$ by the subspace topology induced from the [[algebra-commutative/zariski-topology|Zariski topology on \operatorname{Spec}(R)]]. Concretely, for an ideal $I\subseteq R$ the corresponding closed subset of $\operatorname{MaxSpec}(R)$ is
\[
V(I)\cap \operatorname{MaxSpec}(R)=\{\mathfrak m\in \operatorname{MaxSpec}(R)\mid I\subseteq \mathfrak m\}.
\]

A point $\mathfrak m\in \operatorname{MaxSpec}(R)$ has residue field $R/\mathfrak m$, which agrees with the [[algebra-commutative/residue-field|residue field]] at $\mathfrak m$.

### Examples

1. **Local rings.**
   If $R$ is a [[algebra-commutative/local-ring|local ring]], it has a unique maximal ideal (see [[algebra-commutative/maximal-ideal-local-ring|the characterization of local rings by a unique maximal ideal]]), hence $\operatorname{MaxSpec}(R)$ is a single point.

2. **The integers.**
   For $R=\mathbb{Z}$, the maximal ideals are exactly $(p)$ for primes $p$. Thus
   \[
   \operatorname{MaxSpec}(\mathbb{Z})=\{(p)\mid p\ \text{prime}\},
   \]
   which is $\operatorname{Spec}(\mathbb{Z})$ with the generic point $(0)$ removed.

3. **Polynomial rings over an algebraically closed field.**
   If $k$ is algebraically closed and $R=k[x_1,\dots,x_n]$, then the [[algebra-commutative/nullstellensatz-variety-correspondence|Nullstellensatz]] identifies maximal ideals with points $a=(a_1,\dots,a_n)\in k^n$ via
   \[
   a \longleftrightarrow (x_1-a_1,\dots,x_n-a_n).
   \]
   In this sense, $\operatorname{MaxSpec}(k[x_1,\dots,x_n])$ recovers affine $n$-space over $k$ as a set, and its induced topology is the classical Zariski topology on $k^n$.
