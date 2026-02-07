---
title: "Theorem: Existence and uniqueness of horizontal lifts of curves"
description: "Given a connection, any curve in the base has a unique horizontal lift through a chosen point in the fiber."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with a {{< knowl id="principal-connection" text="principal connection" >}} $\omega$, and let $H=\ker(\omega)\subset TP$ be its horizontal distribution.

Let $\gamma:[a,b]\to M$ be a smooth curve, and choose a point $p_0\in P$ with $\pi(p_0)=\gamma(a)$.

## Theorem

There exists a unique smooth curve $\widetilde\gamma:[a,b]\to P$ such that:

1. $\pi\circ \widetilde\gamma=\gamma$,
2. $\widetilde\gamma(a)=p_0$,
3. $\dot{\widetilde\gamma}(t)\in H_{\widetilde\gamma(t)}$ for all $t$ (i.e. $\widetilde\gamma$ is horizontal).

Moreover, the lift depends smoothly on $(\gamma,p_0)$ under smooth variations.

## Remarks

- In a local trivialization $P|_U\cong U\times G$, the horizontality condition becomes an ODE in $G$ driven by the local connection $1$-form, so existence and uniqueness follow from standard ODE theory.
- Horizontal lifting is the basic input for {{< knowl id="parallel-transport" text="parallel transport" >}} on principal and associated bundles.

## Examples

1. **Trivial bundle with connection form.** For $P=M\times G$ and a connection given by a $\mathfrak g$-valued $1$-form $A$ on $M$, writing $\widetilde\gamma(t)=(\gamma(t),g(t))$, horizontality is
   \[
   g(t)^{-1}\dot g(t) = -A_{\gamma(t)}(\dot\gamma(t)),
   \]
   an ODE with unique solution given $g(a)$.

2. **Product (flat) connection.** If $A=0$, then the equation is $\dot g(t)=0$, so the horizontal lift is simply $(\gamma(t),g_0)$: constant group component.

3. **Circle bundles.** For a principal $U(1)$-bundle with a connection $1$-form, horizontal lifts of closed curves encode holonomy as a phase factor; this is the simplest instance of connection-induced transport.
