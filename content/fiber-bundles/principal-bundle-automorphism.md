---
title: "Principal bundle automorphism"
description: "A principal bundle isomorphism from a principal bundle to itself, possibly covering a nontrivial base diffeomorphism."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}.

A **principal bundle automorphism** is a {{< knowl id="principal-bundle-isomorphism" text="principal bundle isomorphism" >}} $\Phi:P\to P$ (so $\Phi$ is an equivariant diffeomorphism) covering a base {{< knowl id="diffeomorphism" text="diffeomorphism" >}} $f:M\to M$, meaning
\[
\pi\circ \Phi = f\circ \pi
\quad\text{and}\quad
\Phi(p\cdot g)=\Phi(p)\cdot g.
\]
The automorphisms of $P$ form a group under composition, often denoted $\mathrm{Aut}(P)$. The subgroup consisting of automorphisms with $f=\mathrm{id}_M$ is the group of {{< knowl id="gauge-transformation" text="gauge transformations" >}}.

## Examples
1. **Automorphisms of a trivial bundle.** If $P=M\times G$, any pair consisting of a diffeomorphism $f:M\to M$ and a smooth map $a:M\to G$ defines
   \[
   \Phi(x,h)=(f(x),\,a(x)\,h),
   \]
   which is equivariant and hence an automorphism.
2. **Lift of a base diffeomorphism to frames.** A diffeomorphism $f:M\to M$ acts on the frame bundle by sending a frame at $x$ to its pushforward frame at $f(x)$; this is a principal bundle automorphism.
3. **Central right multiplication.** If $z$ lies in the center of $G$, then $\Phi(p)=p\cdot z$ is equivariant and defines an automorphism covering $\mathrm{id}_M$.
