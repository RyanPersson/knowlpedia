---
title: "Preimage (inverse image)"
description: "The set of inputs that a function maps into a given subset of the codomain."
---

Let $f:X\to Y$ be a function and let $B\subseteq Y$. The **preimage** (or **inverse image**) of $B$ under $f$ is
$$f^{-1}(B):=\{x\in X : f(x)\in B\}\subseteq X.$$

The notation $f^{-1}(B)$ does not require $f$ to be invertible; it is defined for every function. Preimages interact well with set operations and are central in topology (continuity via preimages of open sets) and measure theory (measurability via preimages of measurable sets).

**Examples:**
- If $f:\mathbb{R}\to\mathbb{R}$, $f(x)=x^2$, then $f^{-1}(\{1\})=\{-1,1\}$.
- For the same $f$, $f^{-1}((-\infty,1])=[-1,1]$.
- If $f(x)=x^2$, then $f^{-1}((-1,0))=\varnothing$ since $x^2\ge 0$ for all $x\in\mathbb{R}$.
