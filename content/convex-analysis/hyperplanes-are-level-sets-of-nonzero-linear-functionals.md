---
title: "Hyperplanes as Level Sets of Linear Functionals"
description: "In real vector spaces, Ω is a hyperplane iff Ω={x : f(x)=α} for some f≠0."
---

Let $X$ be a real {{< knowl id="vector-space" section="linear-algebra" section="linear-algebra" text="vector space" >}}.

**Proposition**: A subset $\Omega\subset X$ is a {{< knowl id="hyperplane" text="hyperplane" >}} if and only if there exist a nonzero linear functional $f:X\to\mathbb{R}$ and a scalar $\alpha\in\mathbb{R}$ such that
$$
\Omega=\{x\in X\mid f(x)=\alpha\}.
$$

**Context:**
One direction uses the decomposition of codimension-one subspaces (see {{< knowl id="codimension-one-subspaces-yield-direct-sum-decompositions" text="codimension-one decomposition" >}}). The other direction uses that $\ker f$ has codimension one (see {{< knowl id="kernel-of-a-nonzero-linear-functional-has-codimension-one" text="codimension of kernels" >}}).
