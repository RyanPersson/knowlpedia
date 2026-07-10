---
title: "Continuous image of compact set is compact"
description: "A continuous map sends compact sets to compact sets"
---

**Continuous image of compact set is compact**: Let $f:X\to Y$ be a {{< knowl id="continuous-map" text="continuous map" >}} between topological spaces, and let $K\subseteq X$ be {{< knowl id="compact-set" text="compact" >}}. Then the {{< knowl id="image" text="image" >}} $f(K)\subseteq Y$ is compact.

**Proof sketch**: Let $\mathcal{V}$ be an {{< knowl id="open-cover" text="open cover" >}} of $f(K)$ in $Y$. The {{< knowl id="preimage" text="preimages" >}} of sets in $\mathcal{V}$ form an open cover of $K$ in $X$. By compactness of $K$, finitely many of these preimages cover $K$, and the corresponding finitely many sets in $\mathcal{V}$ cover $f(K)$.

**Examples:**
- If $K\subset\mathbb{R}$ is compact and $f$ is continuous, then $f(K)\subset\mathbb{R}$ is compact.
- The projection map $X\times Y\to X$ sends compact subsets of $X\times Y$ to compact subsets of $X$.
