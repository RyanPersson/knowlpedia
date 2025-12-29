---
title: "Relatively compact set"
description: "A subset whose closure is compact (also called precompact)"
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $A\subseteq X$.

The set $A$ is **relatively compact** (or **precompact**) in $X$ if its {{< knowl id="closure" text="closure" >}} $\overline{A}$ is {{< knowl id="compact-set" text="compact" >}} in $X$:
$
\overline{A}\ \text{is compact}.
$

Equivalently (in metric spaces), $A$ is relatively compact if and only if every sequence in $A$ has a {{< knowl id="convergent-sequence" text="convergent" >}} {{< knowl id="subsequence" text="subsequence" >}} in $X$ whose {{< knowl id="limit-of-a-sequence" text="limit" >}} lies in $\overline{A}$.

Relative compactness is the correct notion of "compact up to taking limits": $A$ itself need not be {{< knowl id="closed-set" text="closed" >}}.

**Examples:**
- $(0,1)\subseteq\mathbb{R}$ is relatively compact since $\overline{(0,1)}=[0,1]$ is compact.
- Any {{< knowl id="bounded-set" text="bounded" >}} subset of $\mathbb{R}^k$ is relatively compact iff it is {{< knowl id="totally-bounded-set" text="totally bounded" >}} (and its closure is then compact by {{< knowl id="heine-borel-theorem" text="Heine–Borel" >}}).
- $\mathbb{Z}\subseteq\mathbb{R}$ is not relatively compact (its closure is unbounded, hence not compact).
