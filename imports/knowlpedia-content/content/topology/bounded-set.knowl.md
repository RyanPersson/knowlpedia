+++
id = "topology/bounded-set"
title = "Bounded set"
kind = "knowl"
summary = "A subset of a metric space that lies inside some ball of finite radius."
aliases = ["bounded-set", "Bounded set"]
domains = ["topology"]
legacy_source_path = "topology/bounded-set.md"
+++

A **bounded set** in a metric space $(X,d)$ is a subset $A\subseteq X$ for which there exist $x_0\in X$ and $R>0$ such that $A\subseteq B_d(x_0,R)$, where $B_d(x_0,R)$ is the [[topology/open-ball|open ball]] of radius $R$ around $x_0$.

Equivalently, $A$ is bounded if and only if its [[topology/diameter|diameter]] is finite. Boundedness is a basic size condition that appears in notions such as [[topology/totally-bounded-set|total boundedness]].

**Examples:**
- Any (open or closed) ball of finite radius is bounded.
- In $(\mathbb{R},|\cdot|)$, the interval $(0,1)$ is bounded, while $(0,\infty)$ is not.
