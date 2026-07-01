+++
id = "topology/cantor-intersection-theorem"
title = "Cantor intersection theorem"
kind = "knowl"
summary = "Nested closed sets with diameters going to zero intersect in a single point in a complete metric space"
aliases = ["cantor-intersection-theorem", "Cantor intersection theorem"]
domains = ["topology"]
legacy_source_path = "topology/cantor-intersection-theorem.md"
+++

**Cantor intersection theorem:** Let $(X,d)$ be a [[topology/complete-metric-space|complete metric space]] and let $(F_n)_{n\in\mathbb{N}}$ be a sequence of nonempty [[topology/closed-set|closed sets]] with
1) $F_{n+1}\subseteq F_n$ for all $n$, and
2) $\operatorname{diam}(F_n)\to 0$, where $\operatorname{diam}$ is the [[topology/diameter|diameter]] in the metric $d$.

Then the intersection $\bigcap_{n\in\mathbb{N}} F_n$ consists of exactly one point.

This theorem is the metric-space analogue of the [[topology/nested-interval-theorem|nested interval theorem]] and is a standard tool in fixed-point and completeness arguments.
