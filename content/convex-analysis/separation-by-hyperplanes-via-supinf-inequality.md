---
title: "Separation via Sup/Inf Inequality"
description: "Hyperplane separation is equivalent to sup_{Ω1}f ≤ inf_{Ω2}f for some f≠0."
---

Let $X$ be a real {{< knowl id="vector-space" section="linear-algebra" section="linear-algebra" text="vector space" >}} and let $\Omega_1,\Omega_2\subset X$ be nonempty.

**Proposition**: The sets $\Omega_1$ and $\Omega_2$ can be {{< knowl id="separation-by-a-hyperplane" text="separated by a hyperplane" >}} if and only if there exists a nonzero linear functional $f:X\to\mathbb{R}$ such that
$$
\sup_{x\in\Omega_1} f(x)\le \inf_{y\in\Omega_2} f(y).
$$

**Context:**
This equivalence is often used because it replaces a pointwise inequality ("for all $x$ and $y$") with a single inequality between two real numbers. In the notes, the existence of $\sup$ and $\inf$ is justified using completeness of $\mathbb{R}$.
