---
title: "Trivial vector bundle"
description: "The product bundle M times V with constant fiber V and a global frame of constant sections."
---

Let $M$ be a {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let $V$ be a finite-dimensional real vector space.

The **trivial vector bundle with fiber $V$** is the projection
\[
\pi: M\times V \longrightarrow M,\qquad \pi(x,v)=x,
\]
with fiberwise vector space operations
\[
(x,v)+(x,w)=(x,v+w),\qquad \lambda(x,v)=(x,\lambda v).
\]
It is a smooth vector bundle of rank $\dim V$. A section of $M\times V$ is the same thing as a smooth map $s:M\to V$.

The bundle admits a global frame: choosing a basis $(e_1,\dots,e_k)$ of $V$ yields sections $s_i(x)=(x,e_i)$ that span each fiber.

The trivial bundle is the vector-bundle analogue of the {{< knowl id="trivial-principal-bundle-mgm" text="trivial principal bundle" >}}.

## Examples
1. **Euclidean tangent bundle.**  
   The {{< knowl id="tangent-bundle" text="tangent bundle" >}} of $\mathbb R^n$ is trivial: $T\mathbb R^n\cong \mathbb R^n\times \mathbb R^n$ using the standard coordinate vector fields.

2. **Product bundles.**  
   For any manifold $M$ and any $k$, the bundle $M\times\mathbb R^k\to M$ is the standard rank-$k$ trivial bundle; its sections are $k$-tuples of smooth functions on $M$.

3. **Connections on trivial bundles.**  
   A {{< knowl id="connection-on-a-vector-bundle" text="connection on a vector bundle" >}} on $M\times V$ can be written globally in a chosen basis as $\nabla=d+A$, where $A$ is a matrix of 1-forms on $M$.
