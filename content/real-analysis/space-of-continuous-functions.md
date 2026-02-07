---
title: "Space of continuous functions"
description: "The set of all real-valued continuous functions on a given topological space."
---

The **space of continuous functions** on a {{< knowl id="topological-space" section="topology" text="topological space" >}} $X$ is
\[
C(X)=\{f:X\to\mathbb{R} \mid f \text{ is continuous}\},
\]
where continuity is in the sense of a {{< knowl id="continuous-map" section="topology" text="continuous map" >}}. It is naturally a vector space under pointwise addition and scalar multiplication.

On domains where continuous functions are bounded (for example, on a compact interval), $C(X)$ can be equipped with the {{< knowl id="supremum-norm" text="supremum norm" >}} and the associated {{< knowl id="uniform-metric" text="uniform metric" >}}, linking function-space topology to {{< knowl id="uniform-convergence" text="uniform convergence" >}}. Theorems such as {{< knowl id="arzela-ascoli-theorem" text="Arzelà–Ascoli" >}} and {{< knowl id="stone-weierstrass-theorem" text="Stone–Weierstrass" >}} are statements about subsets of $C(X)$.

**Examples:**
- On $[0,1]$, every {{< knowl id="polynomial" text="polynomial" >}} function belongs to $C([0,1])$.
- On $[-1,1]$, the function $f(x)=|x|$ belongs to $C([-1,1])$.
