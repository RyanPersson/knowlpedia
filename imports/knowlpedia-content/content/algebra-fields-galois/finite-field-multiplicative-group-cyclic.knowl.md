+++
id = "algebra-fields-galois/finite-field-multiplicative-group-cyclic"
title = "Multiplicative group of a finite field is cyclic"
kind = "knowl"
summary = "For a finite field F_q, the group F_q^× is cyclic of order q−1."
aliases = ["finite-field-multiplicative-group-cyclic", "Multiplicative group of a finite field is cyclic"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/finite-field-multiplicative-group-cyclic.md"
+++

Let \(\mathbb{F}_q\) be a [[algebra-fields-galois/finite-field|finite field]] with \(q\) elements. Its nonzero elements form a group under multiplication,
\[
\mathbb{F}_q^\times=\mathbb{F}_q\setminus\{0\},
\]
which is an [[algebra-groups/abelian-group|abelian group]].

**Theorem.** The multiplicative group \(\mathbb{F}_q^\times\) is cyclic. In particular,
\[
|\mathbb{F}_q^\times| = q-1
\]
and there exists an element \(g\in\mathbb{F}_q^\times\) such that every nonzero element equals \(g^k\) for some integer \(k\). Such a \(g\) is often called a *primitive element* of \(\mathbb{F}_q\).

This cyclicity is frequently paired with the [[algebra-fields-galois/primitive-element-theorem|primitive element theorem]]: it provides explicit generators for many finite [[algebra-fields-galois/field-extension|field extensions]], especially in the finite-field setting.

### Examples
1. \(\mathbb{F}_5^\times=\{1,2,3,4\}\) has order \(4\) and is cyclic: \(2\) is a generator since
   \[
   2^1=2,\quad 2^2=4,\quad 2^3=3,\quad 2^4=1 \pmod 5.
   \]

2. \(\mathbb{F}_4^\times\) has order \(3\), hence is cyclic of order \(3\).
   If \(\alpha\) is a root of \(x^2+x+1\) in \(\mathbb{F}_4\cong \mathbb{F}_2[x]/(x^2+x+1)\), then \(\mathbb{F}_4^\times=\{1,\alpha,\alpha+1\}\) and \(\alpha\) generates it.

3. \(\mathbb{F}_8^\times\) has order \(7\), so it is cyclic of prime order \(7\).
   Thus every nonzero element other than \(1\) is automatically a generator of \(\mathbb{F}_8^\times\).
