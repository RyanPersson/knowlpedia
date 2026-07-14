---
title: "Image of compact connected set is an interval"
description: "A continuous real-valued function on a compact connected space has an interval as its image"
---

**Image of compact connected set is an interval:** Let $X$ be a {{< knowl id="topological-space" section="topology-core" text="topological space" >}}, let $K\subseteq X$ be {{< knowl id="compact-set" section="topology-compactness" text="compact" >}} and {{< knowl id="connected-set" text="connected" >}}, and let $f:K\to \mathbb{R}$ be a {{< knowl id="continuous-map" section="topology-core" text="continuous map" >}}. Then $f(K)\subseteq \mathbb{R}$ is a compact interval (possibly a single point).

More concretely, {{< knowl id="continuous-image-of-compact-set-is-compact" section="topology-compactness" text="compactness is preserved by continuous maps" >}} and {{< knowl id="continuous-image-of-connected-set-is-connected" text="connectedness is preserved by continuous maps" >}}, so $f(K)$ is compact and connected in $\mathbb{R}$; by {{< knowl id="connected-subsets-of-r-are-intervals" text="connected subsets of R are intervals" >}} it is an interval, and by {{< knowl id="continuous-attains-max-min-compact" section="topology-compactness" text="attainment of maxima and minima on compact sets" >}} it can be written as $[m,M]$ where $m=\min f(K)$ and $M=\max f(K)$.
