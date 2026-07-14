---
title: "Compactness implies closedness"
description: "In a metric space, every compact set is closed"
---

**Compactness implies closedness**: If $K$ is a {{< knowl id="compact-set" text="compact set" >}} in a {{< knowl id="metric-space" text="metric space" >}} $(X,d)$, then $K$ is {{< knowl id="closed-set" text="closed" >}}.

**Proof sketch**: Suppose $(x_n)$ is a {{< knowl id="convergent-sequence" text="convergent sequence" >}} in $K$ with $x_n\to x$ in $X$. By compactness, $(x_n)$ has a convergent subsequence $x_{n_k}\to y$ with $y\in K$. In a {{< knowl id="hausdorff-space" text="Hausdorff space" >}} (in particular, in any metric space), limits of sequences are unique, so $y=x$. Hence $x\in K$, showing $K$ is closed.

In general topological spaces, compactness alone does not force closedness; a Hausdorff-type separation assumption is what makes the conclusion topologically valid.

**Examples:**
- In $\mathbb{R}$, every compact set is closed (e.g. $[0,1]$).
- The set $(0,1)$ is not closed, and it is not compact.
