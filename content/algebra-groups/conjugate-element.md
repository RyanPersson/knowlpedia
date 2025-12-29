---
title: "Conjugate element"
description: "Two elements of a group are conjugate if one is obtained from the other by an inner automorphism"
---

Let $G$ be a {{< knowl id="group" text="group" >}} and let $g,h\in G$. We say that **$h$ is conjugate to $g$ (in $G$)**, and write $h\sim g$, if there exists an element $x\in G$ such that
$
h = x g x^{-1}.
$
For a fixed $x\in G$, the map $c_x\colon G\to G$ given by $c_x(g)=xgx^{-1}$ is called **conjugation by $x$**; it is an {{< knowl id="inner-automorphism" text="inner automorphism" >}} of $G$.

Conjugacy is an equivalence relation on $G$; its equivalence classes are the {{< knowl id="conjugacy-class" text="conjugacy classes" >}}. Equivalently, conjugacy classes are the orbits of the {{< knowl id="conjugation-action" text="conjugation action" >}} of $G$ on itself. Conjugation also controls normality: a {{< knowl id="normal-subgroup" text="normal subgroup" >}} is precisely a subgroup stable under conjugation.

**Examples:**
- If $G$ is abelian, then $xgx^{-1}=g$ for all $x,g\in G$, so every element is conjugate only to itself.
- In $S_3$, the transpositions are all conjugate: for instance $(123)(12)(123)^{-1}=(23)$.
- In a matrix group $G\le GL_n(\mathbb{F})$, conjugation $XAX^{-1}$ corresponds to similarity of matrices; conjugate matrices represent the same linear operator in different bases.
