---
title: "Refinement of a partition"
description: "A partition that contains all points of another partition."
---

A **refinement of a partition** $P$ of $[a,b]$ is a partition $Q$ of $[a,b]$ such that every point of $P$ is also a point of $Q$. In other words, $P\subseteq Q$ in the sense of {{< knowl id="subset" section="shared-foundations" text="subset" >}}.

Refinements are used to compare {{< knowl id="upper-sum" text="upper sums" >}} and {{< knowl id="lower-sum" text="lower sums" >}}: making a partition finer is the basic way to force these sums closer together in {{< knowl id="riemann-integrable-function" text="Riemann integrability" >}}.

**Examples:**
- If $P=\{0,1\}$ and $Q=\{0,\tfrac12,1\}$, then $Q$ is a refinement of $P$.
- If $P_1=\{0,\tfrac12,1\}$ and $P_2=\{0,\tfrac13,\tfrac23,1\}$, then $P_1\cup P_2=\{0,\tfrac13,\tfrac12,\tfrac23,1\}$ is a common refinement of both.
