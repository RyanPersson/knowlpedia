---
title: "Measurable set"
description: "A subset that belongs to the sigma-algebra of a measurable space."
---

A **measurable set** in a measurable space $(X,\Sigma)$ is a subset $A\subseteq X$ with $A\in\Sigma$.

Measurable sets are precisely the subsets to which a {{< knowl id="measure" text="measure" >}} assigns a value, and they determine {{< knowl id="measurable-function" text="measurable functions" >}} via preimages. The {{< knowl id="indicator-function" text="indicator function" >}} of a measurable set is a basic example of a measurable function.

**Examples:**
- In $(\mathbb R,\mathcal B(\mathbb R))$ with the {{< knowl id="borel-sigma-algebra" text="Borel sigma-algebra" >}}, every open {{< knowl id="interval" section="real-analysis" text="interval" >}} such as $(a,b)$ is measurable.
- If $A$ is measurable in $(X,\Sigma)$, then its {{< knowl id="complement" section="shared-foundations" text="complement" >}} $X\setminus A$ is also measurable.
- If $(A_n)_{n\ge 1}$ are measurable, then the countable {{< knowl id="union" section="shared-foundations" text="union" >}} $\bigcup_{n=1}^\infty A_n$ is measurable.
