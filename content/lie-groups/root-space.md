---
title: "Root space"
description: "The eigenspace g_α for the adjoint action of a Cartan subalgebra corresponding to a root α."
---

Let $\mathfrak g$ be a complex semisimple Lie algebra and $\mathfrak h\subset\mathfrak g$ a {{< knowl id="cartan-subalgebra" text="Cartan subalgebra" >}}. For $\alpha\in\mathfrak h^*$, the **root space** (more generally, the $\alpha$-weight space for $\mathrm{ad}|_{\mathfrak h}$) is
\[
\mathfrak g_\alpha \;=\;\{X\in\mathfrak g : [H,X]=\alpha(H)\,X\ \text{for all }H\in\mathfrak h\}.
\]
If $\alpha\neq 0$ and $\mathfrak g_\alpha\neq 0$, then $\alpha$ is a {{< knowl id="root-lie-algebra" text="root" >}} and $\mathfrak g_\alpha$ is its root space.

These spaces interact well with the Lie bracket: if $X\in\mathfrak g_\alpha$ and $Y\in\mathfrak g_\beta$, then
\[
[H,[X,Y]] = (\alpha(H)+\beta(H))\,[X,Y]\quad\text{for all }H\in\mathfrak h,
\]
so $[\mathfrak g_\alpha,\mathfrak g_\beta]\subseteq \mathfrak g_{\alpha+\beta}$ (interpreting $\mathfrak g_{\alpha+\beta}=0$ if $\alpha+\beta$ is not a weight). This is one of the structural inputs for the {{< knowl id="root-space-decomposition" text="root space decomposition" >}}.

**Concrete calculation (the $\mathfrak{sl}_2$ case).**  
Let $\mathfrak g=\mathfrak{sl}_2(\mathbb C)$ (see {{< knowl id="example-sl2c" text="standard sl2 example" >}}) with basis
\[
H=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
F=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
\]
Take $\mathfrak h=\mathbb C\cdot H$. Then
\[
[H,E]=2E,\qquad [H,F]=-2F.
\]
Define $\alpha\in\mathfrak h^*$ by $\alpha(H)=2$. Then $\mathfrak g_\alpha=\mathbb C\cdot E$ and $\mathfrak g_{-\alpha}=\mathbb C\cdot F$, giving the familiar decomposition
\[
\mathfrak{sl}_2(\mathbb C)=\mathfrak h\oplus \mathfrak g_\alpha\oplus \mathfrak g_{-\alpha}.
\]
