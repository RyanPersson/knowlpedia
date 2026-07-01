+++
id = "fiber-bundles/corollary-conn-gauge-is-a-well-defined-orbit-space"
title = "Gauge equivalence classes of connections form an orbit space"
kind = "knowl"
summary = "The space of connections modulo gauge transformations is the set of orbits for the gauge group action"
aliases = ["corollary-conn-gauge-is-a-well-defined-orbit-space", "Gauge equivalence classes of connections form an orbit space"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/corollary-conn-gauge-is-a-well-defined-orbit-space.md"
+++

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]]. Write
\[
\mathrm{Conn}(P)
\]
for the set (indeed an affine space) of all [[fiber-bundles/principal-connection|principal connections]] on $P$.

Let $\mathcal G(P)$ be the [[fiber-bundles/gauge-group|gauge group]] of $P$, i.e. the group of [[fiber-bundles/principal-bundle-automorphism|principal bundle automorphisms]] covering the identity on $M$.

By [[fiber-bundles/proposition-gauge-group-acts-on-conn-by-pullback|the proposition that the gauge group acts on connections by pullback]], there is a well-defined left action
\[
\mathcal G(P)\times \mathrm{Conn}(P)\longrightarrow \mathrm{Conn}(P),\qquad (u,\omega)\longmapsto u^*\omega.
\]
Because this is a genuine group action, it determines an equivalence relation on $\mathrm{Conn}(P)$:
\[
\omega_0 \sim \omega_1
\quad\Longleftrightarrow\quad
\exists\,u\in\mathcal G(P)\ \text{such that}\ \omega_1=u^*\omega_0.
\]

### Corollary (orbit space of connections modulo gauge)
The quotient set
\[
\mathrm{Conn}(P)/\mathcal G(P)
\]
is therefore a well-defined orbit space: its elements are precisely the gauge equivalence classes of connections, i.e. the orbits of the action $u\cdot \omega := u^*\omega$.

In local data, this action is the familiar gauge transformation law for connection 1-forms: on a chart, a [[fiber-bundles/local-gauge-transformation|local gauge transformation]] $g:U\to G$ sends a [[fiber-bundles/local-connection-1-form|local connection form]] $A$ to $A^g$, as in [[fiber-bundles/lemma-local-gauge-transformation-law-ag-g-1ag-g-1dg|the local gauge transformation law]].

## Examples
1. **Trivial bundle: gauge action on Lie algebra valued 1-forms.**
   If $P=M\times G$ is the [[fiber-bundles/trivial-principal-bundle-mgm|trivial principal bundle]], then specifying a connection is equivalent to specifying a $\mathfrak g$-valued 1-form $A\in\Omega^1(M;\mathfrak g)$. The gauge group identifies with $C^\infty(M,G)$, and the action is
   \[
   A \longmapsto g^{-1}Ag + g^{-1}dg,
   \]
   exactly the transformation described by [[fiber-bundles/gauge-transform-of-a-local-connection-form|gauge transform of a local connection form]].

2. **Abelian case: $U(1)$ connections differ by exact 1-forms on a trivial bundle.**
   For $G=U(1)$ on a trivial bundle, the adjoint term $g^{-1}Ag$ is just $A$, so the gauge action becomes
   \[
   A \longmapsto A + g^{-1}dg.
   \]
   Writing $g=e^{i\theta}$ locally, one has $g^{-1}dg = i\,d\theta$. Thus gauge-equivalent connections differ by an exact 1-form, and the orbit space records precisely the ambiguity coming from adding exact forms.

3. **Flat connections and holonomy data.**
   For a [[fiber-bundles/flat-principal-connection|flat principal connection]], gauge equivalence preserves the [[fiber-bundles/holonomy-group|holonomy]] up to conjugation. On $M=S^1$, gauge classes of flat connections on the trivial bundle correspond to conjugacy classes in $G$ via the holonomy element around the loop (constructed as in [[fiber-bundles/construction-holonomy-element-from-parallel-transport-around-a-loop|holonomy from parallel transport around a loop]]).
