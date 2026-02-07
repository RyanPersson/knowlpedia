---
title: "Kernel (categorical)"
description: "In a pointed category, the kernel of f:A→B is the equalizer of f and the zero morphism A→B."
---

Kernels are a categorical version of “solutions of \(f(x)=0\)”, defined using universal properties.

Throughout, assume \(\mathcal C\) is a {{< knowl id="category" text="category" >}} with a zero object (e.g. any {{< knowl id="additive-category" text="additive category" >}}), so that for any objects \(A,B\) there is a distinguished **zero morphism** \(0_{A,B}:A\to B\).

## Definition (Kernel)
Given a morphism \(f:A\to B\) in \(\mathcal C\), a **kernel** of \(f\) is a morphism
\[
k:K\to A
\]
such that:
1. \(f\circ k = 0_{K,B}\), and
2. (Universal property) for every morphism \(t:T\to A\) with \(f\circ t=0_{T,B}\), there exists a unique morphism \(u:T\to K\) with
   \[
   k\circ u = t.
   \]

Equivalently, \(k:K\to A\) is an {{< knowl id="equalizer" text="equalizer" >}} of the parallel pair \(f,0_{A,B}:A\rightrightarrows B\).

A kernel, if it exists, is unique up to unique {{< knowl id="isomorphism-category" text="isomorphism" >}}. In any category, kernels are {{< knowl id="monomorphism-category" text="monomorphisms" >}} (because equalizers are monic).

## Examples
1. **\(\mathbf{Ab}\).** For a homomorphism \(f:A\to B\) of abelian groups, \(\ker(f)\subseteq A\) with inclusion \(\ker(f)\hookrightarrow A\) is the categorical kernel.

2. **\(R\)\(-\)\(\mathbf{Mod}\).** For an \(R\)-linear map \(f:M\to N\), the usual submodule \(\{m\in M : f(m)=0\}\) with inclusion is the kernel.

3. **\(\mathbf{Grp}\).** For a group homomorphism \(f:G\to H\), the usual kernel \(\{g\in G : f(g)=e\}\) with inclusion is the categorical kernel (here the zero morphism \(G\to H\) is the constant map to the identity element).
