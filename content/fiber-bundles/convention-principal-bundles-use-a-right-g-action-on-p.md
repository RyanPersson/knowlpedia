---
title: "Convention: principal bundles use a right G-action on P"
description: "A principal G-bundle is written with a right action of G on the total space, matching standard connection and equivariance formulas."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" >}}.

## Convention
A {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} is a fiber bundle $\pi:P\to M$ equipped with a **right** smooth action
\[
R: P\times G\to P,\qquad (p,g)\mapsto p\cdot g,
\]
which is free and fiberwise transitive, with $M\cong P/G$.

All equivariance conditions are written with respect to this right action. In particular, for a {{< knowl id="principal-connection" text="principal connection" >}} 1-form $\omega\in\Omega^1(P;\mathfrak g)$ and for $g\in G$, we use
\[
(R_g)^*\omega=\mathrm{Ad}(g^{-1})\,\omega,
\]
and the induced vertical identification uses fundamental vector fields defined from the right action (see {{< knowl id="convention-fundamental-vector-field-x-is-defined-using-the-right-action" text="fundamental vector field convention" >}}).

This convention fixes the sign choices appearing in curvature and covariant differentiation identities.

## Examples
1. **Frame bundle.** For a rank-$n$ vector bundle $E\to M$, the bundle of frames $P=\mathrm{Fr}(E)$ carries a natural right $GL(n,\mathbb R)$-action by postcomposition of frames, $(u,g)\mapsto u\circ g$.

2. **Transition functions from local sections.** With right actions, if $s_i,s_j:U\to P$ are local sections, the transition map $g_{ij}:U\to G$ is defined by $s_j=s_i\cdot g_{ij}$ (see {{< knowl id="construction-transition-functions-g-iju-iu-jg-from-local-sections" text="transition functions from local sections" >}}).

3. **Gauge transformations.** A gauge transformation is typically a $G$-equivariant diffeomorphism $\Phi:P\to P$ commuting with the right action; writing the action on the right makes $\Phi(p\cdot g)=\Phi(p)\cdot g$ the natural equivariance condition.
