---
title: "Totally bounded set"
description: "A metric-space set that can be covered by finitely many small-radius balls at every scale"
---

A **totally bounded set** $A$ in a {{{< knowl id="metric-space" section="topology-metric" text="metric space" >}}} $(X,d)$ is a subset such that for every $\varepsilon>0$ there exist points $x_1,\dots,x_n\in X$ with
\[
A \subseteq B(x_1,\varepsilon)\cup\cdots\cup B(x_n,\varepsilon),
\]
where each $B(x_i,\varepsilon)$ is an {{{< knowl id="open-ball" section="topology-metric" text="open ball" >}}}.

Equivalently, $A$ is totally bounded if it has a finite {{{< knowl id="total-boundedness-epsilon-nets" text="epsilon-net" >}}} at every scale. Total boundedness is stronger than being {{{< knowl id="bounded-set" section="topology-metric" text="bounded" >}}} and is central in the metric characterization {{{< knowl id="compact-iff-complete-totally-bounded" text="compact iff complete and totally bounded" >}}}.

**Examples:**
- In $\mathbb R$ with the usual metric, $[0,1]$ is totally bounded.
- $\mathbb R$ is not totally bounded.
