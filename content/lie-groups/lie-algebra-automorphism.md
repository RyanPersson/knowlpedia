---
title: "Lie algebra automorphism"
description: "An invertible linear map preserving the Lie bracket."
---

Let $\mathfrak g$ be a {{< knowl id="lie-algebra" text="Lie algebra" >}}.

**Definition (Automorphism).**  
A **Lie algebra automorphism** is a linear isomorphism $\phi:\mathfrak g\to\mathfrak g$ such that
\[
\phi([x,y])=[\phi(x),\phi(y)]\quad\text{for all }x,y\in\mathfrak g.
\]
Equivalently, $\phi$ is an isomorphism in the category of Lie algebras (compare {{< knowl id="lie-algebra-isomorphism" text="Lie algebra isomorphism" >}}).

The set $\mathrm{Aut}(\mathfrak g)$ is a group under composition; for many $\mathfrak g$ it carries a natural Lie group structure as a closed subgroup of $\mathrm{GL}(\mathfrak g)$.

**Inner vs outer features.**  
The adjoint representation gives canonical automorphisms by exponentiating inner derivations: for $x\in\mathfrak g$, the map $\exp(\mathrm{ad}_x)$ is an automorphism (built from {{< knowl id="inner-derivation" text="inner derivations" >}} and {{< knowl id="exponential-map-lie-group" text="exponentials" >}} in $\mathrm{GL}(\mathfrak g)$). Automorphisms not generated this way are “outer” in nature, and are related to {{< knowl id="outer-derivation" text="outer derivations" >}} at the infinitesimal level.

**Context.**  
Automorphisms organize symmetry of structure constants, control conjugacy of subalgebras (including Levi factors in the {{< knowl id="levi-decomposition-theorem" text="Levi decomposition" >}}), and interact with representation theory through transport of structure.
