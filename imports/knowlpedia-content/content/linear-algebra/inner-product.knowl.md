+++
id = "linear-algebra/inner-product"
title = "Inner product"
kind = "knowl"
summary = "A positive-definite product on a vector space that defines lengths and angles."
aliases = ["inner-product", "Inner product"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/inner-product.md"
+++

An **inner product** on a [[linear-algebra/vector-space|vector space]] $V$ over $\mathbb{F}=\mathbb{R}$ or $\mathbb{C}$ is a map
\[
\langle\cdot,\cdot\rangle:V\times V\to\mathbb{F}
\]
such that for all $u,v,w\in V$ and $a,b\in\mathbb{F}$:
\[
\langle au+bw,\,v\rangle=a\langle u,v\rangle+b\langle w,v\rangle,\qquad
\langle u,v\rangle=\overline{\langle v,u\rangle},\qquad
\langle v,v\rangle\ge 0\ \text{and }\langle v,v\rangle=0\iff v=0.
\]

An inner product is closely related to a [[linear-algebra/bilinear-form|bilinear form]] (or sesquilinear form in the complex case). It induces a [[linear-algebra/norm|norm]] via $\|v\|=\sqrt{\langle v,v\rangle}$ and defines [[linear-algebra/orthogonality|orthogonality]] through the condition $\langle u,v\rangle=0$.

**Examples:**
- On $\mathbb{R}^n$, the standard dot product $\langle x,y\rangle=\sum_{i=1}^n x_i y_i$ is an inner product.
- On $\mathbb{C}^n$, the Hermitian product $\langle x,y\rangle=\sum_{i=1}^n x_i\overline{y_i}$ is an inner product.
- If $W$ is a symmetric positive-definite matrix, then $\langle x,y\rangle=x^\mathsf{T}Wy$ defines an inner product on $\mathbb{R}^n$.
