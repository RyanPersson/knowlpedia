---
title: "Linear independence and dependence"
description: "A set is linearly independent if only the trivial finite linear combination equals zero"
---

Let $X$ be a {{< knowl id="vector-space" section="linear-algebra" section="linear-algebra" text="vector space" >}} over $K$, and let $M\subset X$.

The set $M$ is **linearly independent** if for every finite subset $\{x_1,\dots,x_m\}\subset M$ and every choice of scalars $\alpha_1,\dots,\alpha_m\in K$,
$$
\sum_{i=1}^m \alpha_i x_i = 0 \quad\Longrightarrow\quad \alpha_1=\cdots=\alpha_m=0.
$$

If $M$ is not linearly independent, it is **linearly dependent**, i.e., there exists a finite subset and scalars, not all zero, giving a zero {{< knowl id="linear-combination" text="linear combination" >}}.

Linear independence is one of the two defining properties of a {{< knowl id="basis-hamel-basis-and-dimension" text="basis" >}}.

**Examples:**
- The standard unit vectors $e_1,\dots,e_n$ in $\mathbb{R}^n$ are linearly independent.
- The set $\{(1,0),(2,0)\}\subset\mathbb{R}^2$ is linearly dependent since $2(1,0)-(2,0)=0$.
- Any set containing the zero vector is linearly dependent: if $0\in M$, then $1\cdot 0=0$ is a nontrivial dependence.
- The empty set is linearly independent (there is no finite nonempty subset to witness dependence).
