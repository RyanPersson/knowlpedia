---
title: "Right-Invariant Vector Field"
description: "A vector field on a Lie group that is unchanged by all right translations."
---

Let \(G\) be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}}. A {{< knowl id="vector-field" section="fiber-bundles" text="vector field" >}} \(X\) on \(G\) is **right-invariant** if for every \(g\in G\),
$$
(R_g)_*X = X,
$$
where \(R_g\) is {{< knowl id="right-translation" text="right translation" >}}.

Equivalently, for all \(g,h\in G\),
$$
X_{hg} = (dR_g)_h(X_h).
$$

## Determined by the value at the identity
As with left-invariance, a right-invariant vector field is determined by \(X_e\in T_eG\), and any \(v\in T_eG\) defines a unique right-invariant vector field
$$
X_g := (dR_g)_e(v).
$$
So right-invariant fields also identify (as a vector space) with \(\mathfrak{g}=T_eG\); see {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra of a Lie group" >}}.

## Bracket sign convention
Under the identification \(v\mapsto X^R\), the commutator of right-invariant vector fields satisfies
$$
[X^R,Y^R] = -([v,w])^R,
$$
so the bracket corresponds to the negative of the usual {{< knowl id="lie-bracket" text="Lie bracket" section="fiber-bundles">}} on \(\mathfrak{g}\). (Left-invariant fields match the bracket without the minus sign; see {{< knowl id="left-invariant-vector-field" text="left-invariant vector fields" >}}.)

Right-invariant fields are often convenient when studying conjugation and the {{< knowl id="adjoint-action-of-a-lie-group" text="adjoint action" >}}.
