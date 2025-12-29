---
title: "Jordan content"
description: "The volume assigned to a finite union of rectangles, used as a precursor to measure."
---

A **(closed) rectangle** in $\mathbb{R}^k$ is a set of the form
$$R=\prod_{j=1}^k [a_j,b_j],\qquad a_j\le b_j,$$
with **volume**
$$\operatorname{vol}(R)=\prod_{j=1}^k (b_j-a_j).$$

An **elementary set** is a finite union of rectangles. If an elementary set $E$ is written as a finite union of pairwise disjoint rectangles $R_1,\dots,R_N$, its **Jordan content** (also called **content**) is
$$c(E):=\sum_{i=1}^N \operatorname{vol}(R_i).$$
(One checks that for elementary sets this is well-defined: different disjoint-rectangle decompositions yield the same total volume.)

Jordan content is a finite-additive "volume" defined on elementary sets, and it provides a convenient language for coverings in measure-zero arguments without requiring full measure theory.

**Examples:**
- For a rectangle $R$, $c(R)=\operatorname{vol}(R)$.
- In $\mathbb{R}$, if $E=[0,1]\cup[2,3]$ (disjoint union), then $c(E)=1+1=2$.
- If two rectangles overlap, one first decomposes their union into disjoint rectangles to compute content additively.
