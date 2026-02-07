---
title: "Parallel transport map along a curve"
description: "Construction of the parallel transport map determined by a connection along a smooth curve."
---

Let $E\to M$ be a vector bundle with a {{< knowl id="connection-on-a-vector-bundle" text="connection" >}} $\nabla$.

Let $\gamma:[a,b]\to M$ be a smooth curve.

## Construction
A section $s$ of $E$ **along $\gamma$** (that is, $s(t)\in E_{\gamma(t)}$) is called **parallel** if it satisfies
\[
\nabla_{\dot\gamma(t)} s(t)=0 \quad \text{for all } t\in[a,b].
\]
This is the {{< knowl id="parallel-section-along-a-curve" text="parallel section equation along a curve" >}}.

For each initial vector $v\in E_{\gamma(a)}$, there exists a unique parallel section $s_v$ along $\gamma$ with $s_v(a)=v$. Define the **parallel transport map**
\[
P_\gamma : E_{\gamma(a)} \longrightarrow E_{\gamma(b)},\qquad P_\gamma(v):=s_v(b).
\]
This is a linear isomorphism, and it depends smoothly on the curve and on the initial value.

This construction is the vector-bundle version of {{< knowl id="parallel-transport" text="parallel transport" >}}; when $E$ is an associated bundle of a principal bundle with connection, $P_\gamma$ can be obtained from the unique {{< knowl id="construction-horizontal-lift-of-curves-and-uniqueness-of-horizontal-lift" text="horizontal lift of the base curve" >}}.

### Basic properties
- If $\gamma$ is reversed, then $P_{\gamma^{-1}}=(P_\gamma)^{-1}$.
- If $\gamma=\gamma_2\star\gamma_1$ is a concatenation, then
  \[
  P_{\gamma_2\star\gamma_1} = P_{\gamma_2}\circ P_{\gamma_1},
  \]
  as in {{< knowl id="proposition-parallel-transport-respects-concatenation-of-paths" text="parallel transport respects concatenation" >}}.
- For loops $\gamma$ based at $x$, the endomorphisms $P_\gamma:E_x\to E_x$ generate holonomy; compare {{< knowl id="construction-holonomy-element-from-parallel-transport-around-a-loop" text="constructing a holonomy element from a loop" >}} and the {{< knowl id="holonomy-group" text="holonomy group" >}}.

## Examples
1. **Flat transport in a trivial bundle.** On $E=M\times \mathbb R^n$ with the {{< knowl id="flat-connection-a0-on-a-trivial-bundle" text="flat connection" >}} $\nabla=d$, the parallel equation is $\dot s(t)=0$, so $s(t)$ is constant and $P_\gamma=\mathrm{id}_{\mathbb R^n}$ for every curve.

2. **Line bundle with a 1-form potential.** On the trivial complex line bundle $M\times\mathbb C$, fix a real 1-form $\alpha$ and define $\nabla=d+i\alpha$. Then the parallel equation along $\gamma$ becomes
   \[
   \dot s(t) + i\,\alpha(\dot\gamma(t))\,s(t)=0,
   \]
   with solution
   \[
   P_\gamma(z) = \exp\!\Big(-i\int_\gamma \alpha\Big)\,z.
   \]
   In the abelian case this matches the familiar “phase accumulation” picture.

3. **Levi-Civita parallel transport on the sphere.** For the tangent bundle of the unit sphere $S^2$ with its {{< knowl id="levicivita-connection-connection" text="Levi-Civita connection" >}}, parallel transport around a geodesic triangle rotates tangent vectors by an angle equal to the triangle’s area (a constant-curvature instance of Gauss–Bonnet). This gives a concrete way to see nontrivial holonomy on $S^2$.
