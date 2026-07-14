---
title: "Baire category theorem"
description: "In a complete metric space, countable intersections of dense open sets are dense."
---

**Baire category theorem:** Let $(X,d)$ be a {{{< knowl id="complete-metric-space" section="topology-metric" text="complete metric space" >}}}, and consider the {{{< knowl id="metric-induced-topology" section="topology-metric" text="topology induced by" >}}} $d$. If $(U_n)_{n\in\mathbb{N}}$ is a sequence of {{{< knowl id="open-set" section="topology-core" text="open" >}}} subsets of $X$ that are {{{< knowl id="dense-set" section="topology-core" text="dense" >}}} in $X$, then $\bigcap_{n\in\mathbb{N}} U_n$ is dense in $X$. Equivalently, if $A_1,A_2,\dots\subseteq X$ are {{{< knowl id="nowhere-dense-set" text="nowhere dense" >}}} in $X$, then $\bigcup_{n\in\mathbb{N}} A_n$ has empty {{{< knowl id="interior" section="topology-core" text="interior" >}}}.

This is commonly summarized as {{{< knowl id="complete-metric-space-is-baire" text="every complete metric space is Baire" >}}}. It explains why {{{< knowl id="meager-set" text="meager sets" >}}} are “small” and why {{{< knowl id="residual-set" text="residual sets" >}}} are “generic,” and it powers the {{{< knowl id="category-argument-template" text="category argument template" >}}}.
