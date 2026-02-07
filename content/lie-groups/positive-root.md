---
title: "Positive root"
description: "A choice of “half” of a root set, compatible with addition, used to organize roots into positive and negative."
---

Let $\Phi$ be a root system in a real inner product space $V$ (see {{< knowl id="root-system" text="root system" >}}). A **positive system** (or set of **positive roots**) is a subset $\Phi^+ \subset \Phi$ such that:

1. $\Phi$ is the disjoint union $\Phi = \Phi^+ \sqcup (-\Phi^+)$, and  
2. if $\alpha,\beta \in \Phi^+$ and $\alpha+\beta \in \Phi$, then $\alpha+\beta \in \Phi^+$.

Equivalently, choose a linear functional $\lambda \in V^*$ such that $\lambda(\alpha)\neq 0$ for all $\alpha\in\Phi$, and set
\[
\Phi^+ \;=\; \{\alpha\in\Phi : \lambda(\alpha)>0\}.
\]
Geometrically, this corresponds to choosing a Weyl chamber for the hyperplane arrangement $\{\alpha^\perp\}_{\alpha\in\Phi}$; changing the choice is controlled by the {{< knowl id="weyl-group" text="Weyl group" >}} action.

In the Lie algebra setting, for a semisimple Lie algebra with a {{< knowl id="cartan-subalgebra" text="Cartan subalgebra" >}}, the roots (see {{< knowl id="root-lie-algebra" text="roots of a Lie algebra" >}}) can be split into positive and negative ones, producing a triangular decomposition (see {{< knowl id="root-space-decomposition" text="root space decomposition" >}}). This choice is essential for defining {{< knowl id="simple-root" text="simple roots" >}}, constructing highest-weight theory, and stating results such as the {{< knowl id="highest-weight-theorem" text="highest weight theorem" >}}.
