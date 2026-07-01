+++
id = "convex-analysis/closed-balls-are-closed-sets"
title = "Closed balls are closed"
kind = "knowl"
summary = "In any metric space, every closed ball is a closed set"
aliases = ["closed-balls-are-closed-sets", "Closed balls are closed"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/closed-balls-are-closed-sets.md"
+++

**Proposition.**
In any metric space, every closed ball $B'(x_0;r)$ is a [[convex-analysis/closed-subset|closed set]].

**Proof sketch.** Show that the complement of $B'(x_0;r)$ is open: if $x\notin B'(x_0;r)$ then $d(x,x_0)>r$. Let $\delta:=d(x,x_0)-r>0$. If $d(y,x)<\delta$, then
$d(y,x_0)\ge d(x,x_0)-d(y,x)>r$, so $y$ also lies outside the closed ball. Hence a ball around $x$ lies in the complement, proving openness of the complement.
