---
title: "Core Equals Interior for Convex Sets in Normed Spaces"
description: "For convex sets with nonempty interior, algebraic and topological interiors coincide."
---

Let $X$ be a {{< knowl id="norm-normed-vector-space" text="normed vector space" >}} and let $\Omega\subset X$ be {{< knowl id="convex-set" text="convex" >}} with {{< knowl id="interior-of-a-set" text="int(Ω)" >}}$\neq\emptyset$.

**Theorem**:
$$
\operatorname{core}(\Omega)=\operatorname{int}(\Omega).
$$

**Context:**
The equality identifies the purely algebraic notion {{< knowl id="algebraic-interior-core-and-linear-closure" text="core(Ω)" >}} with the usual topological interior once the set is convex and has nonempty interior. The proof in the notes uses the geometric lemma {{< knowl id="segments-from-interior-points-stay-in-the-interior" text="segments from interior points stay in the interior" >}}.

**Proof sketch (idea):**
The inclusion $\operatorname{int}(\Omega)\subset \operatorname{core}(\Omega)$ is direct. For the reverse direction, translate so that $0\in\operatorname{int}(\Omega)$ and use convexity plus the segment lemma to show any core point must lie in the interior.
