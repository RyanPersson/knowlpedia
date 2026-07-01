+++
id = "fiber-bundles/lie-algebra-valued-k-form"
title = "Lie-algebra-valued k-form"
kind = "knowl"
summary = "A differential form whose values lie in a fixed Lie algebra."
aliases = ["lie-algebra-valued-k-form", "Lie-algebra-valued k-form"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/lie-algebra-valued-k-form.md"
+++

Let $M$ be a smooth manifold and let [[lie-groups/lie-algebra|Lie algebra]] $\mathfrak{g}$ be fixed.

A **$\mathfrak{g}$-valued differential k-form** on $M$ is a smooth section of the vector bundle
\[
\Lambda^k T^*M \otimes \mathfrak{g} \;\longrightarrow\; M.
\]
Equivalently, it is a smoothly varying alternating multilinear map
\[
\alpha_x : (T_xM)^k \to \mathfrak{g}
\quad\text{for each }x\in M.
\]
The space of such forms is commonly denoted $\Omega^k(M;\mathfrak{g})$.

Concretely, choosing a basis $\{e_a\}$ of $\mathfrak{g}$, any $\alpha\in\Omega^k(M;\mathfrak{g})$ can be written uniquely as
\[
\alpha = \sum_a \alpha^a \, e_a,
\]
with ordinary $k$-forms $\alpha^a\in\Omega^k(M)$.

## Examples
1. **Maurer–Cartan form.** On a Lie group $G$, the left Maurer–Cartan form is a $\mathfrak{g}$-valued 1-form on $G$.
2. **Connection form.** A [[fiber-bundles/principal-connection|principal connection]] on a principal bundle is encoded by a $\mathfrak{g}$-valued 1-form on the total space (the connection form).
3. **Curvature.** The [[fiber-bundles/curvature|curvature]] of a principal connection is a $\mathfrak{g}$-valued 2-form on the total space.
