---
title: "Equivalent metrics"
description: "Two metrics that induce the same topology on a set"
---

Two {{< knowl id="metric" text="metrics" >}} $d$ and $d'$ on the same set $X$ are **equivalent** if they induce the same {{< knowl id="metric-induced-topology" text="metric-induced topology" >}}; equivalently, they have the same {{< knowl id="open-set" section="topology-core" text="open sets" >}}.

Equivalently metrized spaces have the same topological notions of {{< knowl id="continuous-map" section="topology-core" text="continuity" >}} and the same convergent sequences, even though their numerical distances and notions like boundedness may differ.

**Examples:**
- If $d'(x,y)=c\,d(x,y)$ for a constant $c>0$, then $d$ and $d'$ are equivalent.
- On $\mathbb{R}$, the metrics $d(x,y)=|x-y|$ and $d'(x,y)=\min\{|x-y|,1\}$ are equivalent.
- On $\mathbb{R}$, the usual metric is not equivalent to the discrete metric (they do not have the same open sets).
