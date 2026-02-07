---
title: "Lie Algebra of a Lie Group"
description: "The tangent space at the identity of a Lie group, equipped with a canonical bracket from invariant vector fields."
---

Let \(G\) be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} with identity element \(e\).
The **Lie algebra of \(G\)** is the {{< knowl id="tangent-space" section="differential-geometry" text="tangent space" >}}
$$
\mathfrak{g} := T_eG.
$$

## How the bracket is defined
Using {{< knowl id="left-translation" text="left translations" >}} \(L_g(h)=gh\), any \(X\in T_eG\) determines a unique {{< knowl id="left-invariant-vector-field" text="left-invariant vector field" >}} \(\widetilde X\) by
$$
\widetilde X_g := (dL_g)_e(X)\in T_gG.
$$
Then the Lie bracket on \(\mathfrak{g}\) is defined by
$$
[X,Y] := \big[\widetilde X,\widetilde Y\big]_e,
$$
where \([\widetilde X,\widetilde Y]\) is the commutator of {{< knowl id="vector-field" section="fiber-bundles" text="vector fields" >}}.

## Key properties
- This makes \(\mathfrak{g}\) a {{< knowl id="lie-algebra" text="Lie algebra" >}}.
- If \(\varphi:G\to H\) is a {{< knowl id="lie-group-homomorphism" text="Lie group homomorphism" >}}, then \((d\varphi)_e:\mathfrak{g}\to\mathfrak{h}\) is a {{< knowl id="lie-algebra-homomorphism" text="Lie algebra homomorphism" >}}.

## Exponential and one-parameter subgroups
The {{< knowl id="exponential-map-lie-group" text="exponential map" >}} \(\exp:\mathfrak{g}\to G\) satisfies that
\(t\mapsto \exp(tX)\) is a {{< knowl id="one-parameter-subgroup" text="one-parameter subgroup" >}} for each \(X\in\mathfrak{g}\), forming a central part of the {{< knowl id="lie-correspondence" text="Lie correspondence" >}}.
