+++
id = "lie-groups/lie-subalgebra"
title = "Lie subalgebra"
kind = "knowl"
summary = "A linear subspace closed under the Lie bracket."
aliases = ["lie-subalgebra", "Lie subalgebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/lie-subalgebra.md"
+++

Let $\mathfrak g$ be a [[lie-groups/lie-algebra|Lie algebra]] over $\Bbbk$ with bracket $[\ ,\ ]$.

A **Lie subalgebra** of $\mathfrak g$ is a $\Bbbk$-linear subspace $\mathfrak h\subseteq \mathfrak g$ such that
$$
[\mathfrak h,\mathfrak h]\subseteq \mathfrak h,
$$

i.e. $[X,Y]\in \mathfrak h$ for all $X,Y\in \mathfrak h$.

With the restricted bracket, $\mathfrak h$ is itself a Lie algebra, and the inclusion $\mathfrak h\hookrightarrow \mathfrak g$ is a [[lie-groups/lie-algebra-homomorphism|Lie algebra homomorphism]].

## Context and examples
- If $H\subseteq G$ is a [[lie-groups/lie-subgroup|Lie subgroup]] of a Lie group, then $\operatorname{Lie}(H)\subseteq \operatorname{Lie}(G)$ is a Lie subalgebra (see [[lie-groups/lie-algebra-of-subgroup-lemma|the Lie algebra of a subgroup lemma]]).
- An [[lie-groups/ideal-lie-algebra|ideal]] is a Lie subalgebra $\mathfrak h$ satisfying $[\mathfrak g,\mathfrak h]\subseteq \mathfrak h$; ideals are exactly kernels of Lie algebra homomorphisms and allow formation of [[lie-groups/quotient-lie-algebra|quotient Lie algebras]].
