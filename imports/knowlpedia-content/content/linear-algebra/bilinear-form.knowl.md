+++
id = "linear-algebra/bilinear-form"
title = "Bilinear form"
kind = "knowl"
summary = "A function of two vector arguments that is linear in each argument."
aliases = ["bilinear-form", "Bilinear form"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/bilinear-form.md"
+++

A **bilinear form** on [[linear-algebra/vector-space|vector spaces]] $V$ and $W$ over a field $\mathbb{F}$ is a map
\[
B:V\times W\to \mathbb{F}
\]
such that for all $u_1,u_2\in V$, $v_1,v_2\in W$, and $a,b\in\mathbb{F}$,
\[
B(a u_1+b u_2,\, v)=a\,B(u_1,v)+b\,B(u_2,v),\qquad
B(u,\, a v_1+b v_2)=a\,B(u,v_1)+b\,B(u,v_2).
\]

A bilinear form is a scalar-valued [[shared-foundations/function|function]] on a [[shared-foundations/cartesian-product|Cartesian product]] of vector spaces. Inner products (see [[linear-algebra/inner-product|inner product]]) are important examples with additional positivity and symmetry properties.

**Examples:**
- On $\mathbb{R}^n$, the dot product $B(x,y)=\sum_{i=1}^n x_i y_i$ is a bilinear form.
- For a fixed matrix $A$, the rule $B(x,y)=x^\mathsf{T}Ay$ on $\mathbb{F}^n$ is a bilinear form.
- On $\mathbb{R}^{2}$, the form $B((x_1,x_2),(y_1,y_2))=x_1y_2-x_2y_1$ is a bilinear form.
