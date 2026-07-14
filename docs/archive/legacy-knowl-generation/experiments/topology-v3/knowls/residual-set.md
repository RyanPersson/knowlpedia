---
title: "Residual set"
description: "A subset whose complement is meager, also called comeager."
---

A subset $R\subseteq X$ of a {{{< knowl id="topological-space" section="topology-core" text="topological space" >}}} $X$ is **residual** (or **comeager**) in $X$ if its {{{< knowl id="complement" section="shared-foundations" text="complement" >}}} $X\setminus R$ is {{{< knowl id="meager-set" text="meager" >}}} in $X$.

Every residual set contains a countable intersection of open dense sets: if $X\setminus R=\bigcup_{n\in\mathbb{N}} N_n$ with each $N_n$ nowhere dense, then using {{{< knowl id="closure" section="topology-core" text="closures" >}}} gives
$$\bigcap_{n\in\mathbb{N}} \bigl(X\setminus \overline{N_n}\bigr)\subseteq R,$$
and each $X\setminus \overline{N_n}$ is open and {{{< knowl id="dense-set" section="topology-core" text="dense" >}}}. In a {{{< knowl id="baire-space" text="Baire space" >}}}, every residual set is dense, so residual sets capture properties that hold for “generic” points.

**Examples:**
- In $\mathbb{R}$ with the usual topology, the irrationals $\mathbb{R}\setminus\mathbb{Q}$ form a residual set because $\mathbb{Q}$ is meager.
