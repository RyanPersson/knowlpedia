---
title: "Inverse function"
description: "The function that undoes a bijective function."
---

Let $f:X\to Y$ be {{< knowl id="bijective-function" text="bijective" >}}. The **inverse function** of $f$ is the {{< knowl id="function-map" text="function" >}} $f^{-1}:Y\to X$ defined by
$$f^{-1}(y)=x\quad\text{where $x\in X$ is the unique element with }f(x)=y.$$
It satisfies
$$f^{-1}\circ f = \mathrm{id}_X \quad\text{and}\quad f\circ f^{-1}=\mathrm{id}_Y,$$
where $\mathrm{id}_X:X\to X$ is the identity map $\mathrm{id}_X(x)=x$ (see {{< knowl id="composition-of-functions" text="composition" >}}).

Inverse functions are central in analysis: many theorems (e.g., inverse function theorems) give conditions under which a function has a (local) inverse with additional regularity.

**Examples:**
- If $f:\mathbb{R}\to\mathbb{R}$, $f(x)=x+1$, then $f^{-1}(y)=y-1$.
- $\exp:\mathbb{R}\to(0,\infty)$ has inverse $\log:(0,\infty)\to\mathbb{R}$.
- The function $x\mapsto x^2$ has no inverse as a map $\mathbb{R}\to\mathbb{R}$, but it has an inverse on $[0,\infty)$ given by $\sqrt{\cdot}:[0,\infty)\to[0,\infty)$.
