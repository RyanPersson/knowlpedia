---
title: "Open ball"
description: "The set of points within a given radius of a center point in a metric space, using strict inequality."
---

An **open ball** in a metric space $(X,d)$ is a set of the form
\[
B_d(x,r)=\{y\in X : d(x,y)<r\},
\]
where $x\in X$ and $r>0$.

Open balls are {{< knowl id="open-set" text="open sets" >}} in the {{< knowl id="metric-induced-topology" text="metric-induced topology" >}} and they form a {{< knowl id="basis-of-topology" text="basis" >}} for that topology; in particular, they are the basic {{< knowl id="neighborhood" text="neighborhoods" >}} in metric spaces.

**Examples:**
- In $(\mathbb{R},|\cdot|)$, $B(x,r)=(x-r,x+r)$.
- In the discrete metric on $X$, $B(x,1)=\{x\}$, while $B(x,r)=X$ for any $r>1$.
