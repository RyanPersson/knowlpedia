---
title: "Balanced and absorbing sets"
description: "Two scaling properties of subsets in a vector space"
---

Let $X$ be a {{< knowl id="vector-space" section="linear-algebra" section="linear-algebra" text="vector space" >}} over $K\in\{\mathbb{R},\mathbb{C}\}$, and let $M\subset X$.

- $M$ is **balanced** if $\lambda M\subset M$ whenever $\lambda\in K$ and $|\lambda|\le 1$. (Equivalently: scaling vectors in $M$ down by a factor of modulus $\le 1$ keeps you inside $M$.)

- $M$ is **absorbing** if for every $x\in X$ there exists $\lambda>0$ such that
  $$
  x\in \alpha M \quad\text{whenever }\alpha\in K\text{ and }|\alpha|\ge \lambda.
  $$

  (In particular, taking $\alpha=\lambda$ shows: for each $x$ there exists some scalar $t>0$ with $x\in tM$.)

Balanced and absorbing sets are the natural hypotheses for defining the {{< knowl id="minkowski-function-gauge-of-a-set" text="Minkowski gauge" >}} and relating it to algebraic interior notions.

**Examples:**
- In a normed space, the closed unit ball $\{x:\|x\|\le 1\}$ is balanced.
- In $\mathbb{R}^n$, any neighborhood of the origin that contains a ball around $0$ is absorbing.
- A proper linear subspace $L\subsetneq X$ is balanced, but not absorbing in $X$ (it cannot "reach" vectors outside $L$ by scaling).
