---
title: "Right principal action"
description: "A smooth right action of a Lie group on a bundle total space that is free and transitive along each fiber."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" >}} and let $\pi:P\to M$ be a surjective submersion of {{< knowl id="smooth-manifold" text="smooth manifolds" >}}.

A **smooth right action** of $G$ on $P$ is a smooth map
\[
R: P\times G \to P,\qquad (p,g)\mapsto p\cdot g
\]
such that for all $p\in P$ and $g,h\in G$:
1. (Identity) $p\cdot e = p$.
2. (Associativity) $(p\cdot g)\cdot h = p\cdot(gh)$.

A smooth right action is called a **right principal action** (relative to $\pi$) if, in addition,
3. (Fiber-preserving) $\pi(p\cdot g)=\pi(p)$ for all $p,g$.
4. (Free) If $p\cdot g=p$, then $g=e$.
5. (Fiberwise transitive) If $\pi(p)=\pi(q)$, then there exists a unique $g\in G$ with $q=p\cdot g$.

Equivalently, the map
\[
P\times G \longrightarrow P\times_M P,\qquad (p,g)\longmapsto (p,\,p\cdot g)
\]
is a {{< knowl id="diffeomorphism" text="diffeomorphism" >}}. When $\pi$ is a surjective submersion and $P$ carries a right principal action, $(P,\pi,M,G)$ is a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}.

## Examples
1. **Trivial principal bundle.** For $P=M\times G$ with $\pi(x,h)=x$, the action $(x,h)\cdot g=(x,hg)$ is right principal.
2. **Frame bundle.** On the frame bundle $\mathrm{Fr}(M)$ of an $n$-manifold, the right action of $GL(n)$ by change of frame is free and transitive on each fiber.
3. **Hopf fibration.** The map $S^3\to S^2$ is a principal $S^1$-bundle, with right action given by complex (or quaternionic) multiplication by elements of $S^1$.
