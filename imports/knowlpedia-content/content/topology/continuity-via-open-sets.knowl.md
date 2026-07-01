+++
id = "topology/continuity-via-open-sets"
title = "Continuity via open sets"
kind = "knowl"
summary = "A function is continuous iff the preimage of every open set is open"
aliases = ["continuity-via-open-sets", "Continuity via open sets"]
domains = ["topology"]
legacy_source_path = "topology/continuity-via-open-sets.md"
+++

**Continuity via open sets**: Let $(X,d_X)$ and $(Y,d_Y)$ be [[topology/metric-space|metric spaces]] and $f:X\to Y$. Then $f$ is [[real-analysis/continuity-on-a-set|continuous]] (at every point) if and only if for every [[topology/open-set|open set]] $V\subseteq Y$, the [[real-analysis/preimage-inverse-image|preimage]]
$f^{-1}(V)=\{x\in X: f(x)\in V\}$
is open in $X$.

This formulation is fundamental in topology and makes continuity compatible with [[shared-foundations/composition-of-functions|compositions]] and other structural operations.
