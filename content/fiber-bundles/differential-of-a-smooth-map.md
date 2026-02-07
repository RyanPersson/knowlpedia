---
title: "Differential of a smooth map"
description: "The linear map between tangent spaces induced by a smooth map, also called the pushforward."
---

Let $f:M\to N$ be a {{< knowl id="smooth-map" text="smooth map" >}} between smooth manifolds, and let $p\in M$. The **differential** (or **pushforward**) of $f$ at $p$ is the linear map
\[
\mathrm{d}f_p:T_pM\longrightarrow T_{f(p)}N
\]
between tangent spaces (equivalently, between the fibers of the {{< knowl id="tangent-bundle" text="tangent bundle" >}}) characterized as follows.

Choose {{< knowl id="smooth-chart" text="smooth charts" >}} $(U,\varphi)$ around $p$ and $(V,\psi)$ around $f(p)$ with $f(U)\subset V$. Writing $\psi\circ f\circ\varphi^{-1}:\varphi(U)\to\psi(V)$ as a smooth map between open subsets of Euclidean space, $\mathrm{d}f_p$ is the unique linear map whose matrix in these coordinates is the Jacobian of $\psi\circ f\circ\varphi^{-1}$ at $\varphi(p)$. This definition is independent of the chosen charts.

The differential is functorial: if $g:N\to P$ is smooth, then
\[
\mathrm{d}(g\circ f)_p=\mathrm{d}g_{f(p)}\circ \mathrm{d}f_p,
\qquad
\mathrm{d}(\mathrm{id}_M)_p=\mathrm{id}_{T_pM}.
\]

## Examples
1. **A coordinate computation.** For $f:\mathbb{R}^2\to\mathbb{R}$, $f(x,y)=x^2y$, the differential at $(x,y)$ is the linear functional
   \[
   \mathrm{d}f_{(x,y)}(u,v)=(2xy)u+(x^2)v.
   \]
2. **Projection.** For $\pi:M\times F\to M$, the differential at $(m,f)$ is the projection $\mathrm{d}\pi_{(m,f)}:T_mM\oplus T_fF\to T_mM$ onto the first factor.
3. **Left translation on a Lie group.** If $G$ is a {{< knowl id="lie-group" text="Lie group" >}} and $L_g:G\to G$ is left translation by $g$, then $\mathrm{d}(L_g)_h:T_hG\to T_{gh}G$ is a linear isomorphism for every $h\in G$ (in fact $L_g$ is a diffeomorphism).
