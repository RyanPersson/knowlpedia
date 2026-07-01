+++
id = "shared-foundations/image"
title = "Image"
kind = "knowl"
summary = "The set of outputs a function attains on a given subset of inputs"
aliases = ["image"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/image.md"
+++

An **image** is the set of values a function takes on a subset of its domain: if $f:A\to B$ is a [[shared-foundations/function|function]] and $S\subseteq A$, then
$$
f(S)=\{f(s): s\in S\}\subseteq B.
$$

The image (often called the range) of $f$ is $f(A)$.

Images are built from [[shared-foundations/subset|subsets]] of the domain and are paired conceptually with [[shared-foundations/preimage|preimages]] of subsets of the codomain. A function is [[shared-foundations/surjective-function|surjective]] precisely when $f(A)$ equals its [[shared-foundations/codomain|codomain]].

**Examples:**
- For $f:\mathbb{Z}\to\mathbb{Z}$ given by $f(n)=2n$, the image $f(\mathbb{Z})$ is the set $\{2k: k\in\mathbb{Z}\}$ of even integers.
- For $f:\mathbb{R}\to\mathbb{R}$ given by $f(x)=x^2$ and $S=\{x\in\mathbb{R}:-1\le x\le 2\}$, the image is $f(S)=\{y\in\mathbb{R}:0\le y\le 4\}$.
