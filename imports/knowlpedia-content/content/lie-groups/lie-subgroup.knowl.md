+++
id = "lie-groups/lie-subgroup"
title = "Lie Subgroup"
kind = "knowl"
summary = "A subgroup of a Lie group that carries a compatible immersed submanifold structure."
aliases = ["lie-subgroup", "Lie Subgroup"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/lie-subgroup.md"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]]. A **Lie subgroup** of \(G\) is a subgroup \(H\le G\) together with the structure of an immersed [[fiber-bundles/smooth-manifold|submanifold]] such that the inclusion map
$$
i:H\hookrightarrow G
$$
is a smooth immersion and a group homomorphism (so the group operations on \(H\) are smooth).

A Lie subgroup is called **embedded** if \(i\) is an embedding (so \(H\) is an actual submanifold of \(G\)).

## Closed subgroups
A crucial fact is the [[lie-groups/closed-subgroup-theorem|closed subgroup theorem]]: if \(H\) is a closed subgroup of \(G\) (as a subset), then \(H\) is an embedded Lie subgroup.

## Relationship to Lie algebras
The Lie algebra \(\mathfrak{h}=T_eH\) identifies with a [[lie-groups/lie-subalgebra|Lie subalgebra]] of \(\mathfrak{g}=T_eG\); see [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra of a Lie group]].

## Quotients
If \(H\) is closed, the quotient \(G/H\) carries a natural smooth structure and is the underlying manifold of the [[lie-groups/quotient-lie-group|quotient construction]] when \(H\) is normal.

## Examples
- \(\operatorname{SO}(n)\le \operatorname{GL}(n,\mathbb{R})\).
- The diagonal matrices form a Lie subgroup of \(\operatorname{GL}(n,\mathbb{R})\).
