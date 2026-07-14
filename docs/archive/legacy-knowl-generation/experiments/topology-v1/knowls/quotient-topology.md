---
title: "Quotient topology"
description: "The finest topology making a given surjection continuous."
---

Let $p:X\to Y$ be a {{< knowl id="surjective-function" text="surjection" >}} from a topological space $X$ onto a set $Y$. The **quotient topology** on $Y$ is defined by declaring $U\subseteq Y$ to be open if and only if the {{< knowl id="preimage" text="preimage" >}} $p^{-1}(U)$ is an {{< knowl id="open-set" text="open set" >}} in $X$.

With this topology, $p$ is automatically continuous, and it is the finest topology on $Y$ that makes $p$ continuous. A common source of quotient spaces is an {{< knowl id="equivalence-relation" text="equivalence relation" >}} on $X$, where $Y$ is the corresponding {{< knowl id="quotient-set" text="quotient set" >}} and $p$ sends each point to its equivalence class.

**Examples:**
- Identifying $0$ and $1$ in $[0,1]$ produces a quotient space homeomorphic to a circle.
- Collapsing a subset $A\subseteq X$ to a single point is a quotient construction (the fibers form a {{< knowl id="partition" text="partition" >}} of $X$).
