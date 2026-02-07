---
title: "Theorem: Pullback of a principal connection is a principal connection"
description: "A principal connection pulls back along a smooth map to a canonical connection on the pullback bundle."
---

Let $f:N\to M$ be a {{< knowl id="smooth-map" text="smooth map" >}} and let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with a {{< knowl id="principal-connection" text="principal connection" >}} $\omega$.

Let $\mathrm{pr}_P:f^*P\to P$ denote the projection from the pullback bundle $f^*P\subset N\times P$ onto the second factor.

## Theorem (pullback connection)

There is a unique principal connection $f^*\omega$ on $f^*P\to N$ characterized by either of the equivalent descriptions:

1. **By connection 1-forms:** the connection form on $f^*P$ is $(\mathrm{pr}_P)^*\omega\in\Omega^1(f^*P;\mathfrak g)$.

2. **By horizontal subspaces:** for $(n,p)\in f^*P$, the horizontal subspace is
   \[
   H_{(n,p)} := \{\,v\in T_{(n,p)}(f^*P)\mid d(\mathrm{pr}_P)(v)\in H_p\,\},
   \]
   where $H_p\subset T_pP$ is the horizontal subspace of $\omega$ at $p$.

In either description, $f^*\omega$ is $G$-equivariant and reproduces fundamental vector fields, hence is a principal connection.

Its {{< knowl id="curvature" text="curvature" >}} satisfies $\mathrm{pr}_P^*(\Omega)=\Omega_{f^*\omega}$, i.e. curvature pulls back under $\mathrm{pr}_P$.

## Examples

1. **Restriction of a connection.** If $i:Z\hookrightarrow M$ is an embedding, then $i^*\omega$ is the restriction of $\omega$ to the restricted bundle $P|_Z$.

2. **Pullback along a parametrized curve.** If $\gamma:[0,1]\to M$, then $\gamma^*P\to[0,1]$ carries the pulled-back connection $\gamma^*\omega$; horizontal sections of $\gamma^*P$ are precisely horizontal lifts of $\gamma$ in $P$.

3. **Trivial bundle picture.** For $P=M\times G$ with connection form determined by a $\mathfrak g$-valued $1$-form $A$ on $M$, the pullback connection on $N\times G$ corresponds to the pulled-back form $f^*A$ on $N$.
