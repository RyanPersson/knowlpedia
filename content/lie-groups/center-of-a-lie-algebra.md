---
title: "Center of a Lie algebra"
description: "Elements that bracket to zero with everything; equivalently, the kernel of ad."
---

Let $\mathfrak{g}$ be a {{< knowl id="lie-algebra" text="Lie algebra" >}}.

**Definition.** The **center** of $\mathfrak{g}$ is
$$
Z(\mathfrak{g})=\{Z\in \mathfrak{g} : [Z,X]=0 \text{ for all } X\in \mathfrak{g}\}.
$$

**Basic properties.**
- $Z(\mathfrak{g})$ is a {{< knowl id="lie-subalgebra" text="Lie subalgebra" >}} and in fact an {{< knowl id="ideal-lie-algebra" text="ideal" >}} of $\mathfrak{g}$.
- If $\operatorname{ad}:\mathfrak{g}\to \mathfrak{gl}(\mathfrak{g})$ is the {{< knowl id="adjoint-representation-of-a-lie-algebra" text="adjoint representation" >}}, then
  $$
  Z(\mathfrak{g})=\ker(\operatorname{ad}).
  $$

- $\mathfrak{g}$ is {{< knowl id="abelian-lie-algebra" text="abelian" >}} exactly when $Z(\mathfrak{g})=\mathfrak{g}$.

**Context.** The center measures how far $\mathfrak{g}$ is from being faithful under its own adjoint action. It is also the natural coefficient space for central extensions: a quotient by a central ideal is a {{< knowl id="quotient-lie-algebra" text="quotient Lie algebra" >}} where “extra commuting directions” have been collapsed.
