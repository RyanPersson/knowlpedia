---
title: "Image of a compact connected set is an interval"
description: "A continuous real-valued function on a compact connected space has an interval as its image."
---

**Image of compact connected is an interval:** Let $X$ be a {{< knowl id="compact-set" text="compact" >}} and {{< knowl id="connected-set" text="connected" >}} topological space, and let $f:X\to\mathbb{R}$ be a {{< knowl id="continuous-map" text="continuous map" >}}. Then $f(X)\subseteq\mathbb{R}$ is a compact interval: there exist real numbers $m\le M$ such that
\[
f(X)=[m,M].
\]
Equivalently, $f(X)$ is an {{< knowl id="interval" section="real-analysis" text="interval" >}} that is also compact in $\mathbb{R}$.

This follows by combining {{< knowl id="continuous-image-of-compact-set-is-compact" text="continuous images of compact sets are compact" >}}, {{< knowl id="continuous-image-of-connected-set-is-connected" text="continuous images of connected sets are connected" >}}, and the classification {{< knowl id="connected-subsets-of-r-are-intervals" text="connected subsets of R are intervals" >}}; the endpoints $m$ and $M$ align with {{< knowl id="continuous-attains-max-min-compact" text="attainment of maxima and minima on compact sets" >}}.
