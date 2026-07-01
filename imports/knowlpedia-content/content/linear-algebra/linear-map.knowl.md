+++
id = "linear-algebra/linear-map"
title = "Linear map"
kind = "knowl"
summary = "A function between vector spaces that respects addition and scalar multiplication."
aliases = ["linear-map", "Linear map"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/linear-map.md"
+++

A **linear map** is a [[shared-foundations/function|function]] $T:V\to W$ between [[linear-algebra/vector-space|vector spaces]] over the same field $\mathbb{F}$ such that for all $u,v\in V$ and $a\in\mathbb{F}$,
\[
T(u+v)=T(u)+T(v),\qquad T(a\cdot v)=a\cdot T(v).
\]

As a function, $T$ has [[shared-foundations/domain|domain]] $V$ and [[shared-foundations/codomain|codomain]] $W$. The special case $V=W$ is a [[linear-algebra/linear-operator|linear operator]].

**Examples:**
- For a fixed matrix $A$, the map $T(x)=Ax$ from $\mathbb{F}^n$ to $\mathbb{F}^m$ is linear.
- The derivative map $D:\mathbb{R}[x]\to\mathbb{R}[x]$ given by $D(p)=p'$ is linear.
- The projection $P:\mathbb{R}^2\to\mathbb{R}^2$ defined by $P(x,y)=(x,0)$ is linear.
