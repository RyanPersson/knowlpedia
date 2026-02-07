---
title: "Total order"
description: "A partial order in which any two elements are comparable."
---

A **total order** on a {{< knowl id="set" text="set" >}} $X$ is a {{< knowl id="partial-order" text="partial order" >}} $\le$ on $X$ such that for all $a,b\in X$, either $a\le b$ or $b\le a$.

Total orders are also called linear orders. A {{< knowl id="well-ordered-set" text="well-ordered set" >}} is a totally ordered set with the additional property that every nonempty subset has a least element.

**Examples:**
- The usual order $\le$ on $\mathbb{Z}$ (the {{< knowl id="integers" text="integers" >}}) is a total order.
- (Lexicographic order) If $X$ and $Y$ are totally ordered, define an order on $X\times Y$ by $(x,y)\le_{\mathrm{lex}}(x',y')$ if either $x<x'$, or $x=x'$ and $y\le y'$ (where $x<x'$ means $x\le x'$ and $x\ne x'$). This gives a total order on the {{< knowl id="cartesian-product" text="Cartesian product" >}} $X\times Y$.
