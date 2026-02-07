---
title: "Connected set"
description: "A set that cannot be split into two disjoint nonempty open pieces in the subspace topology."
---

A **connected set** is a subset $C\subseteq X$ of a {{< knowl id="topological-space" text="topological space" >}} $X$ such that there do not exist disjoint nonempty sets $U,V\subseteq C$ that are {{< knowl id="open-set" text="open" >}} in the {{< knowl id="subspace-topology" text="subspace topology" >}} on $C$ and satisfy $C=U\cup V$.
Equivalently, the only subsets of $C$ that are both {{< knowl id="open-set" text="open" >}} and {{< knowl id="closed-set" text="closed" >}} in the subspace topology are $\varnothing$ and $C$.

Connectedness is a basic qualitative invariant of spaces, and it is preserved by {{< knowl id="continuous-map" text="continuous maps" >}} (see {{< knowl id="continuous-image-of-connected-set-is-connected" text="continuous images of connected sets" >}}). Maximal connected pieces are called {{< knowl id="connected-component" text="connected components" >}}.

**Examples:**
- Any {{< knowl id="interval" section="real-analysis" text="interval" >}} in $\mathbb{R}$ (with the usual topology) is connected.
- The set $(-1,0)\cup(0,1)\subseteq\mathbb{R}$ is not connected.
