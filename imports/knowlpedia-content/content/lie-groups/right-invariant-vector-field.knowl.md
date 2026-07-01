+++
id = "lie-groups/right-invariant-vector-field"
title = "Right-Invariant Vector Field"
kind = "knowl"
summary = "A vector field on a Lie group that is unchanged by all right translations."
aliases = ["right-invariant-vector-field", "Right-Invariant Vector Field"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/right-invariant-vector-field.md"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]]. A [[fiber-bundles/vector-field|vector field]] \(X\) on \(G\) is **right-invariant** if for every \(g\in G\),
$$
(R_g)_*X = X,
$$
where \(R_g\) is [[lie-groups/right-translation|right translation]].

Equivalently, for all \(g,h\in G\),
$$
X_{hg} = (dR_g)_h(X_h).
$$

## Determined by the value at the identity
As with left-invariance, a right-invariant vector field is determined by \(X_e\in T_eG\), and any \(v\in T_eG\) defines a unique right-invariant vector field
$$
X_g := (dR_g)_e(v).
$$
So right-invariant fields also identify (as a vector space) with \(\mathfrak{g}=T_eG\); see [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra of a Lie group]].

## Bracket sign convention
Under the identification \(v\mapsto X^R\), the commutator of right-invariant vector fields satisfies
$$
[X^R,Y^R] = -([v,w])^R,
$$
so the bracket corresponds to the negative of the usual [[fiber-bundles/lie-bracket|Lie bracket]] on \(\mathfrak{g}\). (Left-invariant fields match the bracket without the minus sign; see [[lie-groups/left-invariant-vector-field|left-invariant vector fields]].)

Right-invariant fields are often convenient when studying conjugation and the [[lie-groups/adjoint-action-of-a-lie-group|adjoint action]].
