+++
id = "topology/image-compact-connected-is-interval"
title = "Image of a compact connected set is an interval"
kind = "knowl"
summary = "A continuous real-valued function on a compact connected space has an interval as its image."
aliases = ["image-compact-connected-is-interval", "Image of a compact connected set is an interval"]
domains = ["topology"]
legacy_source_path = "topology/image-compact-connected-is-interval.md"
+++

**Image of compact connected is an interval:** Let $X$ be a [[topology/compact-set|compact]] and [[topology/connected-set|connected]] topological space, and let $f:X\to\mathbb{R}$ be a [[topology/continuous-map|continuous map]]. Then $f(X)\subseteq\mathbb{R}$ is a compact interval: there exist real numbers $m\le M$ such that
\[
f(X)=[m,M].
\]
Equivalently, $f(X)$ is an [[real-analysis/interval|interval]] that is also compact in $\mathbb{R}$.

This follows by combining [[topology/continuous-image-of-compact-set-is-compact|continuous images of compact sets are compact]], [[topology/continuous-image-of-connected-set-is-connected|continuous images of connected sets are connected]], and the classification [[topology/connected-subsets-of-r-are-intervals|connected subsets of R are intervals]]; the endpoints $m$ and $M$ align with [[topology/continuous-attains-max-min-compact|attainment of maxima and minima on compact sets]].
