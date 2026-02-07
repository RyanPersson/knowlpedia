---
title: "Horizontal lift of a vector field"
description: "The unique horizontal vector field on the total space that projects to a given vector field on the base."
---

Let $\pi:E\to M$ be a surjective submersion with an {{< knowl id="ehresmann-connection" text="Ehresmann connection" >}} and horizontal spaces $H_eE\subset T_eE$.

Let $X$ be a {{< knowl id="vector-field" text="vector field" >}} on $M$. Since $d\pi_e:H_eE\to T_{\pi(e)}M$ is an isomorphism for each $e$, one can lift $X$ pointwise and obtain a vector field on $E$.

**Definition.** The horizontal lift of $X$ is the unique vector field $X^{\mathrm h}$ on $E$ such that:
1. $X^{\mathrm h}(e)\in H_eE$ for every $e\in E$, and
2. $d\pi_e(X^{\mathrm h}(e)) = X(\pi(e))$ for every $e\in E$.

Equivalently, $X^{\mathrm h}(e)$ is the {{< knowl id="horizontal-lift-of-a-tangent-vector" text="horizontal lift of the tangent vector" >}} $X_{\pi(e)}$ at $e$, for each $e$.

## Examples
1. **Product bundle.** On $E=M\times F$ with product horizontals, the horizontal lift of $X$ is $(X,0)$: it differentiates in the base direction and does nothing in the fiber direction.
2. **Horizontal lift on a principal bundle.** Given a principal connection on $P\to M$, the lift $X^{\mathrm h}$ is the unique $G$-equivariant vector field on $P$ that is everywhere horizontal and $\pi$-related to $X$.
3. **Lift to the tangent bundle.** For an affine connection on $TM\to M$, the horizontal lift of $X$ is a vector field on $TM$ describing infinitesimal parallel translation of tangent vectors along the flow of $X$.
