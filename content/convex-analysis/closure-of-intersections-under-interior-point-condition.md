---
title: "Closure of intersections under an interior-point condition"
description: "If convex sets have intersecting interiors, closure distributes over their intersection"
---

**Theorem.**
Let $X$ be a normed vector space, and let $\Omega_1,\Omega_2\subset X$ be {{< knowl id="convex-set" text="convex" >}} sets such that
$$
\mathrm{int}(\Omega_1)\cap \mathrm{int}(\Omega_2)\neq\emptyset.
$$
Then
$$
\overline{\Omega_1\cap\Omega_2}=\overline{\Omega_1}\cap\overline{\Omega_2}.
$$

**Context.** In general, $\overline{A\cap B}\subset \overline{A}\cap\overline{B}$ can be strict. Convexity plus an interior qualification condition forces equality, which is important in convex analysis and duality.

**Proof idea.** Use the existence of an interior point common to both sets to "stabilize" approximations and apply {{< knowl id="segments-from-interior-points-stay-in-the-interior" text="interior-segment geometry" >}} to build sequences in $\Omega_1\cap\Omega_2$ approximating any point in $\overline{\Omega_1}\cap\overline{\Omega_2}$.

**Remark.** The conclusion remains valid under the weaker condition $\mathrm{int}(\Omega_1)\cap \Omega_2\neq\emptyset$.
