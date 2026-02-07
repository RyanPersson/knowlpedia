---
title: "Separation of Two Convex Sets via the Core Condition"
description: "If core(Ω1)≠∅ and core(Ω1) is disjoint from Ω2, then Ω1 and Ω2 are separable by a hyperplane."
---

Let $X$ be a real {{< knowl id="vector-space" section="linear-algebra" section="linear-algebra" text="vector space" >}} and let $\Omega_1,\Omega_2\subset X$ be nonempty {{< knowl id="convex-set" text="convex sets" >}}. Assume {{< knowl id="algebraic-interior-core" text="core(Ω₁)" >}}$\neq\emptyset$ and
$$
\operatorname{core}(\Omega_1)\cap \Omega_2=\emptyset.
$$

**Theorem**: The sets $\Omega_1$ and $\Omega_2$ can be {{< knowl id="separation-by-a-hyperplane" text="separated by a hyperplane" >}}.

**Context:**
This strengthens the disjointness condition by requiring only that $\Omega_2$ avoid the core of $\Omega_1$. The argument uses {{< knowl id="idempotence-of-the-core-operator" text="idempotence of core" >}} and the {{< knowl id="auxiliary-separation-lemma-for-disjoint-convex-sets-with-nonempty-core" text="auxiliary separation lemma" >}}.
