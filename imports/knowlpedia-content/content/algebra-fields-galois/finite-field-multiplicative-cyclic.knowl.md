+++
id = "algebra-fields-galois/finite-field-multiplicative-cyclic"
title = "Multiplicative Group of a Finite Field Is Cyclic"
kind = "knowl"
summary = "For a finite field 𝔽_q, the group 𝔽_q× of nonzero elements is cyclic of order q−1."
aliases = ["finite-field-multiplicative-cyclic", "Multiplicative Group of a Finite Field Is Cyclic"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/finite-field-multiplicative-cyclic.md"
+++

Let $\mathbb{F}_q$ be a [[algebra-fields-galois/finite-field|finite field]] with $q$ elements. Its multiplicative group of nonzero elements is
\[
\mathbb{F}_q^\times=\mathbb{F}_q\setminus\{0\},
\]
which is an [[algebra-groups/abelian-group|abelian group]] under multiplication.

**Theorem (cyclicity of $\mathbb{F}_q^\times$).**
The group $\mathbb{F}_q^\times$ is cyclic of order $q-1$. Equivalently, there exists $\gamma\in\mathbb{F}_q^\times$ such that
\[
\mathbb{F}_q^\times=\{\gamma^k:0\le k\le q-2\}.
\]
Such a generator is often called a *primitive element* of $\mathbb{F}_q$; it is also a [[algebra-fields-galois/primitive-root-of-unity|primitive $(q-1)$st root of unity]] in the field.

This statement is sometimes recorded as [[algebra-fields-galois/finite-field-multiplicative-group-cyclic|the cyclicity of the finite-field multiplicative group]].

### Examples
1. **$\mathbb{F}_5^\times$ is cyclic of order $4$.**
   We have $\mathbb{F}_5^\times=\{1,2,3,4\}$. The element $2$ generates:
   \[
   2^1=2,\quad 2^2=4,\quad 2^3=3,\quad 2^4=1 \pmod 5,
   \]
   so $\mathbb{F}_5^\times=\langle 2\rangle$.

2. **$\mathbb{F}_7^\times$ is cyclic of order $6$.**
   Here $\mathbb{F}_7^\times=\{1,2,3,4,5,6\}$ and $3$ is a generator:
   \[
   3,\,3^2=2,\,3^3=6,\,3^4=4,\,3^5=5,\,3^6=1 \pmod 7,
   \]
   so every nonzero element is a power of $3$.

3. **$\mathbb{F}_8^\times$ has prime order $7$.**
   Since $|\mathbb{F}_8^\times|=8-1=7$ is prime, every element of $\mathbb{F}_8^\times$ other than $1$ has order $7$, hence is a generator. For instance, if $\mathbb{F}_8\cong \mathbb{F}_2[\alpha]/(f(\alpha))$ for some irreducible cubic $f$ over $\mathbb{F}_2$ (as in [[algebra-fields-galois/finite-field-existence|finite-field existence]]), then $\alpha\ne 1$ and therefore $\mathbb{F}_8^\times=\langle \alpha\rangle$.
