---
title: "Differentiation rules"
description: "Formulas for derivatives of sums, products, quotients, and compositions."
---

**Differentiation rules:** Let $I\subseteq\mathbb{R}$ be an {{< knowl id="interval" text="interval" >}}, and let $f,g:I\to\mathbb{R}$ be {{< knowl id="differentiability-1d" text="differentiable" >}} at a point $x\in I$. Then:

- (Linearity) For constants $c\in\mathbb{R}$,
  $$
  (f+g)'(x)=f'(x)+g'(x),\qquad (cf)'(x)=c\,f'(x).
  $$
- (Product rule)
  $$
  (fg)'(x)=f'(x)g(x)+f(x)g'(x).
  $$

- (Quotient rule) If $g(x)\neq 0$, then
  $$
  \left(\frac{f}{g}\right)'(x)=\frac{f'(x)g(x)-f(x)g'(x)}{(g(x))^2}.
  $$

- (Chain rule) If $g$ is differentiable at $x$ and $f$ is differentiable at $g(x)$, then for the {{< knowl id="composition" section="shared-foundations" text="composition" >}} $f\circ g$,
  $$
  (f\circ g)'(x)=f'(g(x))\,g'(x).
  $$

These identities are the basic computational tools for the {{< knowl id="derivative" text="derivative" >}} and are organized and extended in the {{< knowl id="chain-rule" text="chain rule" >}} and related results (for example, rules used in {{< knowl id="inverse-function-theorem-1d" text="local inversion" >}}).
