---
title: "Integrable horizontal distribution"
description: "A horizontal distribution closed under Lie brackets, equivalently tangent to a foliation transverse to the fibers."
---

Let $\pi:E\to M$ be a surjective submersion and let $H\subset TE$ be a {{< knowl id="horizontal-distribution" text="horizontal distribution" >}}.

**Definition.** The horizontal distribution $H$ is *integrable* if it is involutive: for any smooth vector fields $X,Y$ on $E$ taking values in $H$ (i.e. horizontal vector fields), their {{< knowl id="lie-bracket" text="Lie bracket" >}} $[X,Y]$ also takes values in $H$.

By the Frobenius theorem, integrability is equivalent to the existence of a foliation of $E$ by immersed submanifolds whose tangent spaces equal $H$. For a horizontal distribution, such leaves are automatically transverse to the fibers, so locally each leaf projects diffeomorphically onto an open subset of $M$. In many geometric settings, non-integrability is measured by an appropriate notion of {{< knowl id="curvature" text="curvature" >}} (the “vertical part” of brackets of horizontal fields).

## Examples
1. **Product horizontals are integrable.** On $E=M\times F$ with $H_{(x,f)}=T_xM\oplus\{0\}$, the horizontal leaves are the slices $M\times\{f\}$, so $H$ is integrable.
2. **Flat principal connection gives integrable horizontals.** On a principal bundle with a flat connection, the horizontal distribution is involutive; locally, horizontal leaves provide local “parallel” sections.
3. **Non-example from curvature.** For the Levi-Civita connection on the frame bundle of a curved Riemannian manifold (e.g. the round sphere), the induced horizontal distribution is typically not integrable; horizontal loops can produce nontrivial holonomy.
