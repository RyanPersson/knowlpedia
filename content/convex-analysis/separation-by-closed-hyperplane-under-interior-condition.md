---
title: "Separation by Closed Hyperplane Under an Interior Condition"
description: "If int(Ω1)≠∅ and int(Ω1)∩Ω2=∅, then Ω1 and Ω2 are separable by a continuous functional."
---

Let $X$ be a real {{< knowl id="norm-normed-vector-space" text="normed space" >}} and let $\Omega_1,\Omega_2\subset X$ be nonempty {{< knowl id="convex-set" text="convex sets" >}}. Assume that {{< knowl id="interior-of-a-set" text="int(Ω₁)" >}}$\neq\emptyset$ and
$$
\operatorname{int}(\Omega_1)\cap\Omega_2=\emptyset.
$$

**Theorem**: The sets $\Omega_1$ and $\Omega_2$ can be {{< knowl id="separation-by-a-closed-hyperplane" text="separated by a closed hyperplane" >}}; i.e., there exists $x^*\in X^*\setminus\{0\}$ such that
$$
\langle x^*,x\rangle \le \langle x^*,y\rangle\quad \text{for all }x\in\Omega_1,\ y\in\Omega_2.
$$

**Context:**
In vector spaces, the analogous separation uses possibly discontinuous linear functionals (see {{< knowl id="separation-of-two-convex-sets-via-the-core-condition" text="core-based separation" >}}). The interior assumption ensures the separating functional is continuous, using {{< knowl id="continuity-of-linear-functionals-via-closed-level-sets" text="closed level-set continuity" >}}.
