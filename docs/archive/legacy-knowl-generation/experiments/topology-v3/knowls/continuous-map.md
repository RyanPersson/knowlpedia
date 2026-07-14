---
title: "Continuous map"
description: "A map that pulls back neighborhoods of images to neighborhoods of points."
---

Let $X$ and $Y$ be {{{< knowl id="topological-space" text="topological spaces" >}}} and let $f:X\to Y$ be a {{{< knowl id="function" section="shared-foundations" text="function" >}}}. The map $f$ is **continuous at a point** $x\in X$ if for every {{{< knowl id="neighborhood" text="neighborhood" >}}} $V$ of $f(x)$ in $Y$, there exists a neighborhood $U$ of $x$ in $X$ such that $f(U)\subseteq V$.

The map $f$ is **continuous** (or a **continuous map**) if it is continuous at every point of $X$. An equivalent global characterization is given by {{{< knowl id="continuity-via-open-sets" text="continuity via open sets" >}}}.
