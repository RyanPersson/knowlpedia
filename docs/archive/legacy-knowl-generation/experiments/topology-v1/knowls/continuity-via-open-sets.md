---
title: "Continuity via open sets"
description: "Continuity characterized by preimages of open sets."
---

**Continuity via open sets**: Let $f:X\to Y$ be a function between topological spaces. Then $f$ is {{< knowl id="continuous-map" text="continuous" >}} if and only if for every {{< knowl id="open-set" text="open set" >}} $V\subseteq Y$, the {{< knowl id="preimage" text="preimage" >}} $f^{-1}(V)$ is open in $X$.

This is the standard “intrinsic” definition of continuity in topology. In a {{< knowl id="metric-space" text="metric space" >}}, it agrees with the usual epsilon–delta notion when the topology is the {{< knowl id="metric-induced-topology" text="one induced by the metric" >}}.

**Proof sketch** *(optional)*: The “only if” direction is exactly the definition of continuity. For the converse, the topology on $Y$ is determined by its open sets, so checking that all open sets pull back to open sets is sufficient to ensure continuity.
