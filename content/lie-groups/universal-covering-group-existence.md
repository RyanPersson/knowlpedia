---
title: "Existence of universal covering groups"
description: "Every connected Lie group admits a unique (up to isomorphism) simply connected covering group compatible with multiplication."
---

### Theorem (existence and uniqueness)
Let $G$ be a connected {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}}. Then there exists a Lie group $\widetilde G$ and a smooth map $p:\widetilde G\to G$ such that:

1. $p$ is a covering map of manifolds and a {{< knowl id="lie-group-homomorphism" text="Lie group homomorphism" >}}.
2. $\widetilde G$ is {{< knowl id="simply-connected-lie-group" text="simply connected" >}}.
3. The pair $(\widetilde G,p)$ is unique up to unique Lie group isomorphism over $G$ (i.e. it is the {{< knowl id="universal-covering-group" text="universal covering group" >}} of $G$).

Moreover, the induced map on Lie algebras
$$
dp_e:\mathrm{Lie}(\widetilde G)\to \mathrm{Lie}(G)
$$
is an isomorphism (by {{< knowl id="differential-is-lie-algebra-homomorphism" text="functoriality of the differential" >}}).

### Construction idea (context)
One standard construction starts with the universal cover $\widetilde{G}_{\mathrm{top}}$ of the underlying manifold of $G$. The Lie group operations on $G$ lift uniquely to $\widetilde{G}_{\mathrm{top}}$ once a basepoint over $e\in G$ is fixed, producing a Lie group structure on the universal cover so that the covering projection becomes a homomorphism. This gives a canonical way to pass from a connected Lie group to a simply connected one with the same {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra" >}}, which underlies many “Lie algebra determines the simply connected group” results (compare {{< knowl id="simply-connected-determined-by-algebra" text="simply connected groups are determined by their Lie algebras" >}}).
