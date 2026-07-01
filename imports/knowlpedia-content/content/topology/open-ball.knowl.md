+++
id = "topology/open-ball"
title = "Open ball"
kind = "knowl"
summary = "The set of points within a given radius of a center point in a metric space, using strict inequality."
aliases = ["open-ball", "Open ball"]
domains = ["topology"]
legacy_source_path = "topology/open-ball.md"
+++

An **open ball** in a metric space $(X,d)$ is a set of the form
\[
B_d(x,r)=\{y\in X : d(x,y)<r\},
\]
where $x\in X$ and $r>0$.

Open balls are [[topology/open-set|open sets]] in the [[topology/metric-induced-topology|metric-induced topology]] and they form a [[topology/basis-of-topology|basis]] for that topology; in particular, they are the basic [[topology/neighborhood|neighborhoods]] in metric spaces.

**Examples:**
- In $(\mathbb{R},|\cdot|)$, $B(x,r)=(x-r,x+r)$.
- In the discrete metric on $X$, $B(x,1)=\{x\}$, while $B(x,r)=X$ for any $r>1$.
