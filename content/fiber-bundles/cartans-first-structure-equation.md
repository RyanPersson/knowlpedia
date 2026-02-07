---
title: "Cartan's first structure equation (torsion) in the frame bundle"
description: "On the frame bundle, the torsion form equals the exterior derivative of the solder form plus the connection form acting on it."
---

Let $M$ be an $n$-dimensional {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let $\pi:F(M)\to M$ denote its (linear) frame bundle, viewed as a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure group $G=\mathrm{GL}(n,\mathbb{R})$. Write a point $u\in F(M)$ over $x=\pi(u)$ as a linear isomorphism $u:\mathbb{R}^n\to T_xM$, where $T_xM$ is the fiber of the {{< knowl id="tangent-bundle" text="tangent bundle" >}}.

## Statement (frame bundle formulation)

There is a canonical $\mathbb{R}^n$-valued $1$-form (the **solder form**) $\theta\in\Omega^1(F(M);\mathbb{R}^n)$ defined by
\[
\theta_u(V)\;=\;u^{-1}\bigl(d\pi_u(V)\bigr),\qquad u\in F(M),\;V\in T_uF(M).
\]

Given a {{< knowl id="principal-connection" text="principal connection" >}} $\omega\in\Omega^1(F(M);\mathfrak{gl}(n,\mathbb{R}))$, define the **torsion $2$-form** $\Theta\in\Omega^2(F(M);\mathbb{R}^n)$ by the covariant exterior derivative of $\theta$:
\[
\Theta \;:=\; D\theta.
\]
Then **Cartan’s first structure equation** is the identity
\[
\boxed{\;\Theta \;=\; d\theta \;+\; \omega\wedge \theta\;}
\]
where the $\mathfrak{gl}(n,\mathbb{R})$-action on $\mathbb{R}^n$ is used to define $\omega\wedge\theta$:
\[
(\omega\wedge\theta)(V,W)\;=\;\omega(V)\cdot\theta(W)\;-\;\omega(W)\cdot\theta(V).
\]

The form $\Theta$ is horizontal and $G$-equivariant; it corresponds to the torsion tensor of the induced linear connection $\nabla$ on $TM$, namely
\[
T_\nabla(X,Y)=\nabla_XY-\nabla_YX-[X,Y],
\]
where $[X,Y]$ is the {{< knowl id="lie-bracket" text="Lie bracket" >}} of vector fields. In particular, $\nabla$ is torsion-free if and only if $\Theta=0$, equivalently
\[
d\theta+\omega\wedge\theta=0.
\]

## Examples

1. **Euclidean space with the standard flat connection.**  
   On $M=\mathbb{R}^n$ with its global coordinate frame, the induced connection has $\omega=0$ in that frame and $\theta$ pulls back to the standard coframe. Hence $d\theta=0$ and $\Theta=0$.

2. **Levi-Civita connection (torsion-free case).**  
   For a Riemannian manifold, the Levi-Civita connection is torsion-free, so in any local orthonormal coframe $\{\theta^i\}$ with connection $1$-forms $\{\omega^i{}_j\}$ one has the classical component form
   \[
   d\theta^i+\omega^i{}_j\wedge\theta^j=0,
   \]
   which is exactly $\Theta=0$ expressed using the first structure equation.

3. **Teleparallel (Weitzenböck) connection on a Lie group.**  
   Let $M=G$ be a {{< knowl id="lie-group" text="Lie group" >}} with a global left-invariant frame. The connection for which that frame is parallel has $\omega=0$ in that trivialization, but typically $d\theta\neq 0$ for the left-invariant coframe. Then $\Theta=d\theta$ encodes the structure constants of the corresponding {{< knowl id="lie-algebra" text="Lie algebra" section="lie-groups">}}.
