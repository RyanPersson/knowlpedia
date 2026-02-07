---
title: "Horizontal lift of curves and uniqueness"
description: "Existence and uniqueness of the horizontal lift of a base curve for a given starting point in the total space."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} equipped with a {{< knowl id="principal-connection" text="principal connection" >}} $\omega$, and let $H:=\ker\omega\subset TP$ be its horizontal distribution.

A smooth curve $\widetilde\gamma:I\to P$ is **horizontal** if $\omega(\dot{\widetilde\gamma}(t))=0$ for all $t\in I$ (equivalently, $\dot{\widetilde\gamma}(t)\in H_{\widetilde\gamma(t)}$).

**Theorem (horizontal lifting).** Let $\gamma:I\to M$ be a smooth curve and fix $t_0\in I$ and $p_0\in P$ with $\pi(p_0)=\gamma(t_0)$. Then there exists a unique horizontal curve $\widetilde\gamma:I\to P$ such that
\[
\pi\circ \widetilde\gamma = \gamma,\qquad \widetilde\gamma(t_0)=p_0.
\]
Equivalently, $\widetilde\gamma$ is the unique solution to the first-order ODE requiring that $d\pi(\dot{\widetilde\gamma})=\dot\gamma$ and $\dot{\widetilde\gamma}$ lies in the horizontal subspace.

This construction is the input for defining {{< knowl id="parallel-transport" text="parallel transport" >}} on principal and associated bundles.

## Examples
1. If $P=M\times G$ is trivial and $\omega$ is given by a local gauge potential $A$ on $M$, then the horizontal lift equation becomes an ODE for a curve in $G$ driven by $A(\dot\gamma)$.
2. For the orthonormal frame bundle of a Riemannian manifold with Levi-Civita connection, horizontal lifts are precisely parallel frames along $\gamma$.
3. If $\gamma$ is constant, the unique horizontal lift with initial value $p_0$ is the constant curve at $p_0$.
