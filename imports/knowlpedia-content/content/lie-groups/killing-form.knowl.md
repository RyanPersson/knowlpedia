+++
id = "lie-groups/killing-form"
title = "Killing form"
kind = "knowl"
summary = "The invariant bilinear form B(x,y)=tr(ad_x ad_y) on a Lie algebra."
aliases = ["killing-form", "Killing form"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/killing-form.md"
+++

Let $\mathfrak g$ be a finite-dimensional [[lie-groups/lie-algebra|Lie algebra]] over a field of characteristic $0$ (typically $\mathbb R$ or $\mathbb C$). Let $\mathrm{ad}:\mathfrak g\to\mathfrak{gl}(\mathfrak g)$ be the [[lie-groups/adjoint-representation-of-a-lie-algebra|adjoint representation]].

**Definition (Killing form).**
The **Killing form** on $\mathfrak g$ is the symmetric bilinear form
\[
B:\mathfrak g\times \mathfrak g\to \Bbbk,\qquad B(x,y)=\mathrm{tr}(\mathrm{ad}_x\circ \mathrm{ad}_y).
\]
It is [[lie-groups/killing-form-ad-invariant-lemma|ad-invariant]] and depends functorially on $\mathfrak g$.

**Example: $\mathfrak{sl}_2(\mathbb C)$.**
With basis
\[
H=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
F=\begin{pmatrix}0&0\\1&0\end{pmatrix},
\]
one computes (using $\mathrm{ad}_X(Y)=[X,Y]$) that
\[
B(H,H)=8,\qquad B(E,F)=4,\qquad B(H,E)=B(H,F)=B(E,E)=B(F,F)=0.
\]
This exhibits nondegeneracy for a simple algebra.

**Example: $\mathfrak{sl}_n(\mathbb C)$.**
For $X,Y\in \mathfrak{sl}_n(\mathbb C)$ (see [[lie-groups/special-linear-lie-algebra|sl_n]]), the Killing form is a scalar multiple of the trace pairing; in the standard normalization,
\[
B(X,Y)=2n\,\mathrm{tr}(XY).
\]

**Context.**
Nondegeneracy of $B$ characterizes [[lie-groups/semisimple-lie-algebra|semisimplicity]] (see [[lie-groups/killing-form-nondegenerate-iff-semisimple|the nondegeneracy theorem]]) and underlies criteria such as [[lie-groups/cartans-criterion-semisimplicity|Cartan's criterion]].
