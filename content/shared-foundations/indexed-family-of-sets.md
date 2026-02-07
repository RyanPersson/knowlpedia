---
title: "Indexed family of sets"
description: "A collection of sets labeled by elements of an index set."
---

An **indexed family of sets** is a {{< knowl id="function" text="function" >}} $A\colon I\to V$ whose domain $I$ is a set (the **index set**) and such that for each $i\in I$, the value $A(i)$ is a set. One writes the family as $(A_i)_{i\in I}$, where $A_i:=A(i)$.

Indexed families unify the notation for operations like {{< knowl id="union" text="union" >}} $\bigcup_{i\in I}A_i$ and {{< knowl id="intersection" text="intersection" >}} $\bigcap_{i\in I}A_i$, which depend on an index set and a set assigned to each index.

**Examples:**
- For $I=\mathbb{N}$, the assignment $n\mapsto\{n\}$ defines a family $(\{n\})_{n\in\mathbb{N}}$.
- For $I=\mathbb{R}$, the assignment $x\mapsto (x,x+1)$ defines a family of intervals $( (x,x+1) )_{x\in\mathbb{R}}$.
