---
title: "Construction: quotient manifold P/G for a free proper action"
description: "If a Lie group acts freely and properly on a smooth manifold P, the orbit space P/G is a smooth manifold and the projection is a submersion."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" >}} acting smoothly on a {{< knowl id="smooth-manifold" text="smooth manifold" >}} $P$. Write the action as a right action $(p,g)\mapsto p\cdot g$.

## Construction (Quotient manifold and principal bundle projection)
Assume the action is:

- **Free:** $p\cdot g=p$ implies $g=e$.
- **Proper:** the map $P\times G\to P\times P$, $(p,g)\mapsto (p,p\cdot g)$ is proper.

Then:

1. The orbit space $P/G$ carries a unique smooth manifold structure such that the projection
   \[
   \pi:P\to P/G
   \]
   is a smooth submersion.

2. With this smooth structure, $\pi:P\to P/G$ is a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with the given right action.

3. For each $p\in P$, the vertical tangent space is
   \[
   \ker(d\pi)_p \;=\; \{X^\#_p: X\in\mathfrak g\},
   \]
   where $X^\#$ is the fundamental vector field defined using {{< knowl id="convention-fundamental-vector-field-x-is-defined-using-the-right-action" text="the right-action convention" >}}.

This construction is the standard way principal bundles arise from symmetry.

## Examples
1. **Trivial example.** If $P=M\times G$ with right action $(x,h)\cdot g=(x,hg)$, the action is free and proper and the quotient is canonically $P/G\cong M$.

2. **Hopf fibration viewpoint.** The standard free action of $S^1$ on $S^{2n+1}\subset\mathbb C^{n+1}$ by scalar multiplication is free and proper; the quotient is complex projective space $S^{2n+1}/S^1\cong \mathbb{CP}^n$, and the projection is a principal $S^1$-bundle.

3. **Non-example (failure of properness).** If a noncompact group acts freely but not properly, the orbit space may fail to be Hausdorff, violating the manifold convention in {{< knowl id="convention-manifolds-are-smooth-hausdorff-and-second-countable" text="the manifold hypotheses" >}}.
