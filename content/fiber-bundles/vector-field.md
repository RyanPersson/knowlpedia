---
title: "Vector field"
description: "A smooth section of the tangent bundle; equivalently, an assignment of a tangent vector to each point varying smoothly."
---

Let $M$ be a {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let $\pi:TM\to M$ denote its {{< knowl id="tangent-bundle" text="tangent bundle" >}}.

**Definition.** A **(smooth) vector field** on $M$ is a smooth map $X:M\to TM$ such that $\pi\circ X=\mathrm{id}_M$. Equivalently, $X$ is a smooth section of the tangent bundle, assigning to each $p\in M$ a tangent vector
\[
X_p \in T_pM
\]
(where $T_pM$ is the {{< knowl id="tangent-space-at-a-point" text="tangent space at $p$" >}}) in a way that is smooth in local coordinates.

A vector field can also be viewed as a derivation on smooth functions: for each $X$ and each $f\in C^\infty(M)$, one obtains a smooth function $X(f)\in C^\infty(M)$ defined by differentiating $f$ in the direction $X$. Using the pairing between tangent and cotangent spaces (see the {{< knowl id="cotangent-bundle" text="cotangent bundle" >}}), this can be written pointwise as
\[
(Xf)(p)=df_p(X_p).
\]

Given a {{< knowl id="smooth-map" text="smooth map" >}} $F:M\to N$, the {{< knowl id="differential-pushforward-of-a-smooth-map" text="differential (pushforward)" >}} $dF_p$ transports tangent vectors, and when $F$ is a {{< knowl id="diffeomorphism" text="diffeomorphism" >}} one can push vector fields forward along $F$ by applying $dF$ pointwise.

### Examples

1. **Coordinate vector fields on $\mathbb{R}^n$.** On $M=\mathbb{R}^n$ with coordinates $(x^1,\dots,x^n)$, the vector field $\partial/\partial x^i$ is defined by
   \[
   \left(\frac{\partial}{\partial x^i}\right)_p(f)=\frac{\partial (f\circ x^{-1})}{\partial x^i}\bigg|_{x(p)}.
   \]
   More generally, any $X=\sum_{i=1}^n a_i(x)\,\partial/\partial x^i$ with smooth coefficient functions $a_i$ is a smooth vector field.

2. **Radial and rotational fields on $\mathbb{R}^2$.** In coordinates $(x,y)$, the radial field
   \[
   X = x\,\frac{\partial}{\partial x}+y\,\frac{\partial}{\partial y}
   \]
   points outward from the origin, while the rotational field
   \[
   Y = -y\,\frac{\partial}{\partial x}+x\,\frac{\partial}{\partial y}
   \]
   generates counterclockwise rotation (away from the origin it is tangent to circles).

3. **Left-invariant vector fields on a Lie group.** If $G$ is a {{< knowl id="lie-group" text="Lie group" >}}, each element of the {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra" section="lie-groups">}} determines a unique {{< knowl id="left-invariant-vector-field" text="left-invariant vector field" section="lie-groups">}} by translating that tangent vector from the identity to every point via {{< knowl id="left-translation-l-g" text="left translation" >}}.
