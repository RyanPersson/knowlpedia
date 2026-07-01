+++
id = "topology/closed-ball"
title = "Closed ball"
kind = "knowl"
summary = "The set of points within a given radius of a center point in a metric space, using non-strict inequality."
aliases = ["closed-ball", "Closed ball"]
domains = ["topology"]
legacy_source_path = "topology/closed-ball.md"
+++

A **closed ball** in a metric space $(X,d)$ is a set of the form
\[
\overline{B}_d(x,r)=\{y\in X : d(x,y)\le r\},
\]
where $x\in X$ and $r\ge 0$.

Closed balls are closely related to [[topology/open-ball|open balls]] and are [[topology/closed-set|closed sets]] in the [[topology/metric-induced-topology|metric-induced topology]].

**Examples:**
- In $(\mathbb{R},|\cdot|)$, $\overline{B}(x,r)=[x-r,x+r]$.
- In the discrete metric on $X$, $\overline{B}(x,0)=\{x\}$ and $\overline{B}(x,1)=X$.
