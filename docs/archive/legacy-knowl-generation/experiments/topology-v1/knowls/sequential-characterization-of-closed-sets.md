---
title: "Sequential characterization of closed sets"
description: "In a metric space, a set is closed exactly when it contains limits of convergent sequences from it."
---

**Sequential characterization of closed sets (metric spaces)**:  
Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $F\subseteq X$. Then $F$ is a {{< knowl id="closed-set" text="closed set" >}} if and only if for every {{< knowl id="convergent-sequence" text="convergent sequence" >}} $(x_n)$ in $F$, its {{< knowl id="limit-of-a-sequence" text="limit" >}} (when it exists) also lies in $F$.

This gives a practical criterion for closedness using only sequences. Together with the {{< knowl id="sequential-characterization-of-closure" text="sequential characterization of closure" >}}, it explains why the {{< knowl id="closure" text="closure" >}} $\overline{A}$ can be recovered by adding all sequential limit points of $A$.

**Proof sketch** *(metric space case)*:  
If $F$ is closed and $(x_n)\subseteq F$ converges to $x\notin F$, then $X\setminus F$ is open, so it contains some {{< knowl id="open-ball" text="open ball" >}} around $x$ disjoint from $F$, contradicting $x_n\to x$.  
Conversely, assume the sequential condition. If $x\notin F$ and every open ball around $x$ met $F$, one could choose $x_n\in F$ with $d(x_n,x)<1/n$, producing a sequence in $F$ converging to $x$, a contradiction. Hence some ball around $x$ misses $F$, so $X\setminus F$ is open and $F$ is closed.

**Examples:**
- In $\mathbb{R}$ with the usual metric, $[0,1]$ is closed: any convergent sequence in $[0,1]$ has its limit still in $[0,1]$.
- The interval $(0,1)$ is not closed: the sequence $x_n=1/n$ lies in $(0,1)$ but converges to $0\notin(0,1)$.
