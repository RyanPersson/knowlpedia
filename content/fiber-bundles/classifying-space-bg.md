---
title: "Classifying space BG"
description: "A space whose homotopy classes of maps from a base classify principal G-bundles up to isomorphism."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" >}} (more generally, a reasonable topological group).

## Definition (universal bundle and classifying space)
A **classifying space** $BG$ for $G$ is a space equipped with a principal $G$-bundle
\[
EG \longrightarrow BG
\]
such that:
- $EG$ is contractible, and
- $G$ acts freely on $EG$ with quotient $BG=EG/G$.

The bundle $EG\to BG$ is called the **universal principal $G$-bundle**.

## Classification theorem
If $B$ is a {{< knowl id="paracompact-topological-space" text="paracompact topological space" >}} (in particular, if $B$ is a paracompact smooth manifold), then isomorphism classes of {{< knowl id="principal-g-bundle" text="principal G-bundles" >}} over $B$ are in natural bijection with homotopy classes of maps $[B,BG]$.

Concretely:
- given a map $f:B\to BG$, the pullback bundle $f^*(EG)\to B$ is a principal $G$-bundle;
- every principal $G$-bundle over $B$ is isomorphic to such a pullback for some $f$;
- two maps yield isomorphic bundles if and only if they are homotopic.

Good covers (see {{< knowl id="good-cover" text="good covers" >}}) are often used to build and compare classifying maps via transition functions.

## Examples
1. **Circle bundles.**  
   For $G=U(1)$, one has $BU(1)\simeq \mathbb{CP}^\infty$. The {{< knowl id="hopf-fibration-s3s2-as-a-principal-u-bundle" text="Hopf bundle" >}} over $S^2$ corresponds to a generator of $[S^2,BU(1)]\cong \mathbb Z$.

2. **The Möbius twist via a discrete group.**  
   For $G=\mathbb Z/2$, one has $B(\mathbb Z/2)\simeq \mathbb{RP}^\infty$. The nontrivial element of $[S^1,B(\mathbb Z/2)]\cong \mathbb Z/2$ classifies the principal $\mathbb Z/2$-bundle whose associated line bundle is the Möbius bundle.

3. **Bundles over the circle.**  
   Specializing the classification theorem to $B=S^1$ shows that principal $G$-bundles over the circle are classified by $\pi_0(G)$, matching the explicit {{< knowl id="principal-bundle-over-s1-defined-by-a-clutching-function" text="clutching description" >}} by gluing.
