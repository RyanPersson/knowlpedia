---
title: "Change of variables for pushforward measures"
description: "Identity relating integrals with respect to a pushforward measure to composition with the underlying map."
---

**Change of variables for pushforward measures:** Let $(X,\Sigma,\mu)$ be a {{< knowl id="measure-space" text="measure space" >}}, let $(Y,\mathcal T)$ be a {{< knowl id="measurable-space" text="measurable space" >}}, and let $T:X\to Y$ be a {{< knowl id="measurable-function" text="measurable function" >}}. Let $\nu = T_*\mu$ be the {{< knowl id="pushforward-measure" text="pushforward measure" >}} of $\mu$ by $T$. Then for every nonnegative measurable function $g:Y\to[0,\infty]$,
\[
\int_Y g\,d\nu \;=\; \int_X (g\circ T)\,d\mu.
\]
If $g$ is {{< knowl id="lebesgue-integrable-function" text="Lebesgue integrable" >}} with respect to $\nu$, then $g\circ T$ is Lebesgue integrable with respect to $\mu$ and the same identity holds with finite values.

This formula packages the defining property of the pushforward measure into an equality of {{< knowl id="lebesgue-integral" text="Lebesgue integrals" >}} and is a standard “change of variables” principle for transporting a {{< knowl id="measure" text="measure" >}} along a map. It is frequently used together with constructions such as the {{< knowl id="product-measure" text="product measure" >}}.
