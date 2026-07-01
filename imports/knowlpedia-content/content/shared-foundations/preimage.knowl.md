+++
id = "shared-foundations/preimage"
title = "Preimage"
kind = "knowl"
summary = "The set of inputs that a function sends into a specified subset of its codomain"
aliases = ["preimage"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/preimage.md"
+++

A **preimage** is the set of inputs that map into a given subset of the codomain: if $f:A\to B$ is a [[shared-foundations/function|function]] and $T\subseteq B$, then
$$
f^{-1}(T)=\{a\in A: f(a)\in T\}\subseteq A.
$$

Unlike an [[shared-foundations/inverse-function|inverse function]], the preimage $f^{-1}(T)$ is defined for every function and every [[shared-foundations/subset|subset]] $T$ of the codomain. Preimages interact well with set operations such as [[shared-foundations/union|union]] and [[shared-foundations/intersection|intersection]].

**Examples:**
- For $f:\mathbb{R}\to\mathbb{R}$ given by $f(x)=x^2$, the preimage of $\{1\}$ is $f^{-1}(\{1\})=\{-1,1\}$.
- For $p:\mathbb{Z}\to\{0,1\}$ defined by parity, the preimage $p^{-1}(\{0\})$ is the set $\{2k:k\in\mathbb{Z}\}$ of even integers.
