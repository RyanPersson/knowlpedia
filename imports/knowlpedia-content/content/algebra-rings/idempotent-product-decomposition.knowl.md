+++
id = "algebra-rings/idempotent-product-decomposition"
title = "Idempotents and product decompositions"
kind = "knowl"
summary = "Central idempotents split a ring as a product of two quotient-like pieces."
aliases = ["idempotent-product-decomposition", "Idempotents and product decompositions"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/idempotent-product-decomposition.md"
+++

**Idempotents and product decompositions**: Let $R$ be a ring and let $e\in R$ be a central idempotent (so $e^2=e$ and $er=re$ for all $r\in R$). Then $eR$ and $(1-e)R$ are two-sided ideals, and the map
\[
R\longrightarrow eR\times (1-e)R,\qquad r\longmapsto (er,(1-e)r)
\]
is a ring isomorphism with inverse $(a,b)\mapsto a+b$. Conversely, any product decomposition $R\cong A\times B$ determines a central idempotent corresponding to $(1,0)$.

A [[algebra-rings/idempotent-element|central idempotent]] in the [[algebra-rings/center-of-ring|center]] splits a ring into a [[shared-foundations/cartesian-product|product]] of rings via complementary [[algebra-rings/ideal|ideals]]. This mechanism is closely related to [[algebra-rings/chinese-remainder-decomposition|Chinese remainder decompositions]] and is often used to build explicit splittings from orthogonal idempotents.
