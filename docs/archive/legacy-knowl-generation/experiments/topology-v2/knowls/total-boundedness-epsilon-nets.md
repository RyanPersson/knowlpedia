---
title: "Epsilon-nets and total boundedness"
description: "Finite epsilon-nets characterize total boundedness in metric spaces"
---

An **epsilon-net** for a set $A$ in a {{< knowl id="metric-space" section="topology-metric" text="metric space" >}} $(X,d)$ is a finite set $F\subseteq X$ such that
\[
A \subseteq \bigcup_{x\in F} B(x,\varepsilon),
\]
where $B(x,\varepsilon)$ denotes the {{< knowl id="open-ball" section="topology-metric" text="open ball" >}} of radius $\varepsilon$.

A set is {{< knowl id="totally-bounded-set" text="totally bounded" >}} exactly when it admits a finite epsilon-net for every $\varepsilon>0$.

**Examples:**
- In $\mathbb R$ with the usual metric, $F=\{0,1/2,1\}$ is a $1/2$-net for $[0,1]$.
- Any finite subset $F$ of a metric space is an epsilon-net for itself for every $\varepsilon>0$.
