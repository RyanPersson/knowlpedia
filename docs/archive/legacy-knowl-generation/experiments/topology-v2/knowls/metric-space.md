---
title: "Metric space"
description: "A set equipped with a metric that determines distances and convergence"
---

A **metric space** is a pair $(X,d)$ where $X$ is a {{< knowl id="set" section="shared-foundations" text="set" >}} and $d$ is a {{< knowl id="metric" text="metric" >}} on $X$.

Every metric space carries a canonical {{< knowl id="metric-induced-topology" text="metric-induced topology" >}}, so it is a special case of a {{< knowl id="topological-space" section="topology-core" text="topological space" >}}.

**Examples:**
- $(\mathbb{R},d)$ with $d(x,y)=|x-y|$.
- $(\mathbb{R}^n,d)$ with $d(x,y)=\|x-y\|_2$, where $\|\cdot\|_2$ is the {{< knowl id="euclidean-norm" section="linear-algebra" text="Euclidean norm" >}}.
- Any set $X$ with the discrete metric.
