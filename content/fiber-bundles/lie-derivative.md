---
title: "Lie derivative"
description: "The derivative of a differential form along the flow of a vector field."
---

Let $M$ be a {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let $X$ be a {{< knowl id="vector-field" text="vector field" >}} on $M$ with local flow $\Phi_t$. For a {{< knowl id="differential-k-form" text="differential k-form" >}} $\omega\in\Omega^k(M)$, the **Lie derivative of $\omega$ along $X$** is
$$
\mathcal{L}_X\omega = \left.\frac{d}{dt}\right|_{t=0}\Phi_t^*\omega,
$$

where $\Phi_t^*$ denotes pullback by the diffeomorphism $\Phi_t$.

The Lie derivative is characterized by **Cartan's formula**:
$$
\mathcal{L}_X\omega = d(\iota_X\omega) + \iota_X(d\omega),
$$

where $\iota_X$ is the {{< knowl id="interior-product" text="interior product" >}} and $d$ is the {{< knowl id="exterior-derivative" text="exterior derivative" >}}.

## Examples

1. **Functions.** For $f\in C^\infty(M)$, we have $\mathcal{L}_X f = X(f)$, the directional derivative.

2. **Rotation on the plane.** On $\mathbb{R}^2$, let $X = -y\partial_x + x\partial_y$. For $\omega = dx\wedge dy$, we have $\mathcal{L}_X\omega = 0$.

3. **Left-invariant forms.** On a {{< knowl id="lie-group" text="Lie group" >}} $G$, if $\omega$ and $X$ are both left-invariant, then $\mathcal{L}_X\omega$ is left-invariant.
