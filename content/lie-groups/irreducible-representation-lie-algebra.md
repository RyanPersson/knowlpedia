---
title: "Irreducible representation of a Lie algebra"
description: "A representation with no nontrivial invariant subspaces."
---

Let $\mathfrak g$ be a {{< knowl id="lie-algebra" text="Lie algebra" >}} and let $\rho:\mathfrak g\to \mathfrak{gl}(V)$ be a {{< knowl id="representation-of-a-lie-algebra" text="representation" >}} on a finite-dimensional vector space $V$.

**Definition (Irreducible).**  
The representation $(\rho,V)$ is **irreducible** if the only $\mathfrak g$-invariant subspaces of $V$ are $\{0\}$ and $V$. Equivalently, $V$ is a simple $\mathfrak g$-module.

A subspace $W\subseteq V$ is $\mathfrak g$-invariant precisely when $\rho(x)W\subseteq W$ for all $x\in\mathfrak g$; such a $W$ is a {{< knowl id="subrepresentation-lie-algebra" text="subrepresentation" >}}.

**Context.**  
Irreducibles are the building blocks for representation theory. For semisimple $\mathfrak g$, every finite-dimensional representation is completely reducible (see {{< knowl id="weyls-theorem-complete-reducibility" text="Weyl's theorem" >}} and {{< knowl id="completely-reducible-representation-lie" text="complete reducibility" >}}), and irreducibles are classified by the {{< knowl id="highest-weight-theorem" text="highest-weight theorem" >}}.
