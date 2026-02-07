---
title: "Preimage"
description: "The set of inputs that a function sends into a specified subset of its codomain"
---

A **preimage** is the set of inputs that map into a given subset of the codomain: if $f:A\to B$ is a {{< knowl id="function" text="function" >}} and $T\subseteq B$, then
$$
f^{-1}(T)=\{a\in A: f(a)\in T\}\subseteq A.
$$

Unlike an {{< knowl id="inverse-function" text="inverse function" >}}, the preimage $f^{-1}(T)$ is defined for every function and every {{< knowl id="subset" text="subset" >}} $T$ of the codomain. Preimages interact well with set operations such as {{< knowl id="union" text="union" >}} and {{< knowl id="intersection" text="intersection" >}}.

**Examples:**
- For $f:\mathbb{R}\to\mathbb{R}$ given by $f(x)=x^2$, the preimage of $\{1\}$ is $f^{-1}(\{1\})=\{-1,1\}$.
- For $p:\mathbb{Z}\to\{0,1\}$ defined by parity, the preimage $p^{-1}(\{0\})$ is the set $\{2k:k\in\mathbb{Z}\}$ of even integers.
