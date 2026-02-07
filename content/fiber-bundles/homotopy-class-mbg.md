---
title: "Homotopy class [M,BG]"
description: "The set of homotopy classes of continuous maps from a manifold M to the classifying space BG."
---

Let $M$ be a {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let $BG$ be the classifying space associated to a {{< knowl id="lie-group" text="Lie group" >}} $G$.

## Definition (Homotopy classes of maps into BG)
The notation **[M,BG]** denotes the set of (unbased) homotopy classes of continuous maps $f\colon M\to BG$.

Concretely, two maps $f_0,f_1\colon M\to BG$ define the same element of [M,BG] if there exists a continuous homotopy
\[
H\colon M\times [0,1] \to BG,\qquad H(\cdot,0)=f_0,\; H(\cdot,1)=f_1.
\]

If $\phi\colon M'\to M$ is a {{< knowl id="diffeomorphism" text="diffeomorphism" >}}, then precomposition induces a bijection
\[
[M,BG] \xrightarrow{\;\cong\;} [M',BG], \quad [f]\mapsto [f\circ \phi].
\]

This set is the target of the classification map sending a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} $P\to M$ to the homotopy class of its {{< knowl id="classifying-map-of-a-principal-bundle" text="classifying map" >}}.

## Examples
1. **Spheres.** For $M=S^n$, there is a canonical identification [S^n,BG] $\cong \pi_n(BG)$.
2. **Contractible bases.** If $M$ is contractible, then [M,BG] has exactly one element (every map is homotopic to a constant map).
3. **Line bundles.** For $G=U(1)$ one has $BG\simeq \mathbb{C}P^\infty$, and [M,BG] corresponds to isomorphism classes of principal $U(1)$-bundles (equivalently complex line bundles) over $M.
