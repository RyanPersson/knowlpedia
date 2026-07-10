---
title: "Topology axioms"
description: "The three closure properties that characterize a topology."
---

**Topology axioms**: A collection $\tau$ of subsets of a set $X$ is a topology if:
1. $\varnothing \in \tau$ and $X \in \tau$,
2. $\tau$ is closed under arbitrary {{< knowl id="union" text="unions" >}},
3. $\tau$ is closed under finite {{< knowl id="intersection" text="intersections" >}}.

These axioms are designed so that the family of {{< knowl id="open-set" text="open sets" >}} behaves robustly under “gluing” (unions) and “simultaneous conditions” (finite intersections), which supports constructions like {{< knowl id="basis-of-a-topology" text="bases" >}} and {{< knowl id="product-topology" text="product topologies" >}}.

**Examples:**
- $\{\varnothing, X\}$ satisfies the axioms, so it defines a topology (the indiscrete topology).
- The collection of all subsets of $X$ satisfies the axioms (the discrete topology).
