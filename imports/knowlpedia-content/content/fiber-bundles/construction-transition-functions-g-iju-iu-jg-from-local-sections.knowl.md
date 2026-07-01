+++
id = "fiber-bundles/construction-transition-functions-g-iju-iu-jg-from-local-sections"
title = "Transition functions from local sections"
kind = "knowl"
summary = "How local sections determine transition functions on overlaps in a principal bundle."
aliases = ["construction-transition-functions-g-iju-iu-jg-from-local-sections", "Transition functions from local sections"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/construction-transition-functions-g-iju-iu-jg-from-local-sections.md"
+++

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with the [[fiber-bundles/convention-principal-bundles-use-a-right-g-action-on-p|standard right G-action]]. Let $\{U_i\}$ be an open cover of $M$ and let $s_i:U_i\to P$ be smooth local sections.

## Construction
For each overlap $U_{ij}:=U_i\cap U_j$ and each $x\in U_{ij}$, the points $s_i(x)$ and $s_j(x)$ lie in the same fiber $P_x$. Since the right action is free and transitive on each fiber, there exists a unique element $g_{ij}(x)\in G$ such that
\[
s_j(x) = s_i(x)\cdot g_{ij}(x).
\]
This defines a smooth map
\[
g_{ij}:U_{ij}\to G,
\]
called the **transition function** for the pair $(i,j)$. These are the [[fiber-bundles/principal-bundle-transition-function|principal bundle transition functions]] associated to the chosen local sections, and they encode the change of the [[fiber-bundles/construction-local-trivialization-from-a-local-section|local trivializations coming from the sections]].

## Basic identities
From the defining equation and uniqueness, one immediately gets:
- $g_{ii}(x)=e$ on $U_i$,
- $g_{ji}(x)=g_{ij}(x)^{-1}$ on $U_{ij}$,
- On triple overlaps $U_{ijk}=U_i\cap U_j\cap U_k$,
  \[
  g_{ij}(x)\,g_{jk}(x)=g_{ik}(x),
  \]
  which is the [[fiber-bundles/cocycle-condition-for-transition-functions|cocycle condition]].

Changing the local sections changes the functions $g_{ij}$ by an [[fiber-bundles/equivalence-of-cocycles|equivalence of cocycles]], leaving the underlying bundle unchanged.

## Examples
1. **Trivial bundle.** For $P=M\times G$ with global section $s(x)=(x,e)$, any cover and the restricted sections $s_i=s|_{U_i}$ give $g_{ij}\equiv e$ on all overlaps.

2. **Hopf fibration.** In the [[fiber-bundles/hopf-fibration-s3s2-as-a-principal-u-bundle|Hopf bundle]] $S^3\to S^2$ with structure group $U(1)$, take the standard cover of $S^2\cong \mathbb{CP}^1$ by the charts $U_0=\{[z_1:z_2]\mid z_2\neq 0\}$ and $U_1=\{[z_1:z_2]\mid z_1\neq 0\}$. Using the local sections
   \[
   s_0(w)=\frac{(w,1)}{\sqrt{1+|w|^2}},\qquad s_1(w')=\frac{(1,w')}{\sqrt{1+|w'|^2}},
   \]
   with $w=z_1/z_2$ and $w'=z_2/z_1$, the overlap has $w'=1/w$ and one finds a transition function $g_{01}:U_0\cap U_1\to U(1)$ satisfying $s_1(1/w)=s_0(w)\cdot g_{01}(w)$; a concrete choice is
   \[
   g_{01}(w)=\frac{|w|}{w}\quad (w\neq 0),
   \]
   with $g_{10}=g_{01}^{-1}$.

3. **Möbius bundle as a principal $O(1)$-bundle.** View the Möbius line bundle over $S^1$ as a principal $O(1)=\{\pm 1\}$-bundle. With two local sections over two arcs whose overlap has two components, one component can have transition value $+1$ and the other $-1$, producing a nontrivial cocycle and hence a nontrivial bundle.
