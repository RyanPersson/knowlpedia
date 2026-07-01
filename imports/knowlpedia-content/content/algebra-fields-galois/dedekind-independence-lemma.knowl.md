+++
id = "algebra-fields-galois/dedekind-independence-lemma"
title = "Dedekind independence lemma"
kind = "knowl"
summary = "Distinct K-embeddings of a field are linearly independent as functions."
aliases = ["dedekind-independence-lemma", "Dedekind independence lemma"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/dedekind-independence-lemma.md"
+++

Let \(K \subseteq L\) be a [[algebra-fields-galois/field-extension|field extension]], and let \(\Omega\) be a field containing (identified copies of) the images of \(L\) under the embeddings below. If
\[
\sigma_1,\dots,\sigma_n : L \hookrightarrow \Omega
\]
are **distinct** [[algebra-fields-galois/field-embedding|field embeddings]] that fix \(K\), then they are linearly independent over \(\Omega\) when viewed as \(\Omega\)-valued [[shared-foundations/function|functions]] on \(L\). Concretely:

> If \(a_1,\dots,a_n \in \Omega\) satisfy
> \[
> a_1\sigma_1(x)+\cdots+a_n\sigma_n(x)=0 \quad \text{for all } x\in L,
> \]
> then \(a_1=\cdots=a_n=0\).

Equivalently, the \(\Omega\)-vector space \(\Omega^L\) of all functions \(L\to\Omega\) contains \(\{\sigma_1,\dots,\sigma_n\}\) as a linearly independent set.

This lemma is frequently applied with \(\Omega=L\) and \(\sigma_i\) ranging over a subgroup of the [[algebra-fields-galois/galois-group|Galois group]] (or more generally the [[algebra-fields-galois/field-automorphism|field automorphism]] group) of \(L\).

### Examples

1. **Two embeddings of a quadratic extension.**
   In \(L=\mathbb{Q}(\sqrt2)\subset \mathbb{C}\), there are two \(\mathbb{Q}\)-embeddings into \(\mathbb{C}\): the identity \(\mathrm{id}\) and conjugation \(\tau(\sqrt2)=-\sqrt2\). If \(a\,\mathrm{id}+b\,\tau=0\) as functions, then evaluating at \(1\) gives \(a+b=0\), and at \(\sqrt2\) gives \(a\sqrt2-b\sqrt2=0\), hence \(a=b=0\).

2. **Cyclotomic embeddings.**
   For \(L=\mathbb{Q}(\zeta_n)\) with \(\zeta_n\) a [[algebra-fields-galois/primitive-root-of-unity|primitive root of unity]], the distinct embeddings \(\sigma_k(\zeta_n)=\zeta_n^k\) (for \(\gcd(k,n)=1\)) are linearly independent as \(\mathbb{C}\)-valued functions on \(L\).

3. **Finite-field Frobenius powers.**
   In a finite field \(L=\mathbb{F}_{p^m}\), the maps \(x\mapsto x^{p^i}\) are distinct [[algebra-fields-galois/field-automorphism|automorphisms]] for \(0\le i<m\) (see [[algebra-fields-galois/finite-field-galois-group-cyclic|cyclic Galois group of a finite field]]). Dedekind independence implies no nontrivial \(\mathbb{F}_{p^m}\)-linear combination of these maps vanishes identically.
