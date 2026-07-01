+++
id = "lie-groups/center-of-a-lie-algebra"
title = "Center of a Lie algebra"
kind = "knowl"
summary = "Elements that bracket to zero with everything; equivalently, the kernel of ad."
aliases = ["center-of-a-lie-algebra", "Center of a Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/center-of-a-lie-algebra.md"
+++

Let $\mathfrak{g}$ be a [[lie-groups/lie-algebra|Lie algebra]].

**Definition.** The **center** of $\mathfrak{g}$ is
$$
Z(\mathfrak{g})=\{Z\in \mathfrak{g} : [Z,X]=0 \text{ for all } X\in \mathfrak{g}\}.
$$

**Basic properties.**
- $Z(\mathfrak{g})$ is a [[lie-groups/lie-subalgebra|Lie subalgebra]] and in fact an [[lie-groups/ideal-lie-algebra|ideal]] of $\mathfrak{g}$.
- If $\operatorname{ad}:\mathfrak{g}\to \mathfrak{gl}(\mathfrak{g})$ is the [[lie-groups/adjoint-representation-of-a-lie-algebra|adjoint representation]], then
  $$
  Z(\mathfrak{g})=\ker(\operatorname{ad}).
  $$

- $\mathfrak{g}$ is [[lie-groups/abelian-lie-algebra|abelian]] exactly when $Z(\mathfrak{g})=\mathfrak{g}$.

**Context.** The center measures how far $\mathfrak{g}$ is from being faithful under its own adjoint action. It is also the natural coefficient space for central extensions: a quotient by a central ideal is a [[lie-groups/quotient-lie-algebra|quotient Lie algebra]] where “extra commuting directions” have been collapsed.
