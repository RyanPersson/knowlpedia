+++
id = "lie-groups/left-invariant-vector-field"
title = "Left-Invariant Vector Field"
kind = "knowl"
summary = "A vector field on a Lie group that is unchanged by all left translations."
aliases = ["left-invariant-vector-field", "Left-Invariant Vector Field"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/left-invariant-vector-field.md"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]]. A [[fiber-bundles/vector-field|vector field]] \(X\) on \(G\) is **left-invariant** if for every \(g\in G\),
$$
(L_g)_*X = X,
$$
where \(L_g\) is [[lie-groups/left-translation|left translation]] and \((L_g)_*\) denotes the pushforward on vector fields.

Equivalently, for all \(g,h\in G\),
$$
X_{gh} = (dL_g)_h(X_h).
$$

## Determined by the value at the identity
A left-invariant vector field is completely determined by its value \(X_e\in T_eG\).
Conversely, every \(v\in T_eG\) defines a unique left-invariant vector field by
$$
X_g := (dL_g)_e(v).
$$
Thus the space of left-invariant vector fields is naturally identified with the [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra]] \(\mathfrak{g}=T_eG\).

## Lie bracket compatibility
If \(\widetilde X,\widetilde Y\) are left-invariant, then so is \([\widetilde X,\widetilde Y]\), and
$$
[\widetilde X,\widetilde Y]_e = [X_e,Y_e]
$$
defines the [[fiber-bundles/lie-bracket|Lie bracket]] on \(\mathfrak{g}\).

Flows of left-invariant vector fields yield [[lie-groups/one-parameter-subgroup|one-parameter subgroups]] and are closely related to the [[lie-groups/exponential-map-lie-group|exponential map]].
