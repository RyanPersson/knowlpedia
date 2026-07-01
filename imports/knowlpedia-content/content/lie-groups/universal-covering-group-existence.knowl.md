+++
id = "lie-groups/universal-covering-group-existence"
title = "Existence of universal covering groups"
kind = "knowl"
summary = "Every connected Lie group admits a unique (up to isomorphism) simply connected covering group compatible with multiplication."
aliases = ["universal-covering-group-existence", "Existence of universal covering groups"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/universal-covering-group-existence.md"
+++

### Theorem (existence and uniqueness)
Let $G$ be a connected [[fiber-bundles/lie-group|Lie group]]. Then there exists a Lie group $\widetilde G$ and a smooth map $p:\widetilde G\to G$ such that:

1. $p$ is a covering map of manifolds and a [[lie-groups/lie-group-homomorphism|Lie group homomorphism]].
2. $\widetilde G$ is [[lie-groups/simply-connected-lie-group|simply connected]].
3. The pair $(\widetilde G,p)$ is unique up to unique Lie group isomorphism over $G$ (i.e. it is the [[lie-groups/universal-covering-group|universal covering group]] of $G$).

Moreover, the induced map on Lie algebras
$$
dp_e:\mathrm{Lie}(\widetilde G)\to \mathrm{Lie}(G)
$$
is an isomorphism (by [[lie-groups/differential-is-lie-algebra-homomorphism|functoriality of the differential]]).

### Construction idea (context)
One standard construction starts with the universal cover $\widetilde{G}_{\mathrm{top}}$ of the underlying manifold of $G$. The Lie group operations on $G$ lift uniquely to $\widetilde{G}_{\mathrm{top}}$ once a basepoint over $e\in G$ is fixed, producing a Lie group structure on the universal cover so that the covering projection becomes a homomorphism. This gives a canonical way to pass from a connected Lie group to a simply connected one with the same [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra]], which underlies many “Lie algebra determines the simply connected group” results (compare [[lie-groups/simply-connected-determined-by-algebra|simply connected groups are determined by their Lie algebras]]).
