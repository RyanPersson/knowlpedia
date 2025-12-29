---
title: "Indexed family of sets"
description: "A function assigning a set to each element of an index set."
---

An **indexed family of sets** is a function
$$i \longmapsto A_i$$
from an **index set** $I$ to the class of sets. It is typically denoted by $\{A_i\}_{i\in I}$.

Indexed families let one take unions/intersections over arbitrary index sets (including infinite ones) and are pervasive in analysis (e.g., sequences of sets correspond to the case $I=\mathbb{N}$).

**Examples:**
- A sequence of sets $(A_n)_{n\in\mathbb{N}}$ is an indexed family with $I=\mathbb{N}$.
- In $\mathbb{R}$, $A_n := (-1/n,1/n)$ for $n\in\mathbb{N}$ defines an indexed family of open intervals.
- If $I=\{1,2,3\}$ and $A_1=\{0\}$, $A_2=\{1,2\}$, $A_3=\varnothing$, then $\{A_i\}_{i\in I}$ is a finite indexed family.
