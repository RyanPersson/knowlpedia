---
title: "Differentiability at a point (one variable)"
description: "A function is differentiable at a point if the limit defining its derivative exists there."
---

A function \(f: (a, b) \to \mathbb{R}\) is **differentiable at** \(x_0 \in (a, b)\) if the limit
$$
f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}
$$
exists. This limit, when it exists, is the {{< knowl id="derivative" text="derivative" >}} of \(f\) at \(x_0\).

## Equivalent formulation
\(f\) is differentiable at \(x_0\) iff there exists \(L \in \mathbb{R}\) such that
$$
f(x_0 + h) = f(x_0) + Lh + o(h) \quad \text{as } h \to 0.
$$
Here \(L = f'(x_0)\) and \(o(h)\) denotes a function with \(o(h)/h \to 0\).

## Implications
- Differentiability at \(x_0\) implies {{< knowl id="continuity-at-a-point" text="continuity at" >}} \(x_0\).
- The converse is false: \(f(x) = |x|\) is continuous but not differentiable at \(0\).

## One-sided derivatives
Left and right derivatives are
$$
f'_-(x_0) = \lim_{h \to 0^-} \frac{f(x_0 + h) - f(x_0)}{h}, \quad f'_+(x_0) = \lim_{h \to 0^+} \frac{f(x_0 + h) - f(x_0)}{h}.
$$
\(f\) is differentiable at \(x_0\) iff both exist and are equal.
