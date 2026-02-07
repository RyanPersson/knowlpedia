---
title: "Killing form"
description: "The invariant bilinear form B(x,y)=tr(ad_x ad_y) on a Lie algebra."
---

Let $\mathfrak g$ be a finite-dimensional {{< knowl id="lie-algebra" text="Lie algebra" >}} over a field of characteristic $0$ (typically $\mathbb R$ or $\mathbb C$). Let $\mathrm{ad}:\mathfrak g\to\mathfrak{gl}(\mathfrak g)$ be the {{< knowl id="adjoint-representation-of-a-lie-algebra" text="adjoint representation" >}}.

**Definition (Killing form).**  
The **Killing form** on $\mathfrak g$ is the symmetric bilinear form
\[
B:\mathfrak g\times \mathfrak g\to \Bbbk,\qquad B(x,y)=\mathrm{tr}(\mathrm{ad}_x\circ \mathrm{ad}_y).
\]
It is {{< knowl id="killing-form-ad-invariant-lemma" text="ad-invariant" >}} and depends functorially on $\mathfrak g$.

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
For $X,Y\in \mathfrak{sl}_n(\mathbb C)$ (see {{< knowl id="special-linear-lie-algebra" text="sl_n" >}}), the Killing form is a scalar multiple of the trace pairing; in the standard normalization,
\[
B(X,Y)=2n\,\mathrm{tr}(XY).
\]

**Context.**  
Nondegeneracy of $B$ characterizes {{< knowl id="semisimple-lie-algebra" text="semisimplicity" >}} (see {{< knowl id="killing-form-nondegenerate-iff-semisimple" text="the nondegeneracy theorem" >}}) and underlies criteria such as {{< knowl id="cartans-criterion-semisimplicity" text="Cartan's criterion" >}}.
