---
title: "Left-Invariant Vector Field"
description: "A vector field on a Lie group that is unchanged by all left translations."
---

Let \(G\) be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}}. A {{< knowl id="vector-field" section="fiber-bundles" text="vector field" >}} \(X\) on \(G\) is **left-invariant** if for every \(g\in G\),
$$
(L_g)_*X = X,
$$
where \(L_g\) is {{< knowl id="left-translation" text="left translation" >}} and \((L_g)_*\) denotes the pushforward on vector fields.

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
Thus the space of left-invariant vector fields is naturally identified with the {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra" >}} \(\mathfrak{g}=T_eG\).

## Lie bracket compatibility
If \(\widetilde X,\widetilde Y\) are left-invariant, then so is \([\widetilde X,\widetilde Y]\), and
$$
[\widetilde X,\widetilde Y]_e = [X_e,Y_e]
$$
defines the {{< knowl id="lie-bracket" text="Lie bracket" section="fiber-bundles">}} on \(\mathfrak{g}\).

Flows of left-invariant vector fields yield {{< knowl id="one-parameter-subgroup" text="one-parameter subgroups" >}} and are closely related to the {{< knowl id="exponential-map-lie-group" text="exponential map" >}}.
