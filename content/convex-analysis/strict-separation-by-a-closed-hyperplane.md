---
title: "Strict Separation by a Closed Hyperplane"
description: "Strict separation means there is a positive gap between the two sets under a continuous functional."
---

Let $X$ be a real {{< knowl id="norm-normed-vector-space" text="normed space" >}} and let $\Omega_1,\Omega_2\subset X$ be nonempty.

We say that $\Omega_1$ and $\Omega_2$ can be **strictly separated by a closed hyperplane** if there exist $x^\ast \in X^\ast$ (see {{< knowl id="dual-space-and-duality-pairing" text="dual space" >}}) and real numbers $\alpha<\beta$ such that
$$
\langle x^\ast ,x\rangle \le \alpha < \beta \le \langle x^\ast ,y\rangle
\quad\text{for all }x\in\Omega_1,\ y\in\Omega_2.
$$

Equivalently, strict separation holds iff there exists $x^\ast \in X^\ast $ with
$$
\sup_{x\in\Omega_1}\langle x^\ast ,x\rangle < \inf_{y\in\Omega_2}\langle x^\ast ,y\rangle.
$$

This notion strengthens {{< knowl id="separation-by-a-closed-hyperplane" text="separation by a closed hyperplane" >}} by requiring a strict gap.
