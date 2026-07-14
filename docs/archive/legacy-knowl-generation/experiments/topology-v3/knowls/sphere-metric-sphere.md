---
title: "Metric sphere"
description: "The set of points at exactly distance r from a center point."
---

A **metric sphere** in a metric space $(X,d)$ is a set of the form
\[
S(x,r)=\{\,y\in X : d(x,y)=r\,\},
\]
where $x\in X$ and $r\ge 0$.

For $r>0$, the sphere sits between the {{{< knowl id="open-ball" text="open ball" >}}} and {{{< knowl id="closed-ball" text="closed ball" >}}} of radius $r$ in the sense that $S(x,r)\subseteq \overline{B}(x,r)$ and $S(x,r)\cap B(x,r)=\varnothing$.

**Examples:**
- In $\mathbb{R}$ with the usual metric and $r>0$, $S(a,r)=\{a-r,a+r\}$.
