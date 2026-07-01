+++
id = "fiber-bundles/homotopy-class-mbg"
title = "Homotopy class [M,BG]"
kind = "knowl"
summary = "The set of homotopy classes of continuous maps from a manifold M to the classifying space BG."
aliases = ["homotopy-class-mbg", "Homotopy class [M,BG]"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/homotopy-class-mbg.md"
+++

Let $M$ be a [[fiber-bundles/smooth-manifold|smooth manifold]] and let $BG$ be the classifying space associated to a [[fiber-bundles/lie-group|Lie group]] $G$.

## Definition (Homotopy classes of maps into BG)
The notation **[M,BG]** denotes the set of (unbased) homotopy classes of continuous maps $f\colon M\to BG$.

Concretely, two maps $f_0,f_1\colon M\to BG$ define the same element of [M,BG] if there exists a continuous homotopy
\[
H\colon M\times [0,1] \to BG,\qquad H(\cdot,0)=f_0,\; H(\cdot,1)=f_1.
\]

If $\phi\colon M'\to M$ is a [[fiber-bundles/diffeomorphism|diffeomorphism]], then precomposition induces a bijection
\[
[M,BG] \xrightarrow{\;\cong\;} [M',BG], \quad [f]\mapsto [f\circ \phi].
\]

This set is the target of the classification map sending a [[fiber-bundles/principal-g-bundle|principal G-bundle]] $P\to M$ to the homotopy class of its [[fiber-bundles/classifying-map-of-a-principal-bundle|classifying map]].

## Examples
1. **Spheres.** For $M=S^n$, there is a canonical identification [S^n,BG] $\cong \pi_n(BG)$.
2. **Contractible bases.** If $M$ is contractible, then [M,BG] has exactly one element (every map is homotopic to a constant map).
3. **Line bundles.** For $G=U(1)$ one has $BG\simeq \mathbb{C}P^\infty$, and [M,BG] corresponds to isomorphism classes of principal $U(1)$-bundles (equivalently complex line bundles) over $M.
