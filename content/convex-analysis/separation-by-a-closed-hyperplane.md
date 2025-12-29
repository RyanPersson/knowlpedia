---
title: "Separation by a Closed Hyperplane"
description: "Separation using a nonzero continuous functional in the dual space."
---

Let $X$ be a real {{< knowl id="norm-normed-vector-space" text="normed space" >}} and let $\Omega_1,\Omega_2\subset X$ be nonempty.

We say that $\Omega_1$ and $\Omega_2$ can be **separated by a closed hyperplane** if there exists a nonzero functional $x^*\in {{< knowl id="dual-space-and-duality-pairing" text="X^*" >}}$ such that
$$
\langle x^*,x\rangle \le \langle x^*,y\rangle \quad\text{whenever }x\in\Omega_1,\ y\in\Omega_2.
$$

Here "closed {{< knowl id="hyperplane" text="hyperplane" >}}" emphasizes that $x^*$ is continuous, so each level set $\{x\mid \langle x^*,x\rangle=\alpha\}$ is {{< knowl id="closed-subset" text="closed" >}}; see {{< knowl id="continuity-of-linear-functionals-via-closed-level-sets" text="continuity via closed level sets" >}}.
