---
title: "Image"
description: "The set of outputs a function attains on a given subset of inputs"
---

An **image** is the set of values a function takes on a subset of its domain: if $f:A\to B$ is a {{< knowl id="function" text="function" >}} and $S\subseteq A$, then
$$
f(S)=\{f(s): s\in S\}\subseteq B.
$$

The image (often called the range) of $f$ is $f(A)$.

Images are built from {{< knowl id="subset" text="subsets" >}} of the domain and are paired conceptually with {{< knowl id="preimage" text="preimages" >}} of subsets of the codomain. A function is {{< knowl id="surjective-function" text="surjective" >}} precisely when $f(A)$ equals its {{< knowl id="codomain" text="codomain" >}}.

**Examples:**
- For $f:\mathbb{Z}\to\mathbb{Z}$ given by $f(n)=2n$, the image $f(\mathbb{Z})$ is the set $\{2k: k\in\mathbb{Z}\}$ of even integers.
- For $f:\mathbb{R}\to\mathbb{R}$ given by $f(x)=x^2$ and $S=\{x\in\mathbb{R}:-1\le x\le 2\}$, the image is $f(S)=\{y\in\mathbb{R}:0\le y\le 4\}$.
