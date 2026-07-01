+++
id = "real-analysis/sufficient-condition-for-differentiability"
title = "Sufficient condition for differentiability"
kind = "knowl"
summary = "Continuity of partial derivatives at a point implies differentiability of a multivariable function there."
aliases = ["sufficient-condition-for-differentiability", "Sufficient condition for differentiability"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/sufficient-condition-for-differentiability.md"
+++

**Sufficient condition for differentiability:** Let $U\subseteq\mathbb{R}^n$ be open and let $f:U\to\mathbb{R}^m$ be a [[shared-foundations/function|function]]. Fix $a\in U$. Assume that each first-order [[real-analysis/partial-derivative|partial derivative]] $\partial f_i/\partial x_j$ exists on a neighborhood of $a$ and is continuous at $a$ (for all components $i=1,\dots,m$ and coordinates $j=1,\dots,n$). Then $f$ is [[real-analysis/differentiable-map|differentiable]] at $a$ in the sense of the [[real-analysis/frechet-derivative|Fréchet derivative]], and its derivative is the linear map represented by the [[real-analysis/jacobian-matrix|Jacobian matrix]] at $a$.

In particular, continuity of the first partial derivatives is a practical hypothesis for verifying differentiability, and it places $Df(a)$ in the framework of [[linear-algebra/linear-map|linear maps]] between Euclidean spaces.
