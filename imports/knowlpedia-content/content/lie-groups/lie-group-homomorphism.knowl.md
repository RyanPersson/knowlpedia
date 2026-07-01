+++
id = "lie-groups/lie-group-homomorphism"
title = "Lie Group Homomorphism"
kind = "knowl"
summary = "A smooth map between Lie groups that is also a group homomorphism."
aliases = ["lie-group-homomorphism", "Lie Group Homomorphism"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/lie-group-homomorphism.md"
+++

A **Lie group homomorphism** is a map \(\varphi:G\to H\) between [[fiber-bundles/lie-group|Lie groups]] such that:
- \(\varphi(gh)=\varphi(g)\varphi(h)\) for all \(g,h\in G\), and
- \(\varphi\) is a [[fiber-bundles/smooth-map|smooth map]].

Equivalently, \(\varphi\) is a group homomorphism that is smooth as a map of manifolds.

## Differential at the identity
The [[fiber-bundles/differential-of-a-smooth-map|differential]] at the identity,
$$
(d\varphi)_e:T_eG\to T_eH,
$$
is a [[lie-groups/lie-algebra-homomorphism|Lie algebra homomorphism]]
\((d\varphi)_e:\mathfrak{g}\to\mathfrak{h}\), where \(\mathfrak{g}=T_eG\) and \(\mathfrak{h}=T_eH\); see [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra of a Lie group]].

## Kernels, images, and coverings
- \(\ker(\varphi)\) is a closed subgroup of \(G\), hence an embedded [[lie-groups/lie-subgroup|Lie subgroup]] (by [[lie-groups/closed-subgroup-theorem|closed subgroup theorem]]).
- The image \(\varphi(G)\) is an immersed Lie subgroup of \(H\).
- When \(\ker(\varphi)\) is discrete and \(\varphi\) is a local diffeomorphism, \(\varphi\) is a [[lie-groups/covering-lie-group|covering Lie group]] map.

Lie group homomorphisms are the morphisms in the category underlying the [[lie-groups/lie-correspondence|Lie correspondence]].
