---
title: "Marginal (Optimal Value) Function"
description: "The infimum of an objective over a set-valued constraint mapping"
---

Given a {{< knowl id="set-valued-mapping-multifunction-domain-and-graph-convex-set-valued-mapping" text="set-valued mapping" >}} $F:X\rightrightarrows Y$ and a function $\varphi:X\times Y\to\overline{\mathbb{R}}$, the **optimal value (marginal) function** $\mu:X\to\overline{\mathbb{R}}$ is defined by
$$
\mu(x):=\inf\{\varphi(x,y)\mid y\in F(x)\}, \qquad x\in X.
$$
We use the convention $\inf(\emptyset):=\infty$, and in the notes it is assumed that $\mu(x)>-\infty$ for all $x\in X$.

The marginal function captures "minimize over $y$ given $x$" and is central in parametric optimization and convex analysis; its convexity is addressed in {{< knowl id="convexity-of-the-marginal-optimal-value-function" text="the convexity theorem for marginal functions" >}}.

**Examples:**
- If $F(x)\equiv C$ is a fixed nonempty set and $\varphi(x,y)=g(x,y)$, then $\mu(x)=\inf_{y\in C} g(x,y)$.
- If $F(x)$ is the feasible set of a constraint system depending on $x$, then $\mu(x)$ is the optimal value of that parameterized problem.
