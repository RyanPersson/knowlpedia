+++
id = "topology/connected-set"
title = "Connected set"
kind = "knowl"
summary = "A set that cannot be split into two disjoint nonempty open pieces in the subspace topology."
aliases = ["connected-set", "Connected set"]
domains = ["topology"]
legacy_source_path = "topology/connected-set.md"
+++

A **connected set** is a subset $C\subseteq X$ of a [[topology/topological-space|topological space]] $X$ such that there do not exist disjoint nonempty sets $U,V\subseteq C$ that are [[topology/open-set|open]] in the [[topology/subspace-topology|subspace topology]] on $C$ and satisfy $C=U\cup V$.
Equivalently, the only subsets of $C$ that are both [[topology/open-set|open]] and [[topology/closed-set|closed]] in the subspace topology are $\varnothing$ and $C$.

Connectedness is a basic qualitative invariant of spaces, and it is preserved by [[topology/continuous-map|continuous maps]] (see [[topology/continuous-image-of-connected-set-is-connected|continuous images of connected sets]]). Maximal connected pieces are called [[topology/connected-component|connected components]].

**Examples:**
- Any [[real-analysis/interval|interval]] in $\mathbb{R}$ (with the usual topology) is connected.
- The set $(-1,0)\cup(0,1)\subseteq\mathbb{R}$ is not connected.
