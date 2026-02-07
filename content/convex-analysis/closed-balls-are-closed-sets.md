---
title: "Closed balls are closed"
description: "In any metric space, every closed ball is a closed set"
---

**Proposition.**
In any metric space, every closed ball $B'(x_0;r)$ is a {{< knowl id="closed-subset" text="closed set" >}}.

**Proof sketch.** Show that the complement of $B'(x_0;r)$ is open: if $x\notin B'(x_0;r)$ then $d(x,x_0)>r$. Let $\delta:=d(x,x_0)-r>0$. If $d(y,x)<\delta$, then
$d(y,x_0)\ge d(x,x_0)-d(y,x)>r$, so $y$ also lies outside the closed ball. Hence a ball around $x$ lies in the complement, proving openness of the complement.
