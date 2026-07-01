+++
id = "shared-foundations/identity-function"
title = "Identity function"
kind = "knowl"
summary = "The function that maps every element of a set to itself"
aliases = ["identity-function", "Identity function"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/identity-function.md"
+++

An **identity function** on a set $A$ is the [[shared-foundations/function|function]] $\mathrm{id}_A:A\to A$ defined by
$$
\mathrm{id}_A(a)=a\quad\text{for all }a\in A.
$$

Identity functions are neutral elements for [[shared-foundations/composition|composition]]: if $f:A\to B$ is any function, then $f\circ \mathrm{id}_A=f$ and $\mathrm{id}_B\circ f=f$. The identity function is always [[shared-foundations/bijective-function|bijective]], and its [[shared-foundations/inverse-function|inverse function]] is itself.

**Examples:**
- On [[shared-foundations/real-numbers|the real numbers]], $\mathrm{id}_{\mathbb{R}}(x)=x$ for all $x\in\mathbb{R}$.
- On the [[shared-foundations/power-set|power set]] $\mathcal{P}(A)$ of a set $A$, the identity function sends each subset $S\subseteq A$ to itself.
