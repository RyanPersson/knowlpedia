---
title: "Restriction of a function"
description: "A function obtained by limiting the domain to a subset"
---

A **restriction of a function** is a new function obtained by limiting the domain: if $f:A\to B$ is a {{< knowl id="function" text="function" >}} and $S\subseteq A$, then the restriction $f|_S:S\to B$ is defined by
$$
f|_S(s)=f(s)\quad\text{for all }s\in S.
$$

A restriction changes the {{< knowl id="domain" text="domain" >}} while keeping the same {{< knowl id="codomain" text="codomain" >}}. The {{< knowl id="graph-of-function" text="graph" >}} of $f|_S$ is obtained by intersecting the graph of $f$ with the subset $S\times B$ of the {{< knowl id="cartesian-product" text="Cartesian product" >}} $A\times B$.

**Examples:**
- If $f:\mathbb{R}\to\mathbb{R}$ is $f(x)=x^2$ and $S=\mathbb{Z}\subseteq\mathbb{R}$, then $f|_S:\mathbb{Z}\to\mathbb{R}$ is the squaring function on integers.
- If $A$ is a set and $S\subseteq A$, then $\mathrm{id}_A|_S:S\to A$ is the inclusion map $s\mapsto s$.
