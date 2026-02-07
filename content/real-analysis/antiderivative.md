---
title: "Antiderivative"
description: "A function whose derivative equals a given function."
---

An **antiderivative** (or **primitive**) of a function \(f: I \to \mathbb{R}\) on an interval \(I\) is a {{< knowl id="differentiable-map" text="differentiable function" >}} \(F: I \to \mathbb{R}\) such that
$$
F'(x) = f(x) \quad \text{for all } x \in I.
$$

## Non-uniqueness
If \(F\) is an antiderivative of \(f\), then so is \(F + C\) for any constant \(C\). Moreover, any two antiderivatives differ by a constant: if \(F' = G' = f\) on an interval, then \(F - G\) is constant.

The family of all antiderivatives is written as the **indefinite integral**:
$$
\int f(x)\, dx = F(x) + C.
$$

## Connection to definite integrals
The {{< knowl id="fundamental-theorem-of-calculus-i" text="Fundamental Theorem of Calculus" >}} states that if \(f\) is continuous, then
$$
F(x) = \int_a^x f(t)\, dt
$$
is an antiderivative of \(f\).

## Examples
- An antiderivative of \(x^n\) (for \(n \neq -1\)) is \(\frac{x^{n+1}}{n+1}\).
- An antiderivative of \(\cos x\) is \(\sin x\).
- An antiderivative of \(e^x\) is \(e^x\).
