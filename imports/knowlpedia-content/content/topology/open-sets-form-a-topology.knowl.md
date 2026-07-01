+++
id = "topology/open-sets-form-a-topology"
title = "Open sets form a topology"
kind = "knowl"
summary = "In a metric space, unions of open sets are open and finite intersections of open sets are open"
aliases = ["open-sets-form-a-topology", "Open sets form a topology"]
domains = ["topology"]
legacy_source_path = "topology/open-sets-form-a-topology.md"
+++

**Open sets form a topology**: Let $(X,d)$ be a [[topology/metric-space|metric space]]. Then:
- $\varnothing$ and $X$ are [[topology/open-set|open]];
- arbitrary unions of open sets are open: if $\{U_\alpha\}_{\alpha\in A}$ are open, then $\bigcup_{\alpha\in A} U_\alpha$ is open;
- finite intersections of open sets are open: if $U_1,\dots,U_n$ are open, then $\bigcap_{j=1}^n U_j$ is open.

These closure properties justify treating "open sets" as the primitive objects defining the topological structure induced by a [[topology/metric|metric]].
