+++
id = "lie-groups/positive-root"
title = "Positive root"
kind = "knowl"
summary = "A choice of “half” of a root set, compatible with addition, used to organize roots into positive and negative."
aliases = ["positive-root", "Positive root"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/positive-root.md"
+++

Let $\Phi$ be a root system in a real inner product space $V$ (see [[lie-groups/root-system|root system]]). A **positive system** (or set of **positive roots**) is a subset $\Phi^+ \subset \Phi$ such that:

1. $\Phi$ is the disjoint union $\Phi = \Phi^+ \sqcup (-\Phi^+)$, and
2. if $\alpha,\beta \in \Phi^+$ and $\alpha+\beta \in \Phi$, then $\alpha+\beta \in \Phi^+$.

Equivalently, choose a linear functional $\lambda \in V^*$ such that $\lambda(\alpha)\neq 0$ for all $\alpha\in\Phi$, and set
\[
\Phi^+ \;=\; \{\alpha\in\Phi : \lambda(\alpha)>0\}.
\]
Geometrically, this corresponds to choosing a Weyl chamber for the hyperplane arrangement $\{\alpha^\perp\}_{\alpha\in\Phi}$; changing the choice is controlled by the [[lie-groups/weyl-group|Weyl group]] action.

In the Lie algebra setting, for a semisimple Lie algebra with a [[lie-groups/cartan-subalgebra|Cartan subalgebra]], the roots (see [[lie-groups/root-lie-algebra|roots of a Lie algebra]]) can be split into positive and negative ones, producing a triangular decomposition (see [[lie-groups/root-space-decomposition|root space decomposition]]). This choice is essential for defining [[lie-groups/simple-root|simple roots]], constructing highest-weight theory, and stating results such as the [[lie-groups/highest-weight-theorem|highest weight theorem]].
