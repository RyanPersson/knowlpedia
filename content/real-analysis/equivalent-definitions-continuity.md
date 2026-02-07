---
title: "Equivalent definitions of continuity (metric spaces)"
description: "Epsilon–delta, sequential continuity, and open-set preimages are equivalent in metric spaces"
---

Let $(X,d_X)$ and $(Y,d_Y)$ be {{< knowl id="metric-space" section="topology" text="metric spaces" >}}, and let $f:X\to Y$.

Fix a point $x_0\in X$. The following are equivalent:

- **Epsilon–delta continuity at $x_0$**: for every $\varepsilon>0$ there exists $\delta>0$ such that
  $
  d_X(x,x_0)<\delta \implies d_Y(f(x),f(x_0))<\varepsilon.
  $
- **Sequential continuity at $x_0$**: for every {{< knowl id="convergent-sequence" section="topology" text="sequence" >}} $(x_n)$ in $X$,
  $
  x_n\to x_0 \implies f(x_n)\to f(x_0).
  $
- **Neighborhood formulation**: for every {{< knowl id="open-set" section="topology" text="open" >}} set $V\subseteq Y$ with $f(x_0)\in V$, there exists $\delta>0$ such that
  $
  B_X(x_0,\delta)\subseteq f^{-1}(V).
  $

Moreover, $f$ is {{< knowl id="continuity-on-a-set" text="continuous" >}} on all of $X$ if and only if **preimages of open sets are open**:
$
V\subseteq Y \text{ open} \implies f^{-1}(V)\subseteq X \text{ open}.
$

These equivalences let you choose the most convenient continuity definition for a given proof.
