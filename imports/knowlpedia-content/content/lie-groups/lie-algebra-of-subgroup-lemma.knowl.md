+++
id = "lie-groups/lie-algebra-of-subgroup-lemma"
title = "Lie algebra of a subgroup lemma"
kind = "knowl"
summary = "A Lie subgroup has Lie algebra equal to its tangent space at the identity, viewed as a Lie subalgebra."
aliases = ["lie-algebra-of-subgroup-lemma", "Lie algebra of a subgroup lemma"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/lie-algebra-of-subgroup-lemma.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] and let $H\subseteq G$ be a [[lie-groups/lie-subgroup|Lie subgroup]] with inclusion map $\iota:H\hookrightarrow G$.

## Lemma
The differential at the identity
$$
(d\iota)_e : \operatorname{Lie}(H)\to \operatorname{Lie}(G)
$$

is injective, and its image identifies $\operatorname{Lie}(H)$ with the subspace $T_eH\subseteq T_eG$. Under this identification, $\operatorname{Lie}(H)$ is a [[lie-groups/lie-subalgebra|Lie subalgebra]] of $\operatorname{Lie}(G)$.

Equivalently: the Lie algebra of a Lie subgroup is its tangent space at the identity, with the bracket inherited from $\operatorname{Lie}(G)$.

## Context
When $H$ is a *closed* subgroup, [[lie-groups/closed-subgroup-theorem|the closed subgroup theorem]] guarantees that $H$ is an embedded Lie subgroup, so $T_eH$ is literally a subspace of $T_eG$ in the usual embedded-submanifold sense. In that case, this lemma is the key step behind the subgroup–subalgebra bridge used in the [[lie-groups/lie-correspondence|Lie correspondence]].
