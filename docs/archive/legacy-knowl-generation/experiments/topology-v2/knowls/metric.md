---
title: "Metric"
description: "A distance function on a set satisfying symmetry and the triangle inequality"
---

A **metric** on a {{< knowl id="set" section="shared-foundations" text="set" >}} $X$ is a {{< knowl id="function" section="shared-foundations" text="function" >}} $d: X\times X\to[0,\infty)$ such that for all $x,y,z\in X$:
- (Positivity/identity) $d(x,y)\ge 0$, and $d(x,y)=0$ if and only if $x=y$.
- (Symmetry) $d(x,y)=d(y,x)$.
- (Triangle inequality) $d(x,z)\le d(x,y)+d(y,z)$.

Given a metric $d$, the pair $(X,d)$ is a {{< knowl id="metric-space" text="metric space" >}}, and the {{< knowl id="open-ball" text="open balls" >}} for $d$ generate the {{< knowl id="metric-induced-topology" text="metric-induced topology" >}}.

**Examples:**
- On $\mathbb{R}^n$, $d(x,y)=\|x-y\|_2$, where $\|\cdot\|_2$ denotes the {{< knowl id="euclidean-norm" section="linear-algebra" text="Euclidean norm" >}}.
- The discrete metric on any set $X$: $d(x,y)=0$ if $x=y$, and $d(x,y)=1$ otherwise.
- If $\|\cdot\|$ is a {{< knowl id="norm" section="linear-algebra" text="norm" >}} on a {{< knowl id="vector-space" section="linear-algebra" text="vector space" >}}, then $d(x,y)=\|x-y\|$ is a metric.
