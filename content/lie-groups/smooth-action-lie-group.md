---
title: "Smooth action of a Lie group"
description: "A Lie group action on a manifold given by a smooth map G×M→M satisfying the action axioms."
---

Let $G$ be a Lie group and $M$ a smooth manifold. A **smooth (left) action** of $G$ on $M$ is a smooth map
\[
a: G\times M \longrightarrow M,\qquad (g,m)\mapsto g\cdot m,
\]
such that:

1. $e\cdot m = m$ for all $m\in M$ (where $e$ is the identity in $G$), and  
2. $(g_1g_2)\cdot m = g_1\cdot(g_2\cdot m)$ for all $g_1,g_2\in G$ and $m\in M$.

Associated to any smooth action are the basic orbit-stabilizer constructions: the orbit $G\cdot m$ (see {{< knowl id="orbit-lie-group" text="orbit" >}}) and the stabilizer subgroup $G_m$ (see {{< knowl id="stabilizer-lie-group" text="stabilizer" >}}). If the action is transitive, $M$ becomes a {{< knowl id="homogeneous-space" text="homogeneous space" >}}; if it is free, it resembles a {{< knowl id="principal-homogeneous-space" text="principal homogeneous space" >}} (compare {{< knowl id="transitive-action-lie" text="transitive action" >}} and {{< knowl id="free-action-lie" text="free action" >}}).

Differentiating at the identity produces an infinitesimal action: each $X\in\mathfrak g=\mathrm{Lie}(G)$ defines a vector field $X_M$ on $M$ by
\[
(X_M)_m = \left.\frac{d}{dt}\right|_{t=0}\exp(tX)\cdot m,
\]
linking smooth actions to {{< knowl id="one-parameter-subgroup" text="one-parameter subgroups" >}} and the {{< knowl id="exponential-map-lie-group" text="exponential map" >}}. The kernel of the action homomorphism $G\to \mathrm{Diff}(M)$ measures whether the action is {{< knowl id="effective-action" text="effective" >}}.
