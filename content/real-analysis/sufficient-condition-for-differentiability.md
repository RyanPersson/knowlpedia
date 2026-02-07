---
title: "Sufficient condition for differentiability"
description: "Continuity of partial derivatives at a point implies differentiability of a multivariable function there."
---

**Sufficient condition for differentiability:** Let $U\subseteq\mathbb{R}^n$ be open and let $f:U\to\mathbb{R}^m$ be a {{< knowl id="function" section="shared-foundations" text="function" >}}. Fix $a\in U$. Assume that each first-order {{< knowl id="partial-derivative" text="partial derivative" >}} $\partial f_i/\partial x_j$ exists on a neighborhood of $a$ and is continuous at $a$ (for all components $i=1,\dots,m$ and coordinates $j=1,\dots,n$). Then $f$ is {{< knowl id="differentiable-map" text="differentiable" >}} at $a$ in the sense of the {{< knowl id="frechet-derivative" text="Fréchet derivative" >}}, and its derivative is the linear map represented by the {{< knowl id="jacobian-matrix" text="Jacobian matrix" >}} at $a$.

In particular, continuity of the first partial derivatives is a practical hypothesis for verifying differentiability, and it places $Df(a)$ in the framework of {{< knowl id="linear-map" section="linear-algebra" text="linear maps" >}} between Euclidean spaces.
