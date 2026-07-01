+++
id = "lie-groups/weight-space"
title = "Weight space"
kind = "knowl"
summary = "For a representation relative to a Cartan subalgebra, is the simultaneous eigenspace with weight ."
aliases = ["weight-space", "Weight space"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/weight-space.md"
+++

### Definition
Let $\mathfrak g$ be a complex Lie algebra, $\mathfrak h\subseteq\mathfrak g$ an abelian subalgebra (typically a [[lie-groups/cartan-subalgebra|Cartan subalgebra]] in the semisimple setting), and let $\rho:\mathfrak g\to\mathfrak{gl}(V)$ be a representation. For $\lambda\in\mathfrak h^\ast$, the **$\lambda$-weight space** is
$$
V_\lambda=\{v\in V\mid \rho(H)v=\lambda(H)v\ \text{for all }H\in\mathfrak h\}.
$$

If $V_\lambda\neq 0$, then $\lambda$ is a [[lie-groups/weight-of-a-representation|weight of the representation]].

### Interaction with roots (semisimple context)
When $\mathfrak g$ is semisimple and $\mathfrak h$ is a Cartan subalgebra, $\mathfrak g$ decomposes into [[lie-groups/root-space|root spaces]] $\mathfrak g_\alpha$ (see [[lie-groups/root-space-decomposition|root space decomposition]]). For $X\in \mathfrak g_\alpha$ and $v\in V_\lambda$, one has
$$
X\cdot v \in V_{\lambda+\alpha},
$$
so root vectors “shift” weights by roots.

### Context
For finite-dimensional representations of semisimple Lie algebras, the action of $\mathfrak h$ is semisimple and one gets a direct sum decomposition
$$
V=\bigoplus_\lambda V_\lambda.
$$
This weight-space decomposition is one of the main inputs to highest-weight methods and depends crucially on complete reducibility phenomena (compare [[lie-groups/weyls-theorem-complete-reducibility|Weyl’s complete reducibility theorem]]).
