---
title: "Closed subgroup of a Lie group"
description: "A subgroup that is closed in the topology of the ambient Lie group."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} and let $H\le G$ be a subgroup.

**Definition.** $H$ is a **closed subgroup** if it is closed as a subset of the underlying manifold (equivalently, as a subset of the underlying Hausdorff topological space) of $G$.

**Why this matters.** Closedness is the exact hypothesis needed to ensure that $H$ inherits a canonical Lie group structure from $G$: by the {{< knowl id="closed-subgroup-theorem" text="closed subgroup theorem" >}}, a closed subgroup is an embedded {{< knowl id="lie-subgroup" text="Lie subgroup" >}}. This is essential for forming smooth quotients such as the {{< knowl id="coset-space" text="coset space" >}} $G/H$, which becomes a manifold under the same hypothesis.

**Remark.** The assumption cannot be dropped in general: non-closed subgroups can be dense and fail to be submanifolds, so there need not be a reasonable smooth structure making inclusion a smooth embedding.
