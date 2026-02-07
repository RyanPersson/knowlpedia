---
title: "Differentiability implies continuity"
description: "If a function is differentiable at a point, then it is continuous at that point."
---

**Differentiability implies continuity:** Let $f:I\to\mathbb{R}$ be a {{< knowl id="function" section="shared-foundations" text="function" >}} on an {{< knowl id="interval" text="interval" >}} $I$, and let $a\in I$ be an interior point. If $f$ is {{< knowl id="differentiability-1d" text="differentiable" >}} at $a$, then
$$
\lim_{x\to a} f(x) \;=\; f(a),
$$

so $f$ is continuous at $a$.

More generally, if $f:U\to\mathbb{R}^m$ is {{< knowl id="differentiable-map" text="differentiable" >}} at $a\in U$ in the sense of the {{< knowl id="frechet-derivative" text="Fréchet derivative" >}}, then $f$ is continuous at $a$ (i.e. a {{< knowl id="continuous-map" section="topology" text="continuous map" >}} at that point). This connects {{< knowl id="derivative" text="derivatives" >}} to {{< knowl id="limit-at-a-point" text="limits at a point" >}}.
