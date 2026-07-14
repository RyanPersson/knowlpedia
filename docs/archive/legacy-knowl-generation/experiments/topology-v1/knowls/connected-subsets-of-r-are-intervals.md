---
title: "Connected subsets of the real line are intervals"
description: "A subset of the real line is connected exactly when it has no gaps"
---

**Connected subsets of the real line are intervals**: Let $A\subseteq \mathbb{R}$, where $\mathbb{R}$ has its {{< knowl id="metric-induced-topology" text="usual metric topology" >}}, and view $A$ with the {{< knowl id="subspace-topology" text="subspace topology" >}}. Then $A$ is {{< knowl id="connected-set" text="connected" >}} if and only if the following “no gaps” condition holds:

If $a,b\in A$ with $a<b$ and $c\in\mathbb{R}$ satisfies $a<c<b$, then $c\in A$.

Equivalently, the connected subsets of $\mathbb{R}$ are precisely the intervals (including the empty set and singletons). This characterization is often used as a practical test; see {{< knowl id="connectedness-criteria-r" text="connectedness criteria in the real line" >}}.

**Proof sketch** *(optional)*: If $A$ has a gap (some $a<c<b$ with $a,b\in A$ but $c\notin A$), then $A\cap(-\infty,c)$ and $A\cap(c,\infty)$ are disjoint nonempty {{< knowl id="open-set" text="open" >}} sets in the subspace topology whose union is $A$, so $A$ is not connected. Conversely, an interval cannot be separated into two disjoint nonempty open subsets without creating a gap.
