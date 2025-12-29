---
title: "Norm induces a metric (and conversely)"
description: "A norm defines a metric by d(x,y)=||x−y||; conversely, certain metrics come from norms"
---

**Proposition.**
Let $(X,\|\cdot\|)$ be a {{< knowl id="norm-normed-vector-space" text="normed vector space" >}}. Define
$$
d(x,y):=\|x-y\| \quad \text{for } x,y\in X.
$$
Then $d$ is a {{< knowl id="metric-metric-space" text="metric" >}} on $X$ (hence $(X,d)$ is a metric space).

Conversely, let $X$ be a vector space equipped with a metric $d$ satisfying:
- **translation invariance:** $d(x+z,y+z)=d(x,y)$ for all $x,y,z\in X$,
- **absolute homogeneity:** $d(\alpha x,\alpha y)=|\alpha|\,d(x,y)$ for all scalars $\alpha$ and all $x,y\in X$.

Then $\|x\|:=d(x,0)$ defines a norm on $X$, and $d(x,y)=\|x-y\|$.

**Context.** This identifies norms as exactly the translation-invariant, homogeneous metrics on vector spaces.

**Proof sketch.** For the forward direction, metric axioms follow from the norm axioms; in particular the triangle inequality for $d$ is $\|x-z\|\le \|x-y\|+\|y-z\|$. For the converse, check the norm axioms directly from the two metric properties and the metric triangle inequality.
