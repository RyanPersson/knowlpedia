+++
id = "algebra-homological/connecting-homomorphism-lemma"
title = "Connecting homomorphism (boundary map) lemma"
kind = "knowl"
summary = "From a short exact sequence of complexes (or of objects with a left/right exact functor), one constructs natural connecting maps yielding a long exact sequence in homology/cohomology."
aliases = ["connecting-homomorphism-lemma", "Connecting homomorphism (boundary map) lemma"]
domains = ["algebra-homological"]
legacy_source_path = "algebra-homological/connecting-homomorphism-lemma.md"
+++

Connecting homomorphisms are the maps that “link” adjacent degrees in a long exact sequence, and they are the key output of diagram chasing (compare [[algebra-homological/snake-lemma|snake lemma]]).

## Connecting map for a short exact sequence of chain complexes
Let
\[
0 \longrightarrow A_\bullet \xrightarrow{i} B_\bullet \xrightarrow{p} C_\bullet \longrightarrow 0
\]
be a short exact sequence of [[algebra-homological/chain-complex|chain complexes]] in an [[algebra-category-theory/abelian-category|abelian category]] (in particular, this holds for \(R\)-modules). Then there is a natural long exact sequence in [[algebra-homological/homology-module|homology]]:
\[
\cdots \to H_n(A) \to H_n(B) \to H_n(C) \xrightarrow{\ \delta\ } H_{n-1}(A) \to H_{n-1}(B)\to \cdots
\]
where \(\delta\) is the **connecting homomorphism**.

### Explicit construction of \(\delta\)
Given a class \([c]\in H_n(C)\), choose a cycle representative \(c\in Z_n(C)\).
1. Pick \(b\in B_n\) with \(p(b)=c\) (possible since \(p\) is degreewise surjective).
2. Since \(c\) is a cycle, \(0=d_C(c)=d_C(p(b))=p(d_B(b))\), so \(d_B(b)\in \ker(p)=\operatorname{im}(i)\).
3. Choose \(a\in A_{n-1}\) with \(i(a)=d_B(b)\).
4. One checks \(a\) is a cycle and that its homology class \([a]\in H_{n-1}(A)\) is independent of all choices.

Define \(\delta([c]) := [a]\).

This is the mechanism behind the connecting maps in [[algebra-homological/long-exact-sequence-derived|long exact sequences from derived functors]], such as [[algebra-homological/long-exact-sequence-tor|Tor]] and [[algebra-homological/long-exact-sequence-ext|Ext]] long exact sequences.

## Examples

### Example 1 (Tor: identifying the connecting map with a kernel)
In \(\mathbf{Ab}\), start with
\[
0\to \mathbb Z \xrightarrow{\cdot n} \mathbb Z \to \mathbb Z/n \to 0
\]
and tensor with \(\mathbb Z/m\). Because tensor is [[algebra-homological/tensor-right-exact|right exact]], you get an exact sequence
\[
\operatorname{Tor}_1^\mathbb Z(\mathbb Z/n,\mathbb Z/m)\xrightarrow{\ \delta\ } \mathbb Z/m \xrightarrow{\cdot n} \mathbb Z/m \to (\mathbb Z/n)\otimes(\mathbb Z/m)\to 0.
\]
Exactness forces
\[
\operatorname{im}(\delta)=\ker(\cdot n : \mathbb Z/m\to \mathbb Z/m),
\]
so \(\delta\) identifies \(\operatorname{Tor}_1^\mathbb Z(\mathbb Z/n,\mathbb Z/m)\) with the \(n\)-torsion in \(\mathbb Z/m\), which is cyclic of order \(\gcd(n,m)\).

### Example 2 (Ext: boundary map from a short exact sequence in the second variable)
Given a short exact sequence \(0\to N'\to N\to N''\to 0\), applying the left exact functor [[algebra-modules/hom-module|\(\operatorname{Hom}_R(M,-)\)]] produces a connecting map
\[
\delta:\operatorname{Hom}_R(M,N'') \to \operatorname{Ext}^1_R(M,N')
\]
appearing in [[algebra-homological/long-exact-sequence-ext|the long exact Ext sequence]].
Concretely, a map \(f:M\to N''\) defines a pullback extension of \(M\) by \(N'\), and \(\delta(f)\) is precisely its class in \(\operatorname{Ext}^1\) (compare [[algebra-homological/ext1-classifies-extensions|Ext\(^1\) classifies extensions]]).

### Example 3 (homology of a mapping cone short exact sequence)
Given a chain map \(u:A_\bullet\to B_\bullet\), there is a short exact sequence of complexes
\[
0\to B_\bullet \to \mathrm{Cone}(u)_\bullet \to A_\bullet[-1]\to 0.
\]
The connecting homomorphism in the associated long exact sequence recovers the map on homology induced by \(u\). This is a standard way to package “\(u_*\)” as a boundary map.
