+++
id = "shared-foundations/surjective-function"
title = "Surjective function"
kind = "knowl"
summary = "A function whose outputs cover the entire codomain"
aliases = ["surjective-function", "Surjective function"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/surjective-function.md"
+++

A **surjective function** is a [[shared-foundations/function|function]] $f:A\to B$ such that for every $b\in B$ there exists at least one $a\in A$ with $f(a)=b$.

Surjectivity can be expressed using the [[shared-foundations/image|image]]: $f$ is surjective exactly when $f(A)$ equals its [[shared-foundations/codomain|codomain]] $B$. Surjectivity is one of the two conditions (along with injectivity) needed for a [[shared-foundations/bijective-function|bijection]].

**Examples:**
- The function $f:\mathbb{R}\to\mathbb{R}$ given by $f(x)=x^3$ is surjective, since every real number has a real cube root.
- The parity map $p:\mathbb{Z}\to\{0,1\}$ (even $\mapsto 0$, odd $\mapsto 1$) is surjective.
