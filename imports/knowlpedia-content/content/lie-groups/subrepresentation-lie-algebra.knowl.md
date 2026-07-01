+++
id = "lie-groups/subrepresentation-lie-algebra"
title = "Subrepresentation of a Lie algebra"
kind = "knowl"
summary = "An invariant subspace for a Lie algebra representation, i.e. a -submodule."
aliases = ["subrepresentation-lie-algebra", "Subrepresentation of a Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/subrepresentation-lie-algebra.md"
+++

### Definition
Let $\mathfrak g$ be a Lie algebra and let $\rho:\mathfrak g\to \mathfrak{gl}(V)$ be a [[lie-groups/representation-of-a-lie-algebra|representation of $\\mathfrak g$]] on a finite-dimensional vector space $V$. A linear subspace $W\subseteq V$ is a **subrepresentation** (or **$\mathfrak g$-submodule**) if it is invariant under the action:
$$
\rho(X)(W)\subseteq W \quad \text{for all } X\in\mathfrak g.
$$

In this case, restricting $\rho(X)$ to $W$ defines a representation $\rho|_W:\mathfrak g\to \mathfrak{gl}(W)$.

### Quotients and irreducibility
If $W\subseteq V$ is a subrepresentation, then the quotient space $V/W$ inherits a natural $\mathfrak g$-action via
$$
X\cdot (v+W) = (X\cdot v)+W,
$$

well-defined precisely because $W$ is invariant. A representation is **irreducible** (see [[lie-groups/irreducible-representation-lie-algebra|irreducible representations]]) if its only subrepresentations are $\{0\}$ and $V$.

### Why this matters
Subrepresentations are the “building blocks” for decomposing representations. When $\mathfrak g$ is semisimple, Weyl’s complete reducibility theorem (see [[lie-groups/weyls-theorem-complete-reducibility|Weyl’s theorem on complete reducibility]]) says every subrepresentation has an invariant complement, so finite-dimensional representations split as direct sums rather than forming nontrivial extensions.
