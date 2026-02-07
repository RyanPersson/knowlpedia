---
title: "Solder form on the frame bundle"
description: "The canonical R^n-valued 1-form on the frame bundle that identifies horizontal directions with tangent vectors on the base."
---

Let $M$ be an $n$-dimensional {{< knowl id="smooth-manifold" text="smooth manifold" >}}. Its (linear) frame bundle $FM$ is the set of pairs $(x,u)$ where $x\in M$ and $u\colon \mathbb{R}^n\to T_xM$ is a linear isomorphism. The projection $\pi\colon FM\to M$ makes $FM$ a {{< knowl id="principal-g-bundle" text="principal bundle" >}} with structure group $GL(n,\mathbb{R})$ acting by right composition on frames.

## Definition (Solder form / tautological 1-form)
The **solder form** on $FM$ is the $\mathbb{R}^n$-valued {{< knowl id="differential-k-form" text="1-form" >}}
\[
\theta \in \Omega^1(FM;\mathbb{R}^n)
\]
defined by
\[
\theta_u(v) := u^{-1}\bigl(d\pi_u(v)\bigr), \qquad u\in FM,\; v\in T_uFM.
\]

Equivalently: $\theta$ “measures” the base component of a tangent vector to $FM$ and expresses it in the moving frame $u$.

The solder form satisfies two fundamental properties:

1. **Semibasic:** $\theta$ vanishes on vertical tangent vectors (those in $\ker(d\pi)$).
2. **Equivariance:** for $A\in GL(n,\mathbb{R})$ and the right action $R_A\colon FM\to FM$, one has
   \[
   (R_A)^*\theta = A^{-1}\theta.
   \]

A local section $s\colon U\to FM$ (a local frame) pulls back $\theta$ to a coframing on $U$, i.e. an identification $TU\cong U\times \mathbb{R}^n$ compatible with the {{< knowl id="tangent-bundle" text="tangent bundle" >}}.

## Examples
1. **Euclidean space.** On $M=\mathbb{R}^n$ with the global frame $s(x)=\mathrm{id}_{\mathbb{R}^n}$, one has $s^*\theta = (dx^1,\dots,dx^n)$.
2. **Orthonormal frame bundle.** If $M$ is Riemannian, restricting $FM$ to orthonormal frames yields a principal $O(n)$-bundle; the same formula defines the solder form on this subbundle.
3. **Pullback to a moving frame.** On any coordinate chart $U\subset M$, taking $s$ to be the coordinate frame gives $s^*\theta$ equal to the usual coordinate coframe, showing that $\theta$ globalizes the local “$dx$” data.
