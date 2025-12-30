---
title: "Submodule"
description: "An additive subgroup closed under the scalar action of a module."
---

Let $M$ be a left $R$-{{< knowl id="module" text="module" >}}. A **submodule** of $M$ is a {{< knowl id="subset" text="subset" >}} $N\subseteq M$ such that:
1. $0\in N$,
2. $n_1,n_2\in N \Rightarrow n_1-n_2\in N$,
3. $r\in R$ and $n\in N \Rightarrow rn\in N$.

Equivalently, $N$ is an additive subgroup of $(M,+)$ that is stable under scalar multiplication. Practical closure tests are summarized in the {{< knowl id="submodule-criterion" text="submodule criterion" >}}.

**Examples:**
- In the $\mathbb Z$-module $M=\mathbb Z^2$, the set $N=\{(2a,2b):a,b\in\mathbb Z\}$ is a submodule.
- If $R$ is a ring, any {{< knowl id="ideal" text="ideal" >}} $I\lhd R$ is a submodule of the left $R$-module $R$.
- (Edge case) The sets $\{0\}$ and $M$ are always submodules; a module is {{< knowl id="simple-module" text="simple" >}} exactly when these are the only submodules.
