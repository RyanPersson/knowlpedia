+++
id = "lie-groups/closed-subgroup-lie-group"
title = "Closed subgroup of a Lie group"
kind = "knowl"
summary = "A subgroup that is closed in the topology of the ambient Lie group."
aliases = ["closed-subgroup-lie-group", "Closed subgroup of a Lie group"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/closed-subgroup-lie-group.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] and let $H\le G$ be a subgroup.

**Definition.** $H$ is a **closed subgroup** if it is closed as a subset of the underlying manifold (equivalently, as a subset of the underlying Hausdorff topological space) of $G$.

**Why this matters.** Closedness is the exact hypothesis needed to ensure that $H$ inherits a canonical Lie group structure from $G$: by the [[lie-groups/closed-subgroup-theorem|closed subgroup theorem]], a closed subgroup is an embedded [[lie-groups/lie-subgroup|Lie subgroup]]. This is essential for forming smooth quotients such as the [[lie-groups/coset-space|coset space]] $G/H$, which becomes a manifold under the same hypothesis.

**Remark.** The assumption cannot be dropped in general: non-closed subgroups can be dense and fail to be submanifolds, so there need not be a reasonable smooth structure making inclusion a smooth embedding.
