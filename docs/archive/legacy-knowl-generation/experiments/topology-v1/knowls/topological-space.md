---
title: "Topological space"
description: "A set equipped with a topology of open sets."
---

A **topological space** is an ordered pair $(X,\tau)$ where $X$ is a {{< knowl id="set" text="set" >}} and $\tau$ is a {{< knowl id="topology" text="topology" >}} on $X$.

The elements of $\tau$ are the {{< knowl id="open-set" text="open sets" >}}, and they determine notions such as {{< knowl id="neighborhood" text="neighborhoods" >}} and {{< knowl id="continuous-map" text="continuous maps" >}} without requiring distances.

**Examples:**
- Any {{< knowl id="metric-space" text="metric space" >}} becomes a topological space via its {{< knowl id="metric-induced-topology" text="metric-induced topology" >}}.
- The **discrete** topology on $X$ (all subsets are open) makes every function out of $X$ continuous.
- The **indiscrete** topology $\{\varnothing, X\}$ is the smallest possible topology on a nonempty set.
