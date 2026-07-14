---
title: "Heine–Borel theorem"
description: "In Euclidean space, compact sets are exactly the closed and bounded sets"
---

**Heine–Borel theorem**: In {{< knowl id="euclidean-space" text="Euclidean space" >}} $\mathbb{R}^n$ with its usual topology, a set $K\subseteq \mathbb{R}^n$ is {{< knowl id="compact-set" text="compact" >}} if and only if it is both {{< knowl id="closed-set" text="closed" >}} and {{< knowl id="bounded-set" text="bounded" >}}.

**Proof sketch**: If $K$ is compact, then it is bounded and closed (compactness implies boundedness and closedness in metric spaces). Conversely, if $K$ is closed and bounded in $\mathbb{R}^n$, then $K$ is complete (closed subsets of complete spaces are complete) and totally bounded (bounded subsets of $\mathbb{R}^n$ admit finite epsilon nets). Apply {{< knowl id="compact-iff-complete-totally-bounded" text="compact iff complete and totally bounded" >}}.

**Examples:**
- The closed ball $\{x\in\mathbb{R}^n:\|x\|\le 1\}$ is compact.
- The open ball $\{x\in\mathbb{R}^n:\|x\|<1\}$ is bounded but not closed, hence not compact.
