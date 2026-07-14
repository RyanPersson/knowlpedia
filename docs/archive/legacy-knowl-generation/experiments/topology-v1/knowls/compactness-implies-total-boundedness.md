---
title: "Compactness implies total boundedness"
description: "In a metric space, compactness forces total boundedness"
---

**Compactness implies total boundedness**: If $K$ is a {{< knowl id="compact-set" text="compact set" >}} in a {{< knowl id="metric-space" text="metric space" >}} $(X,d)$, then $K$ is {{< knowl id="totally-bounded-set" text="totally bounded" >}}.

**Proof sketch**: Fix $\varepsilon>0$. The family of {{< knowl id="open-ball" text="open balls" >}} $\{B(x,\varepsilon)\}_{x\in K}$ is an {{< knowl id="open-cover" text="open cover" >}} of $K$. By compactness, there is a finite subcover, i.e. finitely many $\varepsilon$-balls cover $K$.

**Examples:**
- Every compact subset of $\mathbb{R}^n$ is totally bounded.
- The implication can fail without a metric structure: “totally bounded” is a metric notion.
