+++
id = "topology/path"
title = "Path"
kind = "knowl"
summary = "A continuous map from the unit interval into a space."
aliases = ["path"]
domains = ["topology"]
legacy_source_path = "topology/path.md"
+++

A **path** in a [[topology/topological-space|topological space]] $X$ is a [[topology/continuous-map|continuous map]] $\gamma\colon [0,1]\to X$, where $[0,1]$ is the [[real-analysis/interval|interval]] with its usual topology. The points $\gamma(0)$ and $\gamma(1)$ are called the initial and terminal points of the path.

Paths are the basic objects used to define [[topology/path-connected-set|path-connectedness]] and are a special case of a [[topology/curve|curve]].

**Examples:**
- In $\mathbb{R}^2$, for points $a,b\in\mathbb{R}^2$, the map $\gamma(t)=(1-t)a+tb$ is a path from $a$ to $b$.
- The map $\gamma(t)=(\cos(2\pi t),\sin(2\pi t))$ is a path in the unit circle with $\gamma(0)=\gamma(1)$ (a loop).
