---
title: "Class C^k map"
description: "A map with continuous partial derivatives up to order k."
tags: ["needs-review"]
---

A **class $C^k$ map** is a {{< knowl id="function" section="shared-foundations" text="function" >}} $F:U\to\mathbb{R}^m$ defined on an open set $U\subseteq\mathbb{R}^n$ such that all partial derivatives of $F$ of total order at most $k$ exist on $U$ and are continuous on $U$ (with order $0$ meaning $F$ itself).

When $k=1$, this is the standard “continuously differentiable” hypothesis in multivariable calculus: the derivative is encoded by the {{< knowl id="jacobian-matrix" text="Jacobian matrix" >}}, and $C^1$ regularity is closely aligned with having a continuous {{< knowl id="frechet-derivative" text="Fréchet derivative" >}}. Higher regularity interacts with mixed derivatives via results like the {{< knowl id="schwarz-clairaut-theorem" text="Schwarz–Clairaut theorem" >}}.

**Examples:**
- The map $F(x,y)=(x^2+y,\;xy)$ is class $C^\infty$ on $\mathbb{R}^2$.
- The map $F(x,y)=(|x|,\;y)$ is class $C^0$ on $\mathbb{R}^2$ but not class $C^1$ along the line $x=0$.
