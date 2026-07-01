+++
id = "topology/homeomorphism"
title = "Homeomorphism"
kind = "knowl"
summary = "A bijective continuous map with a continuous inverse."
aliases = ["homeomorphism"]
domains = ["topology"]
legacy_source_path = "topology/homeomorphism.md"
+++

A **homeomorphism** between [[topology/topological-space|topological spaces]] $X$ and $Y$ is a [[shared-foundations/bijective-function|bijective function]] $f:X\to Y$ such that $f$ is a [[topology/continuous-map|continuous map]] and its [[shared-foundations/inverse-function|inverse function]] $f^{-1}:Y\to X$ is also continuous.

If there exists a homeomorphism between $X$ and $Y$, the spaces are called *homeomorphic*; this means they are “the same” from the topological viewpoint, sharing properties like [[topology/compact-set|compactness]] and [[topology/connected-set|connectedness]].

**Examples:**
- The map $f:(0,1)\to\mathbb{R}$ given by $f(x)=\tan(\pi(x-\tfrac12))$ is a homeomorphism.
- The map $g:\mathbb{R}\to(0,\infty)$ given by $g(x)=e^x$ is a homeomorphism.
- If two spaces have exactly the same open sets, the identity map between them is a homeomorphism.
