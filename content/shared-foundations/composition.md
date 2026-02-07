---
title: "Composition of functions"
description: "Forming a new function by applying one function after another"
---

A **composition of functions** is the function obtained by applying one function after another: if $f:A\to B$ and $g:B\to C$ are {{< knowl id="function" text="functions" >}} (so the codomain of $f$ matches the domain of $g$), then the composition $g\circ f:A\to C$ is defined by
$$
(g\circ f)(a)=g(f(a))\quad\text{for all }a\in A.
$$

Composition is associative when defined, and {{< knowl id="identity-function" text="identity functions" >}} act as identities for composition. If $f$ is {{< knowl id="bijective-function" text="bijective" >}}, then composing with its {{< knowl id="inverse-function" text="inverse function" >}} recovers the appropriate identity functions.

**Examples:**
- Let $f:\mathbb{Z}\to\mathbb{Z}$ be $f(n)=n+1$ and let $g:\mathbb{Z}\to\mathbb{Z}$ be $g(n)=2n$; then $(g\circ f)(n)=2(n+1)=2n+2$.
- If $i:S\to A$ is the inclusion of a {{< knowl id="subset" text="subset" >}} and $f:A\to B$ is any function, then $f\circ i:S\to B$ is the restriction of $f$ to $S$.
