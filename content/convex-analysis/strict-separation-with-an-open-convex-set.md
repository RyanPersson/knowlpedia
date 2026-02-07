---
title: "Strict Separation When One Set is Open"
description: "An open convex set can be separated from a convex set with a strict inequality gap."
---

Let $X$ be a real {{< knowl id="norm-normed-vector-space" text="normed space" >}}. Let $G,\Omega\subset X$ be nonempty {{< knowl id="convex-set" text="convex sets" >}} and assume that $G$ is {{< knowl id="open-subset" text="open" >}}.

**Corollary**: There exist $x^\ast \in X^\ast$ (see {{< knowl id="dual-space-and-duality-pairing" text="dual space" >}}) and $\beta\in\mathbb{R}$ such that
$$
\langle x^\ast ,x\rangle < \beta \le \langle x^\ast ,y\rangle \quad \text{whenever }x\in G,\ y\in\Omega.
$$

This follows from {{< knowl id="separation-by-closed-hyperplane-under-interior-condition" text="closed hyperplane separation under an interior condition" >}} together with the openness of $G$, which allows a strict inequality on the $G$ side.
