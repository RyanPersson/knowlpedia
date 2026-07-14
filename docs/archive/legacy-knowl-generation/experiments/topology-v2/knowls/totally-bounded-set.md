---
title: "Totally bounded set"
description: "A metric-space set that can be covered by finitely many small balls at every scale"
---

A **totally bounded set** $A$ in a {{< knowl id="metric-space" section="topology-metric" text="metric space" >}} $(X,d)$ is a set such that for every $\varepsilon>0$ there exist points $x_1,\dots,x_n\in X$ with
\[
A \subseteq B(x_1,\varepsilon)\cup\cdots\cup B(x_n,\varepsilon),
\]
where $B(x,\varepsilon)$ is the {{< knowl id="open-ball" section="topology-metric" text="open ball" >}} of radius $\varepsilon$.

Equivalently, $A$ admits finite {{< knowl id="total-boundedness-epsilon-nets" text="epsilon-nets" >}} at every scale. Total boundedness is stronger than being {{< knowl id="bounded-set" section="topology-metric" text="bounded" >}}.

**Examples:**
- Every compact set in a metric space is totally bounded (see {{< knowl id="compactness-implies-total-boundedness" text="compactness implies total boundedness" >}}).
- The set $\mathbb Z\subset\mathbb R$ is bounded in no ball and is not totally bounded.
- The open interval $(0,1)\subset\mathbb R$ is totally bounded, even though it is not compact.
