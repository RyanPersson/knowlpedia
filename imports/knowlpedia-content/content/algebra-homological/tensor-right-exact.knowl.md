+++
id = "algebra-homological/tensor-right-exact"
title = "Tensor product is right exact"
kind = "knowl"
summary = "For fixed N, the functor -⊗_R N preserves cokernels (exactness on the right); its failure to be left exact is measured by Tor."
aliases = ["tensor-right-exact", "Tensor product is right exact"]
domains = ["algebra-homological"]
legacy_source_path = "algebra-homological/tensor-right-exact.md"
+++

Let $R$ be a [[algebra-rings/ring|ring]].

Fix a left $R$-module $N$. Then the functor
\[
(-)\otimes_R N : (\mathrm{Mod}\text{-}R) \to \mathrm{Ab}
\]
from right $R$-modules to abelian groups is the tensor product functor (see [[algebra-modules/tensor-product|tensor product]]).

(Equivalently, if $M$ is a fixed right $R$-module, then $M\otimes_R(-): R\text{-}\mathrm{Mod}\to\mathrm{Ab}$ is also right exact.)

## Statement (right exactness)
If
\[
A' \xrightarrow{u} A \xrightarrow{v} A'' \to 0
\]
is an exact sequence of right $R$-modules, then
\[
A'\otimes_R N \xrightarrow{u\otimes 1} A\otimes_R N \xrightarrow{v\otimes 1} A''\otimes_R N \to 0
\]
is exact.

Equivalently: tensoring preserves cokernels and epimorphisms.

## Failure of left exactness and Tor
Tensor need not preserve kernels (i.e. it need not preserve injections). For a [[algebra-modules/short-exact-sequence|short exact sequence]]
\[
0 \to A' \to A \to A'' \to 0,
\]
there is a natural exact sequence
\[
\mathrm{Tor}^R_1(A'',N)\to A'\otimes_R N \to A\otimes_R N \to A''\otimes_R N \to 0,
\]
where $\mathrm{Tor}^R_1$ is defined in [[algebra-homological/tor|Tor]] and arises from [[algebra-homological/long-exact-sequence-tor|the long exact sequence in Tor]].

In particular, $N$ is [[algebra-modules/flat-module|flat]] iff $(-)\otimes_R N$ is exact (iff $\mathrm{Tor}^R_1(-,N)=0$).

## Examples

### Example 1: Tensor is not left exact (over $\mathbb Z$)
Consider the injective map of $\mathbb Z$-modules
\[
0 \to \mathbb Z \xrightarrow{\times n} \mathbb Z
\]
with cokernel $\mathbb Z/n$. Tensor with $\mathbb Z/n$:
\[
0 \to \mathbb Z\otimes \mathbb Z/n \xrightarrow{\times n} \mathbb Z\otimes \mathbb Z/n.
\]
Since $\mathbb Z\otimes \mathbb Z/n \cong \mathbb Z/n$ and multiplication by $n$ on $\mathbb Z/n$ is the zero map, the induced map is *not* injective. Concretely,
\[
0 \to \mathbb Z/n \xrightarrow{0} \mathbb Z/n
\]
fails exactness on the left, and the defect is detected by
\[
\mathrm{Tor}^{\mathbb Z}_1(\mathbb Z/n,\mathbb Z/n)\cong \mathbb Z/n \neq 0.
\]

### Example 2: Tensor with a flat module is exact (localization)
Over $\mathbb Z$, the module $\mathbb Q$ is a localization and hence flat. Tensor the short exact sequence
\[
0 \to \mathbb Z \xrightarrow{\times n} \mathbb Z \to \mathbb Z/n \to 0
\]
with $\mathbb Q$:
\[
0 \to \mathbb Q \xrightarrow{\times n} \mathbb Q \to (\mathbb Z/n)\otimes \mathbb Q \to 0.
\]
Here $\times n:\mathbb Q\to\mathbb Q$ is an isomorphism, so $(\mathbb Z/n)\otimes \mathbb Q=0$ and the tensored sequence remains exact.

### Example 3: Tensor with a free module is exact
If $N\cong R^{\oplus r}$ is free, then
\[
A\otimes_R N \cong A^{\oplus r},
\]
so $(-)\otimes_R N$ is a finite direct sum of copies of the identity functor and is therefore exact.
