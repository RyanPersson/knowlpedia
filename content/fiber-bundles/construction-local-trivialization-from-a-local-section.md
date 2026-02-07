---
title: "Construction: local trivialization from a local section"
description: "A local section of a principal bundle determines a canonical local trivialization by multiplying by group elements."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with right action $(p,g)\mapsto p\cdot g$. Let $U\subset M$ be open and let $s:U\to P$ be a smooth local section, i.e. $\pi\circ s=\mathrm{id}_U$.

## Construction (Trivialization determined by a section)
Define a map
\[
\Phi_s:U\times G\longrightarrow \pi^{-1}(U),
\qquad
(x,g)\longmapsto s(x)\cdot g.
\]
Then $\Phi_s$ is a diffeomorphism with inverse given by
\[
p\in \pi^{-1}(U)\longmapsto \big(\pi(p),\ g_s(p)\big),
\]
where $g_s(p)\in G$ is the unique element satisfying $p=s(\pi(p))\cdot g_s(p)$.

Moreover, $\Phi_s$ is $G$-equivariant for the right action on $\pi^{-1}(U)$ and the right action on $U\times G$ given by $(x,g)\cdot h=(x,gh)$.

This is the standard way local trivializations are produced and is the starting point for defining local connection forms and curvature.

## Examples
1. **Trivial bundle.** For $P=M\times G$ with section $s(x)=(x,e)$, the map $\Phi_s$ is the identity $U\times G\to U\times G$.

2. **From a local frame.** If $P$ is the frame bundle of a vector bundle $E\to M$, then a local frame on $U$ is exactly a local section $s:U\to P$, and $\Phi_s$ identifies frames over $U$ with $U\times GL(n)$.

3. **Local connection 1-form.** Given a principal connection $\omega$ on $P$, the local connection form is $A=s^*\omega\in\Omega^1(U;\mathfrak g)$; the curvature pulls back to $F=s^*\Omega$ satisfying the identity in {{< knowl id="convention-local-curvature-convention-f-da-aa" text="the local curvature convention" >}}.
