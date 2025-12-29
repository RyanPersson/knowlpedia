---
title: "Set-valued mapping (multifunction), domain, graph, and convexity"
description: "A set-valued map assigns sets to points; convexity is defined via its graph"
---

Let $X,Y$ be vector spaces. A **set-valued mapping** (or **multifunction**) is a map
$$
F:X\rightrightarrows Y
$$
that assigns to each $x\in X$ a (possibly empty) subset $F(x)\subset Y$.

- The **domain** of $F$ is
$$
\mathrm{dom}(F):=\{x\in X: F(x)\neq\emptyset\}.
$$
- The **graph** of $F$ is the subset of the {{< knowl id="product-space-cartesian-product" text="product space" >}} $X\times Y$ given by
$$
\mathrm{gph}(F):=\{(x,y)\in X\times Y: y\in F(x)\}.
$$

The multifunction $F$ is called **convex** if its graph $\mathrm{gph}(F)$ is a {{< knowl id="convex-set" text="convex set" >}} in $X\times Y$.

**Context.** Convex multifunctions generalize convex sets (as graphs) and appear in variational analysis and optimization (e.g., feasible-set and solution mappings).

**Examples:**
- Single-valued affine maps are convex multifunctions: if $F(x)=\{Ax+b\}$, then $\mathrm{gph}(F)$ is an affine subset of $X\times Y$.
- In $X=Y=\mathbb{R}$, the map $F(x)=[x,\infty)$ has a convex graph.
- The constant map $F(x)=C$ has $\mathrm{gph}(F)=X\times C$, convex iff $C$ is convex.
