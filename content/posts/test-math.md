---
title: "Testing Math Rendering"
date: 2025-12-21
draft: false
comments: true
summary: "A test post demonstrating inline math, display equations, matrices, and the knowl system for expandable definitions."
---

This is a test post to verify that build-time math rendering works correctly.

## Inline Math

The quadratic formula is $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.

We can also write inline math like $e^{i\pi} + 1 = 0$ (Euler's identity).

## Display Math

Here's a display equation:

$$
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
$$

And the definition of a derivative:

$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

## Matrix

$$\begin{pmatrix} a & b \\\\ c & d \end{pmatrix} \begin{pmatrix} x \\\\ y \end{pmatrix} = \begin{pmatrix} ax + by \\\\ cx + dy \end{pmatrix}$$

If this renders without any flash or delay, the build-time KaTeX is working!

## Knowl Demo

A {{< knowl id="linear-map" text="linear map" >}} between {{< knowl id="vector-space" text="vector spaces" >}} preserves the algebraic structure. Click on the underlined terms above to see their definitions inline!
