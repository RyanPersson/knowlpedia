---
title: "Gauge equivalence classes of connections form an orbit space"
description: "The space of connections modulo gauge transformations is the set of orbits for the gauge group action"
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}. Write
\[
\mathrm{Conn}(P)
\]
for the set (indeed an affine space) of all {{< knowl id="principal-connection" text="principal connections" >}} on $P$.

Let $\mathcal G(P)$ be the {{< knowl id="gauge-group" text="gauge group" >}} of $P$, i.e. the group of {{< knowl id="principal-bundle-automorphism" text="principal bundle automorphisms" >}} covering the identity on $M$.

By {{< knowl id="proposition-gauge-group-acts-on-conn-by-pullback" text="the proposition that the gauge group acts on connections by pullback" >}}, there is a well-defined left action
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

In local data, this action is the familiar gauge transformation law for connection 1-forms: on a chart, a {{< knowl id="local-gauge-transformation" text="local gauge transformation" >}} $g:U\to G$ sends a {{< knowl id="local-connection-1-form" text="local connection form" >}} $A$ to $A^g$, as in {{< knowl id="lemma-local-gauge-transformation-law-ag-g-1ag-g-1dg" text="the local gauge transformation law" >}}.

## Examples
1. **Trivial bundle: gauge action on Lie algebra valued 1-forms.**  
   If $P=M\times G$ is the {{< knowl id="trivial-principal-bundle-mgm" text="trivial principal bundle" >}}, then specifying a connection is equivalent to specifying a $\mathfrak g$-valued 1-form $A\in\Omega^1(M;\mathfrak g)$. The gauge group identifies with $C^\infty(M,G)$, and the action is
   \[
   A \longmapsto g^{-1}Ag + g^{-1}dg,
   \]
   exactly the transformation described by {{< knowl id="gauge-transform-of-a-local-connection-form" text="gauge transform of a local connection form" >}}.

2. **Abelian case: $U(1)$ connections differ by exact 1-forms on a trivial bundle.**  
   For $G=U(1)$ on a trivial bundle, the adjoint term $g^{-1}Ag$ is just $A$, so the gauge action becomes
   \[
   A \longmapsto A + g^{-1}dg.
   \]
   Writing $g=e^{i\theta}$ locally, one has $g^{-1}dg = i\,d\theta$. Thus gauge-equivalent connections differ by an exact 1-form, and the orbit space records precisely the ambiguity coming from adding exact forms.

3. **Flat connections and holonomy data.**  
   For a {{< knowl id="flat-principal-connection" text="flat principal connection" >}}, gauge equivalence preserves the {{< knowl id="holonomy-group" text="holonomy" >}} up to conjugation. On $M=S^1$, gauge classes of flat connections on the trivial bundle correspond to conjugacy classes in $G$ via the holonomy element around the loop (constructed as in {{< knowl id="construction-holonomy-element-from-parallel-transport-around-a-loop" text="holonomy from parallel transport around a loop" >}}).
