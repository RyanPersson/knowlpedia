---
title: "Equivalence of cocycles"
description: "Two transition function cocycles are equivalent if they differ by a change of local trivializations"
---

Let $M$ be a smooth manifold and let $\{U_i\}$ be an open cover. A $G$-valued cocycle on this cover is a collection of smooth maps $g_{ij}:U_i\cap U_j\to G$ satisfying the {{< knowl id="cocycle-condition-for-transition-functions" text="cocycle condition" >}}
\[
g_{ij}\,g_{jk}=g_{ik}\quad\text{on }U_i\cap U_j\cap U_k,
\qquad
g_{ii}=e,\quad g_{ji}=g_{ij}^{-1}.
\]
Such data defines a principal bundle by gluing trivial bundles, producing the usual notion of {{< knowl id="principal-bundle-transition-function" text="transition functions" >}} and a corresponding {{< knowl id="bundle-atlas" text="bundle atlas" >}}.

## Definition (equivalent cocycles)
Two cocycles $\{g_{ij}\}$ and $\{g'_{ij}\}$ on the same cover are **equivalent** if there exist smooth maps
\[
h_i:U_i\to G
\]
such that on each overlap $U_i\cap U_j$,
\[
g'_{ij}=h_i^{-1}\,g_{ij}\,h_j.
\]

Equivalently, if $\{g_{ij}\}$ arises from local sections $s_i:U_i\to P$ via $s_j=s_i\,g_{ij}$ (as in {{< knowl id="construction-transition-functions-g-iju-iu-jg-from-local-sections" text="transition functions from local sections" >}}), then replacing the sections by
\[
s'_i:=s_i\,h_i
\]
changes the transition functions to $g'_{ij}=h_i^{-1}g_{ij}h_j$. Thus, equivalence of cocycles is precisely “the same gluing data after a change of local trivializations.”

Equivalent cocycles define isomorphic principal bundles; the corresponding isomorphism is a {{< knowl id="principal-bundle-isomorphism" text="principal bundle isomorphism" >}} and, from the atlas perspective, this is the same relation as {{< knowl id="equivalent-bundle-atlases" text="equivalence of bundle atlases" >}}.

## Examples
1. **Trivial cocycle and coboundaries.**  
   The trivial bundle $M\times G$ has cocycle $g_{ij}=e$. A cocycle $\{g_{ij}\}$ is equivalent to the trivial cocycle exactly when there exist $h_i$ with
   \[
   g_{ij}=h_i\,h_j^{-1}.
   \]
   This is the transition-function version of the {{< knowl id="trivial-principal-bundle-criterion-global-section-principal-bundle-is-trivial" text="global section criterion for triviality" >}}.

2. **Changing local sections on a trivial bundle.**  
   On $P=M\times G$, start with the canonical local sections $s_i(x)=(x,e)$ giving $g_{ij}=e$. If you pick arbitrary smooth maps $h_i:U_i\to G$ and set $s'_i(x)=(x,h_i(x))$, then the new transition functions are
   \[
   g'_{ij}=h_i^{-1}h_j,
   \]
   and the cocycles $\{e\}$ and $\{g'_{ij}\}$ are equivalent by construction.

3. **Hopf line bundles of different degree are not equivalent.**  
   Cover $S^2$ by the standard northern and southern charts $U_N,U_S$ with overlap $U_N\cap U_S\simeq S^1$. For $G=U(1)$, transition functions
   \[
   g_{NS}(\theta)=e^{ik\theta}
   \]
   define complex line bundles with different first {{< knowl id="chern-class" text="Chern class" >}} (the integer $k$). If $k\neq k'$, there are no $h_N,h_S$ making $e^{ik'\theta}=h_N^{-1}e^{ik\theta}h_S$, so the cocycles are not equivalent.
