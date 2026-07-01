+++
id = "real-analysis/hessian-matrix"
title = "Hessian matrix"
kind = "knowl"
summary = "Matrix of second partial derivatives of a scalar function"
aliases = ["hessian-matrix", "Hessian matrix"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/hessian-matrix.md"
+++

A **Hessian matrix** of a function $f:U\to \mathbb{R}$ (with $U\subseteq \mathbb{R}^n$) at a point $a\in U$ is the $n\times n$ matrix
$$
Hf(a)=\left(\frac{\partial^2 f}{\partial x_i\,\partial x_j}(a)\right)_{1\le i,j\le n},
$$
provided these second-order partial derivatives exist.

The off-diagonal entries are [[real-analysis/mixed-partial-derivative|mixed partial derivatives]]. Under the hypotheses of the [[real-analysis/schwarz-clairaut-theorem|Schwarz–Clairaut theorem]], the Hessian is symmetric. The Hessian is used in [[real-analysis/second-derivative-tests|second derivative tests]] for classifying [[real-analysis/critical-point|critical points]].

**Examples:**
- For $f(x,y)=x^2+xy+y^2$, one has
  $$
  Hf(x,y)=\begin{pmatrix}2&1\\[2pt]1&2\end{pmatrix}.
  $$

- For $f(x,y,z)=x^2+y^2+z^2$, one has $Hf(x,y,z)=2I_3$.
