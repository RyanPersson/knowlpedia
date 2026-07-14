---
title: "Epsilon-nets and finite ball covers"
description: "A finite set of centers whose balls of a given radius cover a set"
---

An **$\varepsilon$-net** for a subset $A$ of a {{{< knowl id="metric-space" section="topology-metric" text="metric space" >}}} $(X,d)$ is a subset $S\subseteq X$ such that
\[
A \subseteq \bigcup_{s\in S} B(s,\varepsilon),
\]
where $B(s,\varepsilon)$ denotes the {{{< knowl id="open-ball" section="topology-metric" text="open ball" >}}} of radius $\varepsilon$ about $s$.

A set $A$ is {{{< knowl id="totally-bounded-set" text="totally bounded" >}}} precisely when it admits a finite $\varepsilon$-net for every $\varepsilon>0$.
