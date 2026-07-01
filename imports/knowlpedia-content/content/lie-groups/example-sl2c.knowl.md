+++
id = "lie-groups/example-sl2c"
title = "Example:"
kind = "knowl"
summary = "The 3D simple Lie algebra of traceless complex matrices with standard relations."
aliases = ["example-sl2c", "Example:"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/example-sl2c.md"
+++

Let [[lie-groups/special-linear-lie-algebra|$\mathfrak{sl}_2(\mathbb C)$]] be the Lie algebra of traceless $2\times 2$ complex matrices with bracket the commutator.

## Standard basis and brackets (explicit calculation)
Define
\[
E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
F=\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
H=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
Compute:
\[
[H,E]=HE-EH
=\begin{pmatrix}0&2\\0&0\end{pmatrix}=2E,\qquad
[H,F]=HF-FH
=\begin{pmatrix}0&0\\-2&0\end{pmatrix}=-2F,
\]
and
\[
[E,F]=EF-FE
=\begin{pmatrix}1&0\\0&-1\end{pmatrix}=H.
\]
These relations imply $[\mathfrak{sl}_2,\mathfrak{sl}_2]=\mathfrak{sl}_2$, so it is perfect (see [[lie-groups/derived-subalgebra|derived subalgebra]]) and in fact [[lie-groups/simple-lie-algebra|simple]].

## Cartan and root decomposition
A [[lie-groups/cartan-subalgebra|Cartan subalgebra]] is $\mathfrak h=\mathbb C H$. The adjoint action $\mathrm{ad}_H$ is diagonalizable on $\mathfrak{sl}_2$ with
\[
\mathrm{ad}_H(E)=2E,\qquad \mathrm{ad}_H(F)=-2F,\qquad \mathrm{ad}_H(H)=0.
\]
Thus the [[lie-groups/root-space-decomposition|root space decomposition]] has one-dimensional root spaces:
\[
\mathfrak g_{2}=\mathbb C E,\quad \mathfrak g_{-2}=\mathbb C F,\quad \mathfrak g_{0}=\mathbb C H.
\]
With an appropriate positivity choice, $2$ is the positive root and $-2$ the negative root (compare [[lie-groups/positive-root|positive roots]]).

## Killing form (quick computation pattern)
The [[lie-groups/killing-form|Killing form]] is nondegenerate, consistent with [[lie-groups/killing-form-nondegenerate-iff-semisimple|nondegenerate iff semisimple]]. For example, one can compute $\kappa(H,H)=8$ and $\kappa(E,F)=4$ by evaluating traces of $\mathrm{ad}$-operators in this basis.

**Context.** $\mathfrak{sl}_2(\mathbb C)$ is the local model for rank-1 semisimple theory; many general results (weights, highest-weight modules) can be tested concretely here (see [[lie-groups/highest-weight-theorem|highest-weight theorem]]).
