---
title: "Connected component"
description: "The maximal connected subset containing a given point"
---

Given a {{< knowl id="topological-space" text="topological space" >}} $X$ and a point $x\in X$, the **connected component** of $x$ is the {{< knowl id="union" text="union" >}} of all {{< knowl id="connected-set" text="connected subsets" >}} of $X$ that contain $x$. Equivalently,
$$
C(x)=\bigcup\{A\subseteq X : x\in A \text{ and } A \text{ is connected}\}.
$$

A connected component is a maximal connected subset of $X$ (it is connected, contains $x$, and is not properly contained in any larger connected subset). The relation “$x$ and $y$ lie in the same connected component” is an {{< knowl id="equivalence-relation" text="equivalence relation" >}}; each component is an {{< knowl id="equivalence-class" text="equivalence class" >}}, and the set of all components forms a {{< knowl id="partition" text="partition" >}} of $X$. In any topological space, each connected component is {{< knowl id="closed-set" text="closed" >}}.

**Examples:**
- In $\mathbb{R}$ with the usual topology, there is a single connected component: all of $\mathbb{R}$.
- In $\mathbb{R}\setminus\{0\}$, there are two connected components: $(-\infty,0)$ and $(0,\infty)$.
- If $X$ has the discrete topology, every singleton $\{x\}$ is a connected component.
