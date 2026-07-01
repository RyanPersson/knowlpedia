+++
id = "shared-foundations/composition"
title = "Composition of functions"
kind = "knowl"
summary = "Forming a new function by applying one function after another"
aliases = ["composition", "Composition of functions"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/composition.md"
+++

A **composition of functions** is the function obtained by applying one function after another: if $f:A\to B$ and $g:B\to C$ are [[shared-foundations/function|functions]] (so the codomain of $f$ matches the domain of $g$), then the composition $g\circ f:A\to C$ is defined by
$$
(g\circ f)(a)=g(f(a))\quad\text{for all }a\in A.
$$

Composition is associative when defined, and [[shared-foundations/identity-function|identity functions]] act as identities for composition. If $f$ is [[shared-foundations/bijective-function|bijective]], then composing with its [[shared-foundations/inverse-function|inverse function]] recovers the appropriate identity functions.

**Examples:**
- Let $f:\mathbb{Z}\to\mathbb{Z}$ be $f(n)=n+1$ and let $g:\mathbb{Z}\to\mathbb{Z}$ be $g(n)=2n$; then $(g\circ f)(n)=2(n+1)=2n+2$.
- If $i:S\to A$ is the inclusion of a [[shared-foundations/subset|subset]] and $f:A\to B$ is any function, then $f\circ i:S\to B$ is the restriction of $f$ to $S$.
