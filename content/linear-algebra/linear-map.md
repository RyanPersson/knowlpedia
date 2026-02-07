---
title: "Linear map"
description: "A function between vector spaces that respects addition and scalar multiplication."
---

A **linear map** is a {{< knowl id="function" section="shared-foundations" text="function" >}} $T:V\to W$ between {{< knowl id="vector-space" text="vector spaces" >}} over the same field $\mathbb{F}$ such that for all $u,v\in V$ and $a\in\mathbb{F}$,
\[
T(u+v)=T(u)+T(v),\qquad T(a\cdot v)=a\cdot T(v).
\]

As a function, $T$ has {{< knowl id="domain" section="shared-foundations" text="domain" >}} $V$ and {{< knowl id="codomain" section="shared-foundations" text="codomain" >}} $W$. The special case $V=W$ is a {{< knowl id="linear-operator" text="linear operator" >}}.

**Examples:**
- For a fixed matrix $A$, the map $T(x)=Ax$ from $\mathbb{F}^n$ to $\mathbb{F}^m$ is linear.
- The derivative map $D:\mathbb{R}[x]\to\mathbb{R}[x]$ given by $D(p)=p'$ is linear.
- The projection $P:\mathbb{R}^2\to\mathbb{R}^2$ defined by $P(x,y)=(x,0)$ is linear.
