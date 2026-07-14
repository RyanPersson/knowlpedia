---
title: "Intermediate value property in topology"
description: "A continuous real-valued map on a connected space takes all intermediate values"
---

**Intermediate value property (topological form)**: Let $X$ be a {{< knowl id="connected-set" text="connected" >}} topological space and let $f:X\to\mathbb{R}$ be a {{< knowl id="continuous-map" text="continuous map" >}}. If $x_0,x_1\in X$ and $y\in\mathbb{R}$ lies between $f(x_0)$ and $f(x_1)$, then there exists $x\in X$ such that $f(x)=y$.

This is a direct consequence of {{< knowl id="continuous-image-of-connected-set-is-connected" text="continuous images of connected sets are connected" >}}: the {{< knowl id="image" text="image" >}} $f(X)$ is connected in $\mathbb{R}$, hence (by {{< knowl id="connected-subsets-of-r-are-intervals" text="connected subsets of the real line are intervals" >}}) it is an interval and must contain every intermediate value.

**Proof sketch** *(optional)*: Since $X$ is connected and $f$ is continuous, $f(X)$ is connected. Connected subsets of $\mathbb{R}$ are intervals, and intervals contain all values between any two of their points. Apply this to $f(x_0)$ and $f(x_1)$.

**Examples:**
- Taking $X=[a,b]\subseteq\mathbb{R}$ recovers the classical intermediate value theorem for continuous functions on an interval.
- If $X$ is connected and $f$ is continuous, $f$ cannot take only the two values $0$ and $1$ unless it is constant.
