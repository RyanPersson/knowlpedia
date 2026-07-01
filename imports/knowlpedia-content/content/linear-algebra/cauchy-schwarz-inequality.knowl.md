+++
id = "linear-algebra/cauchy-schwarz-inequality"
title = "Cauchy–Schwarz inequality"
kind = "knowl"
summary = "In an inner product space, the absolute value of an inner product is at most the product of norms."
aliases = ["cauchy-schwarz-inequality", "Cauchy–Schwarz inequality"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/cauchy-schwarz-inequality.md"
+++

**Cauchy–Schwarz inequality:** In an [[linear-algebra/inner-product-space|inner product space]] $(V,\langle\cdot,\cdot\rangle)$, for all $x,y\in V$,
\[
|\langle x,y\rangle|\le \|x\|\,\|y\|,
\]
where $\|x\|=\sqrt{\langle x,x\rangle}$ is the induced [[linear-algebra/norm|norm]]. Equality holds if and only if $x$ and $y$ are linearly dependent.

In a [[linear-algebra/euclidean-space|Euclidean space]], this bounds the dot product by the product of Euclidean lengths. It is central for understanding [[linear-algebra/orthogonality|orthogonality]] and for many norm inequalities in inner product geometry.
