---
title: "Equivariant local trivialization"
description: "A local trivialization of a principal bundle that intertwines the right group action with right multiplication on the model fiber."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with {{< knowl id="right-principal-action" text="right principal action" >}} $(p,g)\mapsto p\cdot g$, and let $U\subset M$ be open (often chosen from an {{< knowl id="open-cover" text="open cover" section="topology">}} of $M$).

An **equivariant local trivialization** of $P$ over $U$ is a {{< knowl id="diffeomorphism" text="diffeomorphism" >}}
\[
\psi:\pi^{-1}(U)\to U\times G
\]
such that:
1. (Covers the identity on $U$) $\mathrm{pr}_1\circ\psi=\pi$ on $\pi^{-1}(U)$.
2. (Equivariance) For all $p\in\pi^{-1}(U)$ and $g\in G$,
   \[
   \psi(p\cdot g)=\psi(p)\cdot g,
   \]
   where the right action on $U\times G$ is $(x,h)\cdot g=(x,hg)$.

Given such a $\psi$, the map
\[
s:U\to P,\qquad s(x)=\psi^{-1}(x,e)
\]
is a smooth local section, and every $p\in\pi^{-1}(U)$ can be written uniquely as $p=s(\pi(p))\cdot g$.

## Examples
1. **Trivial bundle.** For $P=M\times G$, the identity map $\psi(x,h)=(x,h)$ is an equivariant local trivialization over any open $U\subset M$.
2. **Frame bundle from a local frame.** If $(X_1,\dots,X_n)$ is a smooth frame of $TM$ on $U$, then every frame at $x\in U$ is uniquely $X(x)\cdot A$ for $A\in GL(n)$, giving an equivariant trivialization of $\mathrm{Fr}(M)|_U$.
3. **Hopf fibration charts.** The Hopf bundle $S^3\to S^2$ admits two standard trivializations over the complements of the north and south poles, each intertwining the $S^1$-action with multiplication on the fiber.
