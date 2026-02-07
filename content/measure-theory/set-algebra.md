---
title: "Set algebra"
description: "A collection of subsets closed under complements and finite unions."
---

A **set algebra** on a set $X$ is a nonempty collection $\mathcal A \subseteq \mathcal P(X)$ such that if $A\in\mathcal A$ then $X\setminus A\in\mathcal A$, and if $A,B\in\mathcal A$ then $A\cup B\in\mathcal A$.

Here $\mathcal P(X)$ is the {{< knowl id="power-set" section="shared-foundations" text="power set" >}} of the {{< knowl id="set" section="shared-foundations" text="set" >}} $X$. Closure under complements and finite unions implies closure under finite {{< knowl id="intersection" section="shared-foundations" text="intersections" >}} and finite {{< knowl id="set-difference" section="shared-foundations" text="set differences" >}}. A set algebra is the typical domain for a {{< knowl id="premeasure" text="premeasure" >}}, and every {{< knowl id="sigma-algebra" text="sigma-algebra" >}} is a set algebra.

**Examples:**
- For any $X$, the full collection $\mathcal P(X)$ is a set algebra.
- The family of subsets of $\mathbb R$ that are finite unions of half-open {{< knowl id="interval" section="real-analysis" text="intervals" >}} of the form $[a,b)$ is a set algebra.
- On an infinite set $X$, the collection of all finite subsets of $X$ together with all cofinite subsets of $X$ (those whose complement is finite) is a set algebra.
