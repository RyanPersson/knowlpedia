+++
id = "fiber-bundles/orbit-map"
title = "Orbit map"
kind = "knowl"
summary = "The smooth map from a Lie group to a manifold sending a group element to its action on a fixed point."
aliases = ["orbit-map", "Orbit map"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/orbit-map.md"
+++

Let $G$ act on $M$ by a [[fiber-bundles/smooth-action-of-a-lie-group-on-a-manifold|smooth action]].

For $x\in M$, the **orbit map at $x$** is the [[fiber-bundles/smooth-map|smooth map]]
\[
\Phi^x: G \longrightarrow M,\qquad \Phi^x(g)=g\cdot x.
\]
Its image is the [[fiber-bundles/orbit-of-a-group-action|orbit]] $G\cdot x$.

The kernel of $\Phi^x$ (in the sense of elements acting trivially at $x$) is the [[algebra-groups/stabilizer|stabilizer subgroup]] $G_x$. Consequently, $\Phi^x$ is constant on left cosets of $G_x$ and factors through the quotient $G/G_x$.

## Examples
1. **Left translation on $G$.** For the action of $G$ on itself by left multiplication and a fixed $h\in G$, the orbit map is $g\mapsto gh$.
2. **Rotations of a vector.** For $SO(2)\curvearrowright \mathbb{R}^2$ and $x\neq 0$, the orbit map parametrizes the circle of radius $\|x\|$.
3. **Conjugation.** For the conjugation action of $G$ on itself, the orbit map at $h$ is $g\mapsto ghg^{-1}$, whose image is the conjugacy class of $h$.
