---
title: "Almost everywhere"
description: "Holding except on a set of measure zero."
---

A property $P(x)$ is said to hold **almost everywhere** (with respect to a measure $\mu$ on $X$) if there exists a {{< knowl id="null-set" text="null set" >}} $N\subseteq X$ such that $P(x)$ holds for all $x\in X\setminus N$.

This notion depends on the underlying {{< knowl id="measure-space" text="measure space" >}} and is weaker than pointwise validity: changing a function on a null set does not affect almost-everywhere statements. It is also closely tied to the {{< knowl id="symmetric-difference" section="shared-foundations" text="symmetric difference" >}} of sets.

**Examples:**
- Two functions $f,g:X\to\mathbb R$ are equal almost everywhere if $\{x\in X: f(x)\ne g(x)\}$ is a null set.
- For measurable sets $A,B\in\Sigma$, the indicator functions $\mathbf 1_A$ and $\mathbf 1_B$ are equal almost everywhere exactly when $A\triangle B$ is a null set.
