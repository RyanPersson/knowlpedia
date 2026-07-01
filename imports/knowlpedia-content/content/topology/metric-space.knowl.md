+++
id = "topology/metric-space"
title = "Metric space"
kind = "knowl"
summary = "A set equipped with a metric that measures distances between its points."
aliases = ["metric-space", "Metric space"]
domains = ["topology"]
legacy_source_path = "topology/metric-space.md"
+++

A **metric space** is a pair $(X,d)$ where $X$ is a [[shared-foundations/set|set]] and $d$ is a [[topology/metric|metric]] on $X$.

Every metric space determines a [[topology/topological-space|topological space]] via the [[topology/metric-induced-topology|metric-induced topology]], whose basic neighborhoods are [[topology/open-ball|open balls]].

**Examples:**
- $(\mathbb{R},d)$ with $d(x,y)=|x-y|$.
- Any set $X$ with the discrete metric $d(x,y)\in\{0,1\}$.
