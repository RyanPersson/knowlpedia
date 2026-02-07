---
title: "Basic properties of lim sup and lim inf"
description: "Key identities and inequalities for limsup and liminf of a sequence"
---

**Basic properties of $\limsup$ and $\liminf$**: Let $(a_n)$ be a real sequence and define
$
s_n=\sup_{k\ge n} a_k,\qquad i_n=\inf_{k\ge n} a_k.
$
Then:
- $(s_n)$ is nonincreasing and $(i_n)$ is nondecreasing,
- the limits exist in the extended reals and
  $
  \limsup_{n\to\infty} a_n=\lim_{n\to\infty} s_n,\qquad
  \liminf_{n\to\infty} a_n=\lim_{n\to\infty} i_n,
  $
- always $\liminf a_n\le \limsup a_n$,
- if $\liminf a_n=\limsup a_n=L\in\mathbb{R}$, then $a_n\to L$,
- if $\ell=\limsup a_n$ is finite, then there exists a {{< knowl id="subsequence" text="subsequence" >}} $(a_{n_j})$ with $a_{n_j}\to \ell$ (and similarly for $\liminf$). See {{< knowl id="limit-superior-lim-sup" text="limit superior" >}} and {{< knowl id="limit-inferior-lim-inf" text="limit inferior" >}}.

These facts package the "eventual upper and lower behavior" of a sequence and are used to analyze oscillation and subsequential limits.

**Examples:**
- For $a_n=(-1)^n$, $\limsup a_n=1$ and $\liminf a_n=-1$.
- For $a_n=1+\frac{(-1)^n}{n}$, $\limsup a_n=\liminf a_n=1$, hence $a_n\to 1$.
