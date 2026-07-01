+++
id = "algebra-homological/derived-functor"
title = "Derived functor"
kind = "knowl"
summary = "Functors R^nF and L_nF obtained from resolutions, measuring the failure of exactness and yielding Ext and Tor."
aliases = ["derived-functor", "Derived functor"]
domains = ["algebra-homological"]
legacy_source_path = "algebra-homological/derived-functor.md"
+++

Derived functors formalize the idea that a non-exact functor can be “corrected” by replacing objects with resolutions and then taking homology/cohomology.

Throughout, let \(\mathcal A,\mathcal B\) be [[algebra-category-theory/abelian-category|abelian categories]] and \(F:\mathcal A\to\mathcal B\) an additive functor.

## Right derived functors (from injective resolutions)
Assume \(F\) is [[algebra-category-theory/left-exact-functor|left exact]] and \(\mathcal A\) has enough injectives (so [[algebra-homological/injective-resolution|injective resolutions]] exist).

For \(A\in\mathcal A\), choose an injective resolution \(0\to A\to I^\bullet\). Apply \(F\) termwise to get a cochain complex \(F(I^\bullet)\) in \(\mathcal B\). The **right derived functors** of \(F\) are
\[
R^nF(A)\;:=\;H^n\bigl(F(I^\bullet)\bigr)\qquad (n\ge 0),
\]
where \(H^n\) is [[algebra-homological/cohomology-module|cohomology]].

Key facts (standard in homological algebra):
- \(R^0F \cong F\).
- \(R^nF(A)\) is independent of the chosen injective resolution up to canonical isomorphism.
- A short exact sequence in \(\mathcal A\) induces a [[algebra-homological/long-exact-sequence-derived|long exact sequence]] in the \(R^nF\).

## Left derived functors (from projective resolutions)
Assume \(F\) is right exact and \(\mathcal A\) has enough projectives (so [[algebra-homological/projective-resolution|projective resolutions]] exist).

For \(A\in\mathcal A\), choose a projective resolution \(P_\bullet\to A\). Apply \(F\) termwise to get a chain complex \(F(P_\bullet)\) in \(\mathcal B\). The **left derived functors** are
\[
L_nF(A)\;:=\;H_n\bigl(F(P_\bullet)\bigr)\qquad (n\ge 0),
\]
where \(H_n\) is [[algebra-homological/homology-module|homology]].

Again:
- \(L_0F \cong F\).
- \(L_nF(A)\) is well-defined up to canonical isomorphism.
- Short exact sequences yield long exact sequences in the \(L_nF\).

## Fundamental examples: Ext and Tor
In \(\mathcal A = R\text{-Mod}\):
- The functor \(\operatorname{Hom}_R(M,-)\) is [[algebra-homological/hom-left-exact|left exact]], and its right derived functors are $R^n\operatorname{Hom}_R(M,-)\cong \mathrm{Ext}_R^n(M,-)$ (see [[algebra-homological/ext|Ext]]).
- The functor \(-\otimes_R N\) is [[algebra-homological/tensor-right-exact|right exact]], and its left derived functors are $L_n(-\otimes_R N)\cong \mathrm{Tor}_n^R(-,N)$ (see [[algebra-homological/tor|Tor]]).
See also [[algebra-homological/ext-tor-derived-functors|Ext and Tor as derived functors]].

## Examples (explicit computations)

### Example 1: Computing \(\mathrm{Tor}_1^{\mathbb Z}(\mathbb Z/n,\mathbb Z/m)\) as a left derived functor
Let \(F(-)= -\otimes_{\mathbb Z}\mathbb Z/m\mathbb Z\). Take the projective resolution
\[
0\to \mathbb Z \xrightarrow{\times n} \mathbb Z \to \mathbb Z/n\mathbb Z \to 0.
\]
Applying \(F\) gives
\[
0\to \mathbb Z/m \xrightarrow{\times n} \mathbb Z/m \to 0,
\]
so
\[
L_1F(\mathbb Z/n)\cong H_1\cong \ker(\times n:\mathbb Z/m\to\mathbb Z/m)\cong \mathbb Z/\gcd(m,n)\mathbb Z.
\]
Thus $\mathrm{Tor}_1^{\mathbb Z}(\mathbb Z/n,\mathbb Z/m)\cong \mathbb Z/\gcd(m,n)\mathbb Z$ (see [[algebra-homological/tor|Tor]]).

### Example 2: Computing \(\mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z)\) as a right derived functor
Let \(F(-)=\operatorname{Hom}_{\mathbb Z}(\mathbb Z/n,-)\), which is left exact. Use the injective resolution
\[
0\to \mathbb Z \to \mathbb Q \to \mathbb Q/\mathbb Z \to 0.
\]
Applying \(F\) gives
\[
0\to \operatorname{Hom}(\mathbb Z/n,\mathbb Q)\to \operatorname{Hom}(\mathbb Z/n,\mathbb Q/\mathbb Z)\to 0,
\]
with \(\operatorname{Hom}(\mathbb Z/n,\mathbb Q)=0\) and \(\operatorname{Hom}(\mathbb Z/n,\mathbb Q/\mathbb Z)\cong \mathbb Z/n\). Hence
\[
R^1F(\mathbb Z)\cong H^1 \cong \mathbb Z/n\mathbb Z,
\]
i.e. $\mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z)\cong \mathbb Z/n\mathbb Z$ (see [[algebra-homological/ext|Ext]]).

### Example 3: Exact functors have no higher derived functors
If \(F\) is an [[algebra-category-theory/exact-functor|exact functor]] (e.g. in module categories, localization is exact on suitable classes of modules), then applying \(F\) to any resolution preserves exactness. Consequently,
\[
R^nF=0 \ (n>0)\quad\text{and}\quad L_nF=0 \ (n>0),
\]
whenever the relevant derived functors are defined (right/left).
