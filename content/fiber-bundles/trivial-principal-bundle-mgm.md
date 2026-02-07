---
title: "Trivial principal bundle"
description: "The product principal bundle M times G with its standard projection and right action."
---

Let $M$ be a {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let $G$ be a {{< knowl id="lie-group" text="Lie group" >}}. The **trivial principal $G$-bundle** over $M$ is
\[
\pi: M\times G \longrightarrow M,\qquad \pi(x,g)=x,
\]
equipped with the right action
\[
(x,g)\cdot h := (x,gh),\qquad h\in G.
\]

The bundle $M\times G\to M$ is a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}: the action is free and transitive on each fiber, and local trivializations are global (the identity map).

It has a canonical global section
\[
s:M\to M\times G,\qquad s(x)=(x,e),
\]
where $e\in G$ is the identity.

A principal bundle $P\to M$ is called **trivial** if it is isomorphic (as a principal $G$-bundle over $M$) to $M\times G$.

## Examples
1. **Any principal bundle over a contractible base is (often) trivial in practice.**  
   For many Lie groups and typical geometric bases, contractibility of $M$ forces every principal bundle to be trivial; in particular, every principal bundle over $\mathbb R^n$ is trivial.

2. **Gauge transformations are just maps to the group.**  
   Every bundle automorphism of $M\times G$ covering $\mathrm{id}_M$ is of the form
   \[
   \Phi_f(x,g)=(x,f(x)g)
   \]
   for a smooth map $f:M\to G$ (a gauge transformation).

3. **Frame bundles on parallelizable manifolds.**  
   If $M$ admits a global frame of $TM$, then the frame bundle $\mathrm{Fr}(TM)$ is trivial: choosing a global frame identifies it with $M\times \mathrm{GL}(n,\mathbb R)$.
