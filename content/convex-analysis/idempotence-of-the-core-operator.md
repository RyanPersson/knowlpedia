---
title: "Idempotence of the Core Operator"
description: "Taking the core twice gives the same set: core(core(Ω))=core(Ω)."
---

Let $X$ be a {{< knowl id="vector-space" text="vector space" >}} and let $\Omega\subset X$ be {{< knowl id="convex-set" text="convex" >}}.

**Corollary**:
$$
\operatorname{core}(\operatorname{core}(\Omega))=\operatorname{core}(\Omega).
$$

Here {{< knowl id="algebraic-interior-core" text="core" >}} denotes the algebraic interior. This follows from {{< knowl id="segments-from-core-points-stay-in-the-core" text="segments from core points stay in the core" >}}: once a point is in $\operatorname{core}(\Omega)$, small segment perturbations remain inside, so taking the core again does not remove any points.
