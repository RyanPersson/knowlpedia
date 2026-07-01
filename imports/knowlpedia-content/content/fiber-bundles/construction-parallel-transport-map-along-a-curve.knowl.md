+++
id = "fiber-bundles/construction-parallel-transport-map-along-a-curve"
title = "Parallel transport map along a curve"
kind = "knowl"
summary = "Construction of the parallel transport map determined by a connection along a smooth curve."
aliases = ["construction-parallel-transport-map-along-a-curve", "Parallel transport map along a curve"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/construction-parallel-transport-map-along-a-curve.md"
+++

Let $E\to M$ be a vector bundle with a [[fiber-bundles/connection-on-a-vector-bundle|connection]] $\nabla$.

Let $\gamma:[a,b]\to M$ be a smooth curve.

## Construction
A section $s$ of $E$ **along $\gamma$** (that is, $s(t)\in E_{\gamma(t)}$) is called **parallel** if it satisfies
\[
\nabla_{\dot\gamma(t)} s(t)=0 \quad \text{for all } t\in[a,b].
\]
This is the [[fiber-bundles/parallel-section-along-a-curve|parallel section equation along a curve]].

For each initial vector $v\in E_{\gamma(a)}$, there exists a unique parallel section $s_v$ along $\gamma$ with $s_v(a)=v$. Define the **parallel transport map**
\[
P_\gamma : E_{\gamma(a)} \longrightarrow E_{\gamma(b)},\qquad P_\gamma(v):=s_v(b).
\]
This is a linear isomorphism, and it depends smoothly on the curve and on the initial value.

This construction is the vector-bundle version of [[fiber-bundles/parallel-transport|parallel transport]]; when $E$ is an associated bundle of a principal bundle with connection, $P_\gamma$ can be obtained from the unique [[fiber-bundles/construction-horizontal-lift-of-curves-and-uniqueness-of-horizontal-lift|horizontal lift of the base curve]].

### Basic properties
- If $\gamma$ is reversed, then $P_{\gamma^{-1}}=(P_\gamma)^{-1}$.
- If $\gamma=\gamma_2\star\gamma_1$ is a concatenation, then
  \[
  P_{\gamma_2\star\gamma_1} = P_{\gamma_2}\circ P_{\gamma_1},
  \]
  as in [[fiber-bundles/proposition-parallel-transport-respects-concatenation-of-paths|parallel transport respects concatenation]].
- For loops $\gamma$ based at $x$, the endomorphisms $P_\gamma:E_x\to E_x$ generate holonomy; compare [[fiber-bundles/construction-holonomy-element-from-parallel-transport-around-a-loop|constructing a holonomy element from a loop]] and the [[fiber-bundles/holonomy-group|holonomy group]].

## Examples
1. **Flat transport in a trivial bundle.** On $E=M\times \mathbb R^n$ with the [[fiber-bundles/flat-connection-a0-on-a-trivial-bundle|flat connection]] $\nabla=d$, the parallel equation is $\dot s(t)=0$, so $s(t)$ is constant and $P_\gamma=\mathrm{id}_{\mathbb R^n}$ for every curve.

2. **Line bundle with a 1-form potential.** On the trivial complex line bundle $M\times\mathbb C$, fix a real 1-form $\alpha$ and define $\nabla=d+i\alpha$. Then the parallel equation along $\gamma$ becomes
   \[
   \dot s(t) + i\,\alpha(\dot\gamma(t))\,s(t)=0,
   \]
   with solution
   \[
   P_\gamma(z) = \exp\!\Big(-i\int_\gamma \alpha\Big)\,z.
   \]
   In the abelian case this matches the familiar “phase accumulation” picture.

3. **Levi-Civita parallel transport on the sphere.** For the tangent bundle of the unit sphere $S^2$ with its [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]], parallel transport around a geodesic triangle rotates tangent vectors by an angle equal to the triangle’s area (a constant-curvature instance of Gauss–Bonnet). This gives a concrete way to see nontrivial holonomy on $S^2$.
