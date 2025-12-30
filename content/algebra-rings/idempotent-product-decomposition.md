---
title: "Idempotents and product decompositions"
description: "Central idempotents split a ring as a product of two quotient-like pieces."
---

**Idempotents and product decompositions**: Let $R$ be a ring and let $e\in R$ be a central idempotent (so $e^2=e$ and $er=re$ for all $r\in R$). Then $eR$ and $(1-e)R$ are two-sided ideals, and the map
\[
R\longrightarrow eR\times (1-e)R,\qquad r\longmapsto (er,(1-e)r)
\]
is a ring isomorphism with inverse $(a,b)\mapsto a+b$. Conversely, any product decomposition $R\cong A\times B$ determines a central idempotent corresponding to $(1,0)$.

A {{< knowl id="idempotent-element" text="central idempotent" >}} in the {{< knowl id="center-of-ring" text="center" >}} splits a ring into a {{< knowl id="cartesian-product" text="product" >}} of rings via complementary {{< knowl id="ideal" text="ideals" >}}. This mechanism is closely related to {{< knowl id="chinese-remainder-decomposition" text="Chinese remainder decompositions" >}} and is often used to build explicit splittings from orthogonal idempotents.