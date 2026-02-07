---
title: "Jet bundle (first jets of sections)"
description: "A bundle whose points record the value and first derivative of a local section at a basepoint."
---

Let $\pi\colon E\to M$ be a smooth fiber bundle over a {{< knowl id="smooth-manifold" text="smooth manifold" >}}.

## Definition (1-jet of a section)
Let $x\in M$. Two smooth local sections $s,t\colon U\to E$ (with $x\in U$) are **1-jet equivalent at $x$** if:

1. $s(x)=t(x)$, and
2. in any local trivialization of $E$ near $x$, their first derivatives at $x$ agree.

The equivalence class of $s$ is denoted $j_x^1 s$ and is called the **1-jet of $s$ at $x$**.

## Definition (1-jet bundle)
The **1-jet bundle** $J^1E$ is the set of all 1-jets $j_x^1 s$ of local sections, with the smooth structure making the projection
\[
\pi_{1,0}\colon J^1E \to E,\qquad j_x^1 s \mapsto s(x),
\]
a smooth fiber bundle over $E$, and the composite $\pi\circ \pi_{1,0}\colon J^1E\to M$ a smooth fiber bundle over $M$.

The fiber of $J^1E\to M$ at $x$ encodes “value + first derivative” data at $x$. More precisely, $J^1E\to E$ is an affine bundle modeled on $\mathrm{Hom}(T_xM, V_eE)$, where $T_xM$ is the {{< knowl id="tangent-bundle" text="tangent space" >}} and $V_eE$ is the vertical tangent space at $e\in E_x$.

A fundamental application is that for a principal bundle $P\to M$, the quotient $J^1P/G$ is the {{< knowl id="bundle-of-connections" text="bundle of connections" >}}.

## Examples
1. **Jets of functions.** For the trivial real line bundle $E=M\times \mathbb{R}$, a section is a function $f\colon M\to \mathbb{R}$, and $j_x^1 f$ is determined by $(f(x), df_x)$. Thus $J^1(M\times \mathbb{R})$ identifies with $M\times \mathbb{R}\times T_x^*M$.
2. **Trivial bundle with fiber F.** For $E=M\times F$, a section is a map $f\colon M\to F$, and $j_x^1 f$ records $(x, f(x), df_x)$.
3. **Local coordinate description.** In coordinates $(x^i)$ on $M$ and fiber coordinates $(y^\alpha)$ on $E$, a jet is described by $(x^i, y^\alpha, y^\alpha_i)$, where $y^\alpha_i$ represent the first partial derivatives of the section components.
