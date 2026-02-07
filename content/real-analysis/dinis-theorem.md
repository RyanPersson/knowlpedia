---
title: "Dini's theorem"
description: "On a compact space, monotone pointwise convergence of continuous functions to a continuous limit is uniform."
---

**Dini's theorem:** Let $K$ be a compact {{< knowl id="topological-space" section="topology" text="topological space" >}} and let $f_n:K\to\mathbb{R}$ be {{< knowl id="continuous-map" section="topology" text="continuous" >}} for every $n$. Assume $(f_n)$ is monotone in $n$ (either $f_n(x)\le f_{n+1}(x)$ for all $x\in K$, or $f_n(x)\ge f_{n+1}(x)$ for all $x\in K$) and that $f_n\to f$ {{< knowl id="pointwise-convergence" text="pointwise" >}} on $K$, where $f$ is continuous. Then $f_n\to f$ {{< knowl id="uniform-convergence" text="uniformly" >}} on $K$.

This is a compactness-based upgrade from {{< knowl id="pointwise-convergence" text="pointwise convergence" >}} to {{< knowl id="uniform-convergence" text="uniform convergence" >}} under the additional hypothesis of monotonicity, as in a {{< knowl id="monotone-sequence-of-functions" text="monotone sequence of functions" >}}.
