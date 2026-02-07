---
title: "Inverse function"
description: "A function that undoes a bijective function"
---

An **inverse function** is a function that undoes a bijection: if $f:A\to B$ is a {{< knowl id="bijective-function" text="bijective function" >}}, then its inverse function $f^{-1}:B\to A$ is defined by the rule “$f^{-1}(b)$ is the unique $a\in A$ such that $f(a)=b$”. Equivalently,
$$
f^{-1}\circ f=\mathrm{id}_A\quad\text{and}\quad f\circ f^{-1}=\mathrm{id}_B,
$$

where $\mathrm{id}_A$ and $\mathrm{id}_B$ are {{< knowl id="identity-function" text="identity functions" >}}.

The notation $f^{-1}$ is also used for the {{< knowl id="preimage" text="preimage" >}} of a subset under a function, but that operation is defined even when $f$ is not bijective. Inverse functions are best understood via {{< knowl id="composition" text="composition" >}} and the identity functions they produce.

**Examples:**
- For $f:\mathbb{R}\to\mathbb{R}$ given by $f(x)=x^3$, the inverse function is $f^{-1}(y)=\sqrt[3]{y}$.
- For $f:\mathbb{Z}\to\mathbb{Z}$ given by $f(n)=n+1$, the inverse function is $f^{-1}(m)=m-1$.
