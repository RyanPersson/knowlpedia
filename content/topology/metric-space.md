---
title: "Metric space"
description: "A set equipped with a metric that measures distances between its points."
---

A **metric space** is a pair $(X,d)$ where $X$ is a {{< knowl id="set" section="shared-foundations" text="set" >}} and $d$ is a {{< knowl id="metric" text="metric" >}} on $X$.

Every metric space determines a {{< knowl id="topological-space" text="topological space" >}} via the {{< knowl id="metric-induced-topology" text="metric-induced topology" >}}, whose basic neighborhoods are {{< knowl id="open-ball" text="open balls" >}}.

**Examples:**
- $(\mathbb{R},d)$ with $d(x,y)=|x-y|$.
- Any set $X$ with the discrete metric $d(x,y)\in\{0,1\}$.
