---
title: "Measurable function"
description: "A function whose preimages of measurable sets are measurable."
---

A **measurable function** between measurable spaces $(X,\Sigma)$ and $(Y,\mathcal T)$ is a {{< knowl id="function" section="shared-foundations" text="function" >}} $f:X\to Y$ such that for every $B\in \mathcal T$, the {{< knowl id="preimage" section="shared-foundations" text="preimage" >}} $f^{-1}(B)$ lies in $\Sigma$.

Measurability depends on the choice of sigma-algebras on domain and codomain; in particular, using the {{< knowl id="borel-sigma-algebra" text="Borel sigma-algebra" >}} connects measurability to topology. For example, a {{< knowl id="continuous-map" section="topology" text="continuous map" >}} between topological spaces is Borel measurable.

**Examples:**
- If $f:\mathbb R\to\mathbb R$ is continuous (in the usual topology), then $f$ is measurable as a map $(\mathbb R,\mathcal B(\mathbb R))\to(\mathbb R,\mathcal B(\mathbb R))$.
- If $A$ is a {{< knowl id="measurable-set" text="measurable set" >}} in $(X,\Sigma)$, then its {{< knowl id="indicator-function" text="indicator function" >}} $\mathbf 1_A:X\to\{0,1\}$ is measurable (with $\{0,1\}$ carrying its power-set sigma-algebra).
- Every {{< knowl id="simple-function" text="simple function" >}} is measurable by definition.
