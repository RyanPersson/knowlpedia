---
title: "Coset space"
description: "The quotient space of left cosets, a smooth manifold when is a closed Lie subgroup."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} and let $H\le G$ be a subgroup.

The **left coset space** $G/H$ is the set of left cosets
\[
G/H := \{gH : g\in G\},
\]
equipped with the quotient topology for the projection $\pi:G\to G/H$, $\pi(g)=gH$.

If $H$ is a **closed** {{< knowl id="lie-subgroup" text="Lie subgroup" >}} (equivalently, a closed subgroup that is automatically an embedded Lie subgroup by the {{< knowl id="closed-subgroup-theorem" text="Closed Subgroup Theorem" >}}), then $G/H$ carries a canonical smooth manifold structure characterized by:

- $\pi:G\to G/H$ is a smooth surjective submersion;
- the left action of $G$ on $G/H$ given by $g'\cdot (gH)=(g'g)H$ is a smooth {{< knowl id="smooth-action-lie-group" text="Lie group action" >}}.

In this case, $G/H$ is a basic example of a {{< knowl id="homogeneous-space" text="homogeneous space" >}}: the action is transitive and the stabilizer of the basepoint $eH$ is exactly $H$ (compare {{< knowl id="stabilizer-lie-group" text="stabilizer" >}} and {{< knowl id="transitive-action-lie" text="transitive action" >}}).

## Tangent space identification
Let $\mathfrak g=\mathrm{Lie}(G)$ and $\mathfrak h=\mathrm{Lie}(H)$ (see {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra of a Lie group" >}}). Then
\[
T_{eH}(G/H)\;\cong\;\mathfrak g/\mathfrak h,
\]
canonically, via the differential $d\pi_e:\mathfrak g\to T_{eH}(G/H)$ whose kernel is $\mathfrak h$.

**Context.** Many geometric objects (spheres, Grassmannians, flag varieties) arise naturally as $G/H$; understanding $G/H$ is often the first step in studying invariant tensors such as {{< knowl id="left-invariant-differential-form" text="left-invariant forms" >}} or {{< knowl id="bi-invariant-metric" text="bi-invariant metrics" >}} on $G$ and their descendants on $G/H$.
