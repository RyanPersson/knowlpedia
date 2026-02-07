---
title: "Orientation of a real vector bundle"
description: "A choice of consistent orientation in each fiber of a real vector bundle, varying continuously across the base."
---

Let $\pi:E\to M$ be a smooth real vector bundle of rank $r$ over a {{< knowl id="smooth-manifold" text="smooth manifold" >}}.

An **orientation** of $E$ can be defined in any of the following equivalent ways:

1. **Atlas definition (transition determinants).** Choose a vector bundle atlas with local trivializations over an open cover $\{U_\alpha\}$ such that the transition functions
   \[
   g_{\alpha\beta}:U_\alpha\cap U_\beta\to \mathrm{GL}(r,\mathbb R)
   \]
   all have positive determinant. Two such atlases are equivalent if their union still has positive-determinant transition functions. An orientation is an equivalence class of such atlases.

2. **Frame definition.** An orientation is a choice, for each $x\in M$, of one of the two connected components of the set of bases of $E_x$, varying locally so that on overlaps it is preserved; equivalently, it is a choice of the “positive” {{< knowl id="oriented-frame" text="oriented frames" >}} in each fiber.

3. **Determinant line bundle definition.** Let $\det(E):=\Lambda^rE$ be the top {{< knowl id="exterior-power-bundle" text="exterior power bundle" >}}. Then $\det(E)$ is a real line bundle, and an orientation of $E$ is the choice of a connected component of $\det(E)\setminus\{0\}$ in each fiber; equivalently, it is the choice of a nowhere-vanishing section of $\det(E)$ up to multiplication by a positive function.

If $M$ is connected, an orientation (if it exists) is a global structure; if it does not exist, $E$ is called **non-orientable**.

## Examples
1. **Tangent bundle of an oriented manifold.** An orientation of $M$ determines an orientation of the {{< knowl id="tangent-bundle" text="tangent bundle" >}} $TM$ by declaring coordinate frames with positively oriented Jacobian to be positive.

2. **Trivial bundle.** The bundle $M\times\mathbb R^r$ has a canonical orientation given by the standard basis of $\mathbb R^r$ in each fiber.

3. **Möbius line bundle.** The Möbius real line bundle over $S^1$ is non-orientable: its transition function on an overlap has negative determinant (it is the constant $-1$ in $\mathrm{GL}(1,\mathbb R)$).
