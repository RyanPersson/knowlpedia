---
title: "Frame bundle of a rank-n vector bundle"
description: "The principal bundle whose fiber consists of ordered bases of the fibers of a rank-n vector bundle."
---

Let $\pi:E\to M$ be a smooth real or complex vector bundle of {{< knowl id="rank-of-a-vector-bundle" text="rank" >}} $n$ over a {{< knowl id="smooth-manifold" text="smooth manifold" >}}. The **frame bundle** (or **general linear frame bundle**) of $E$, denoted $\mathrm{Fr}(E)$, is the manifold whose points are ordered bases (frames) of the fibers of $E$:
\[
\mathrm{Fr}(E):=\bigsqcup_{x\in M}\mathrm{Iso}_{\mathbb F}(\mathbb F^n,E_x),
\]
where $\mathrm{Iso}_{\mathbb F}(\mathbb F^n,E_x)$ denotes the set of $\mathbb F$-linear isomorphisms.

There is a natural projection
\[
p:\mathrm{Fr}(E)\to M,\qquad p(u)=x \ \text{if}\ u:\mathbb F^n\to E_x,
\]
and a free right action of the group $\mathrm{GL}(n,\mathbb F)$ given by postcomposition:
\[
u\cdot A := u\circ A,\qquad A\in \mathrm{GL}(n,\mathbb F).
\]

With its standard smooth structure (built from local trivializations of $E$), $(\mathrm{Fr}(E),p)$ is a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure group $\mathrm{GL}(n,\mathbb F)$.

A local frame $(e_1,\dots,e_n)$ over an open set $U$ determines a local section $U\to \mathrm{Fr}(E)$ by sending $x$ to the frame $(e_1(x),\dots,e_n(x))$, and the corresponding changes of local section on overlaps are given by the usual {{< knowl id="transition-matrix-of-a-local-frame" text="transition matrices" >}}.

## Examples
1. **Frame bundle of the tangent bundle.** $\mathrm{Fr}(TM)$ is the bundle of ordered bases of tangent spaces; it is the basic principal bundle underlying many constructions in differential geometry.

2. **Trivial bundle.** If $E\cong M\times \mathbb F^n$, then $\mathrm{Fr}(E)\cong M\times \mathrm{GL}(n,\mathbb F)$ as a principal bundle (a canonical trivialization is obtained from the standard frame of $\mathbb F^n$).

3. **Oriented frame bundle.** If $E$ is an oriented real rank-$n$ bundle, the oriented frames form a subbundle $\mathrm{Fr}^+(E)\subset \mathrm{Fr}(E)$ which is a principal $\mathrm{GL}^+(n,\mathbb R)$-bundle.
