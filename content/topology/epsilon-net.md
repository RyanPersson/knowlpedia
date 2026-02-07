---
title: "Epsilon-net"
description: "A set of points that approximates a set in a metric space within a fixed tolerance."
---

An **epsilon-net** for a subset $A\subseteq X$ in a {{< knowl id="metric-space" text="metric space" >}} $(X,d)$ is a subset $F\subseteq X$ such that for every $a\in A$ there exists $f\in F$ with
\[
d(a,f) < \varepsilon.
\]
Equivalently, $A\subseteq \bigcup_{f\in F} B(f,\varepsilon)$, where $B(f,\varepsilon)$ is an {{< knowl id="open-ball" text="open ball" >}}.

Finite epsilon-nets are the basic finiteness objects behind {{< knowl id="totally-bounded-set" text="total boundedness" >}}.

**Examples:**
- For $A=[0,1]\subseteq\mathbb{R}$ and $\varepsilon>0$, a finite set of equally spaced points $\{0,\varepsilon,2\varepsilon,\dots,N\varepsilon\}$ with $N\varepsilon\ge 1$ is an epsilon-net for $A$.
- On an infinite set with the discrete metric, any epsilon-net with $\varepsilon<1$ must contain every point of $A$, so $A$ has no finite epsilon-net unless it is finite.
