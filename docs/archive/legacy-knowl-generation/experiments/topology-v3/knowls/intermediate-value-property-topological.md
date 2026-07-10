---
title: "Intermediate value property (topological)"
description: "A continuous real-valued function on a connected set takes all intermediate values between any two values."
---

**Topological intermediate value property:** Let $X$ be a {{{< knowl id="topological-space" section="topology-core" text="topological space" >}}}, let $C\subseteq X$ be {{{< knowl id="connected-set" text="connected" >}}}, and let $f:C\to\mathbb{R}$ be a {{{< knowl id="continuous-map" section="topology-core" text="continuous map" >}}}. If $x_0,x_1\in C$ and $y\in\mathbb{R}$ satisfies
\[
\min(f(x_0),f(x_1))\le y\le \max(f(x_0),f(x_1)),
\]
then there exists $x\in C$ such that $f(x)=y$.

Equivalently, the set $f(C)$ (the {{{< knowl id="image" section="shared-foundations" text="image" >}}} of $C$ under $f$) is an interval in $\mathbb{R}$, since {{{< knowl id="continuous-image-of-connected-set-is-connected" text="continuous images of connected sets are connected" >}}} and {{{< knowl id="connected-subsets-of-r-are-intervals" text="connected subsets of $\mathbb{R}$ are intervals" >}}}.
