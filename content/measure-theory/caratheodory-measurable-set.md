---
title: "Carathéodory measurable set"
description: "A set that satisfies Carathéodory’s splitting condition for an outer measure."
---

A **Carathéodory measurable set** (with respect to an outer measure $\mu^*$ on $X$) is a subset $E\subseteq X$ such that for every subset $S\subseteq X$,
\[
\mu^*(S)=\mu^*(S\cap E)+\mu^*(S\setminus E).
\]

This condition says $E$ “splits” every set $S$ without loss of outer measure, using {{< knowl id="intersection" section="shared-foundations" text="intersection" >}} and {{< knowl id="set-difference" section="shared-foundations" text="set difference" >}}. In the {{< knowl id="caratheodory-construction" text="Carathéodory construction" >}}, the collection of Carathéodory measurable sets forms a {{< knowl id="sigma-algebra" text="sigma-algebra" >}}, and restricting $\mu^*$ to it gives a {{< knowl id="measure" text="measure" >}}.

**Examples:**
- If $\mu^*$ is induced from a measure $\mu$ on a sigma-algebra $\Sigma$ (via the usual infimum over measurable supersets), then every $A\in\Sigma$ is Carathéodory measurable.
- For Lebesgue outer measure on $\mathbb R$, every {{< knowl id="borel-sigma-algebra" text="Borel set" >}} is Carathéodory measurable (and in fact many more sets are as well).
