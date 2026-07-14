---
title: "Continuous map"
description: "A function between topological spaces that sends nearby points to nearby points."
---

A **continuous map** between {{< knowl id="topological-space" text="topological spaces" >}} is a {{< knowl id="function" section="shared-foundations" text="function" >}} $f:X\to Y$ such that for every point $x\in X$ and every {{< knowl id="neighborhood" text="neighborhood" >}} $V$ of $f(x)$ in $Y$, there exists a neighborhood $U$ of $x$ in $X$ with $f(U)\subseteq V$.

This pointwise neighborhood condition is equivalent to the usual open-set formulation in {{< knowl id="continuity-via-open-sets" text="continuity via open sets" >}}.

**Examples:**
- The identity map $\mathrm{id}_X:X\to X$ is continuous.
- Any constant map $c:X\to Y$ is continuous.
- If $Y\subseteq X$ has the {{< knowl id="subspace-topology" text="subspace topology" >}}, the inclusion $Y\hookrightarrow X$ is continuous.
