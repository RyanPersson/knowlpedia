---
title: "Sigma-algebra"
description: "A collection of subsets closed under complements and countable unions."
---

A **sigma-algebra** on a set $X$ is a nonempty collection $\Sigma \subseteq \mathcal P(X)$ such that if $A\in\Sigma$ then $X\setminus A\in\Sigma$, and whenever $(A_n)_{n\ge 1}$ is a sequence in $\Sigma$, the union $\bigcup_{n=1}^\infty A_n$ lies in $\Sigma$.

Equivalently, $\Sigma$ contains $X$ and is closed under complements and countable {{< knowl id="union" section="shared-foundations" text="unions" >}}; it then automatically contains the {{< knowl id="empty-set" section="shared-foundations" text="empty set" >}} and is closed under countable {{< knowl id="intersection" section="shared-foundations" text="intersections" >}}. Sigma-algebras define {{< knowl id="measurable-space" text="measurable spaces" >}} and are the domains of {{< knowl id="measure" text="measures" >}}.

**Examples:**
- For any $X$, the {{< knowl id="power-set" section="shared-foundations" text="power set" >}} $\mathcal P(X)$ is a sigma-algebra.
- On $\mathbb R$ with its usual topology, the {{< knowl id="borel-sigma-algebra" text="Borel sigma-algebra" >}} is a sigma-algebra.
- The “trivial” sigma-algebra $\{\varnothing, X\}$ is a sigma-algebra on any set $X$.
