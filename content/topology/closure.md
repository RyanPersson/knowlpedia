---
title: "Closure"
description: "The smallest closed set containing a given subset."
---

The **closure** of a subset $A\subseteq X$ in a {{< knowl id="topological-space" text="topological space" >}} $(X,\mathcal{T})$ is
\[
\overline{A}=\bigcap\{F\subseteq X : F \text{ is a closed set and } A\subseteq F\}.
\]
Equivalently, a point $x\in X$ lies in $\overline{A}$ if and only if every {{< knowl id="neighborhood" text="neighborhood" >}} of $x$ intersects $A$.

A set $F$ is {{< knowl id="closed-set" text="closed" >}} exactly when $F=\overline{F}$. Closure is closely tied to {{< knowl id="limit-point" text="limit points" >}} and the {{< knowl id="derived-set" text="derived set" >}}.

**Examples:**
- In $\mathbb{R}$ with the usual topology, $\overline{(0,1)}=[0,1]$.
- In $\mathbb{R}$ with the usual topology, $\overline{\mathbb{Q}}=\mathbb{R}$.
- $\overline{\varnothing}=\varnothing$ in any topological space.
