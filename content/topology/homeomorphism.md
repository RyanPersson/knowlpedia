---
title: "Homeomorphism"
description: "A bijective continuous map with a continuous inverse."
---

A **homeomorphism** between {{< knowl id="topological-space" text="topological spaces" >}} $X$ and $Y$ is a {{< knowl id="bijective-function" section="shared-foundations" text="bijective function" >}} $f:X\to Y$ such that $f$ is a {{< knowl id="continuous-map" text="continuous map" >}} and its {{< knowl id="inverse-function" section="shared-foundations" text="inverse function" >}} $f^{-1}:Y\to X$ is also continuous.

If there exists a homeomorphism between $X$ and $Y$, the spaces are called *homeomorphic*; this means they are “the same” from the topological viewpoint, sharing properties like {{< knowl id="compact-set" text="compactness" >}} and {{< knowl id="connected-set" text="connectedness" >}}.

**Examples:**
- The map $f:(0,1)\to\mathbb{R}$ given by $f(x)=\tan(\pi(x-\tfrac12))$ is a homeomorphism.
- The map $g:\mathbb{R}\to(0,\infty)$ given by $g(x)=e^x$ is a homeomorphism.
- If two spaces have exactly the same open sets, the identity map between them is a homeomorphism.
