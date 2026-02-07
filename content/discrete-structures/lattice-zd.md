---
title: "Integer lattice Z^d"
description: "The set of all d-dimensional vectors with integer coordinates."
---

Fix a positive integer \(d\). The **integer lattice** in dimension \(d\) is
\[
\mathbb{Z}^d=\{(x_1,\dots,x_d): x_i\in \mathbb{Z}\},
\]
where \(\mathbb{Z}\) denotes the {{< knowl id="integers" section="shared-foundations" >}}.

Elements \(x\in\mathbb{Z}^d\) are often called **lattice sites** or **lattice points**.

**Algebraic structure.** Addition and subtraction are defined componentwise:
\[
x+y=(x_1+y_1,\dots,x_d+y_d),\qquad x-y=(x_1-y_1,\dots,x_d-y_d).
\]
For \(a\in\mathbb{Z}^d\), the map \(x\mapsto x+a\) is a **translation** of the lattice.

**Standard basis.** For \(i\in\{1,\dots,d\}\), the vector \(e_i\in\mathbb{Z}^d\) is the point with a 1 in the \(i\)-th coordinate and 0 elsewhere. Many local notions on \(\mathbb{Z}^d\) are described using these vectors.

A key combinatorial structure on \(\mathbb{Z}^d\) is the {{< knowl id="nearest-neighbor-zd" >}} adjacency relation, which turns \(\mathbb{Z}^d\) into an infinite graph.
