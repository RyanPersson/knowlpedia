---
title: "Convexity characterized by positive semidefinite Hessian"
description: "A C^2 function on an open convex set is convex iff its Hessian is positive semidefinite everywhere"
---

**Theorem.**
Let $f:\Omega\to\mathbb{R}$ be twice continuously differentiable on a nonempty open convex set $\Omega\subset\mathbb{R}^n$. Then $f$ is convex on $\Omega$ if and only if for every $x\in\Omega$ its Hessian matrix $\nabla^2 f(x)$ is **positive semidefinite** (in the sense of {{< knowl id="nonnegative-positive-semidefinite-operator" text="nonnegative operators" >}}), i.e.,
$$
\langle v,\nabla^2 f(x)\,v\rangle \ge 0 \quad \text{for all } v\in\mathbb{R}^n.
$$

**Context.** This is the standard multivariable calculus criterion for convexity and underlies many second-order methods in optimization.

**Proof sketch.** Convexity of $f$ is equivalent to convexity of every restriction to a line: for fixed $x\in\Omega$ and direction $d\in\mathbb{R}^n$, consider $\varphi(t)=f(x+td)$ on the maximal interval where $x+td\in\Omega$. Apply the one-dimensional criterion {{< knowl id="convexity-via-nonnegative-second-derivative" text="f''≥0 ⇔ convex" >}} to $\varphi$, noting that $\varphi''(t)=\langle d,\nabla^2 f(x+td)d\rangle$.
