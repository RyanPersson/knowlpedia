---
title: "Open ball"
description: "The set of points within a strict distance of a center in a metric space"
---

An **open ball** in a {{< knowl id="metric-space" text="metric space" >}} $(X,d)$ is a set of the form
\[
B_d(x,r)=\{y\in X : d(x,y)<r\},
\]
where $x\in X$ and $r>0$.

Open balls are {{< knowl id="open-set" section="topology-core" text="open sets" >}} in the {{< knowl id="metric-induced-topology" text="metric-induced topology" >}}, and the family of all open balls forms a {{< knowl id="basis-of-a-topology" section="topology-core" text="basis" >}} for that topology.

**Examples:**
- In $(\mathbb{R},|x-y|)$, $B_d(x,r)=(x-r,x+r)$.
- In the discrete metric on $X$, if $0<r\le 1$ then $B_d(x,r)=\{x\}$, and if $r>1$ then $B_d(x,r)=X$.
