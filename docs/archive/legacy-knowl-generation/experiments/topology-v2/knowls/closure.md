---
title: "Closure"
description: "Smallest closed set containing a given set."
---

The **closure** of a subset $A\subseteq X$ in a {{< knowl id="topological-space" text="topological space" >}} $(X,\tau)$ is
\[
\overline{A}=\bigcap\{\,F\subseteq X : F \text{ is closed and } A\subseteq F\,\}.
\]

Thus $\overline{A}$ is the {{< knowl id="intersection" section="shared-foundations" text="intersection" >}} of all {{< knowl id="closed-set" text="closed sets" >}} containing $A$, and is the smallest closed set containing $A$.

**Examples:**
- In $\mathbb{R}$, $\overline{(0,1)}=[0,1]$.
- In $\mathbb{R}$, $\overline{\mathbb{Q}}=\mathbb{R}$ (the rationals are dense).
- If $F$ is closed, then $\overline{F}=F$.
