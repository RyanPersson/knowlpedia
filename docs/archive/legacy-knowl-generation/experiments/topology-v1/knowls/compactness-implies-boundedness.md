---
title: "Compactness implies boundedness"
description: "In a metric space, every compact set is bounded"
---

**Compactness implies boundedness**: If $K$ is a {{< knowl id="compact-set" text="compact set" >}} in a {{< knowl id="metric-space" text="metric space" >}} $(X,d)$, then $K$ is {{< knowl id="bounded-set" text="bounded" >}}.

**Proof sketch**: Fix $x_0\in X$. The family of {{< knowl id="open-ball" text="open balls" >}} $\{B(x_0,n)\}_{n\in\mathbb{N}}$ is an {{< knowl id="open-cover" text="open cover" >}} of $X$, hence of $K$. By compactness, $K$ is contained in $B(x_0,N)$ for some $N$, so $K$ is bounded.

**Examples:**
- Any compact subset of $\mathbb{R}^n$ is bounded.
- The set $\{0\}\cup\{1/n : n\in\mathbb{N}\}\subset\mathbb{R}$ is compact and bounded.
