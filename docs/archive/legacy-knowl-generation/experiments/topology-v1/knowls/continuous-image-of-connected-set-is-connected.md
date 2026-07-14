---
title: "Continuous image of a connected set is connected"
description: "A continuous map sends connected subsets to connected subsets"
---

**Continuous image of a connected set is connected**: Let $f:X\to Y$ be a {{< knowl id="continuous-map" text="continuous map" >}} and let $A\subseteq X$ be {{< knowl id="connected-set" text="connected" >}}. Then the {{< knowl id="image" text="image" >}} $f(A)\subseteq Y$ is connected.

This is one of the most frequently used ways to prove a set is connected: identify it as the image of a connected set under a continuous map.

**Proof sketch** *(optional)*: Suppose $f(A)$ could be written as a union of two disjoint nonempty open subsets in the subspace topology. Consider the {{< knowl id="intersection" text="intersections" >}} of $A$ with the {{< knowl id="preimage" text="preimages" >}} of these two open pieces under $f$. Continuity ensures those subsets of $A$ are open in $A$, disjoint, nonempty, and cover $A$, contradicting that $A$ is connected.
