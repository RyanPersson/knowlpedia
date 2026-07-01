+++
id = "lie-groups/lie-algebra-of-a-lie-group"
title = "Lie Algebra of a Lie Group"
kind = "knowl"
summary = "The tangent space at the identity of a Lie group, equipped with a canonical bracket from invariant vector fields."
aliases = ["lie-algebra-of-a-lie-group", "Lie Algebra of a Lie Group"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/lie-algebra-of-a-lie-group.md"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] with identity element \(e\).
The **Lie algebra of \(G\)** is the [[differential-geometry/tangent-space|tangent space]]
$$
\mathfrak{g} := T_eG.
$$

## How the bracket is defined
Using [[lie-groups/left-translation|left translations]] \(L_g(h)=gh\), any \(X\in T_eG\) determines a unique [[lie-groups/left-invariant-vector-field|left-invariant vector field]] \(\widetilde X\) by
$$
\widetilde X_g := (dL_g)_e(X)\in T_gG.
$$
Then the Lie bracket on \(\mathfrak{g}\) is defined by
$$
[X,Y] := \big[\widetilde X,\widetilde Y\big]_e,
$$
where \([\widetilde X,\widetilde Y]\) is the commutator of [[fiber-bundles/vector-field|vector fields]].

## Key properties
- This makes \(\mathfrak{g}\) a [[lie-groups/lie-algebra|Lie algebra]].
- If \(\varphi:G\to H\) is a [[lie-groups/lie-group-homomorphism|Lie group homomorphism]], then \((d\varphi)_e:\mathfrak{g}\to\mathfrak{h}\) is a [[lie-groups/lie-algebra-homomorphism|Lie algebra homomorphism]].

## Exponential and one-parameter subgroups
The [[lie-groups/exponential-map-lie-group|exponential map]] \(\exp:\mathfrak{g}\to G\) satisfies that
\(t\mapsto \exp(tX)\) is a [[lie-groups/one-parameter-subgroup|one-parameter subgroup]] for each \(X\in\mathfrak{g}\), forming a central part of the [[lie-groups/lie-correspondence|Lie correspondence]].
