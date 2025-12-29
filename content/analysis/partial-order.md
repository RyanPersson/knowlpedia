---
title: "Partial order"
description: "A relation that is reflexive, antisymmetric, and transitive."
---

A **partial order** on a set $X$ is a relation $\preceq\ \subseteq X\times X$ such that for all $x,y,z\in X$:
- (**Reflexive**) $x\preceq x$.
- (**Antisymmetric**) If $x\preceq y$ and $y\preceq x$, then $x=y$.
- (**Transitive**) If $x\preceq y$ and $y\preceq z$, then $x\preceq z$.

A set equipped with a partial order is a **partially ordered set** (poset). Partial orders capture "comparison" that may leave some pairs incomparable.

**Examples:**
- $(\mathcal{P}(X),\subseteq)$ is a poset for any set $X$.
- On $\mathbb{N}$, define $a\preceq b$ iff $a$ divides $b$; this is a partial order.
- On $\mathbb{R}^2$, define $(x_1,y_1)\preceq(x_2,y_2)$ iff $x_1\le x_2$ and $y_1\le y_2$ (coordinatewise order); many pairs are incomparable.
