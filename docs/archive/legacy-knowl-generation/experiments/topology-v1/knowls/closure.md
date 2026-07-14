---
title: "Closure"
description: "The smallest closed set containing a given set."
---

Let $(X,\tau)$ be a topological space and let $A\subseteq X$. The **closure** of $A$, denoted $\overline{A}$, is the smallest {{< knowl id="closed-set" text="closed set" >}} containing $A$; equivalently,
$$
\overline{A}=\bigcap\{F\supseteq A : F \text{ is closed}\}.
$$

A point $x$ lies in $\overline{A}$ exactly when every {{< knowl id="neighborhood" text="neighborhood" >}} of $x$ meets $A$. The closure is closely related to {{< knowl id="limit-point-accumulation-point-cluster-point" text="limit points" >}} and the {{< knowl id="derived-set" text="derived set" >}}.

**Examples:**
- In $\mathbb{R}$ with the usual topology, $\overline{(0,1)}=[0,1]$.
- $\overline{\varnothing}=\varnothing$ and $\overline{X}=X$.
- A subset $A$ is dense precisely when $\overline{A}=X$ (see {{< knowl id="dense-set" text="dense set" >}}).
