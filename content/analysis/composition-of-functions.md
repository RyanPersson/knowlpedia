---
title: "Composition of functions"
description: "The function obtained by applying one function after another."
---

Let $f:X\to Y$ and $g:Y\to Z$ be functions. The **composition** of $g$ with $f$ is the function
$$g\circ f:X\to Z,\qquad (g\circ f)(x):=g(f(x)).$$

Composition formalizes successive application of maps and is the basic operation for building new functions from old ones. In analysis, the chain rule concerns derivatives of compositions, and continuity is stable under composition.

**Examples:**
- If $f:\mathbb{R}\to\mathbb{R}$, $f(x)=x^2$ and $g:\mathbb{R}\to\mathbb{R}$, $g(y)=y+1$, then $(g\circ f)(x)=x^2+1$.
- If $f:\mathbb{R}\to(0,\infty)$ is $f(x)=e^x$ and $g:(0,\infty)\to\mathbb{R}$ is $g(y)=\log y$, then $g\circ f=\mathrm{id}_{\mathbb{R}}$.
- Composition is only defined when the codomain of $f$ matches the domain of $g$ (or at least $f(X)\subseteq \mathrm{dom}(g)$ if one allows partial maps).
