---
title: "Representation of a Lie Group"
description: "A smooth homomorphism from a Lie group to the group of invertible linear maps on a vector space."
---

Let \(G\) be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} and \(V\) a finite-dimensional {{< knowl id="vector-space" section="linear-algebra" text="vector space" >}}.
A **(linear) representation of \(G\)** is a {{< knowl id="lie-group-homomorphism" text="Lie group homomorphism" >}}
$$
\rho: G \to \operatorname{GL}(V),
$$
where \(\operatorname{GL}(V)\) is the group of invertible {{< knowl id="linear-operator" section="linear-algebra" text="linear operators" >}} on \(V\).

Equivalently, \(\rho\) is a smooth action of \(G\) on \(V\) by linear isomorphisms, written \(g\cdot v := \rho(g)v\).

## Differentiating a representation
The differential at the identity gives a Lie algebra representation
$$
d\rho_e : \mathfrak{g} \to \mathfrak{gl}(V),
$$
which is a {{< knowl id="representation-of-a-lie-algebra" text="representation of the Lie algebra" >}} \(\mathfrak{g}=T_eG\); see
{{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra of a Lie group" >}} and {{< knowl id="differential-of-a-smooth-map" section="fiber-bundles" text="differential" >}}.

## Examples
- The defining representation \(\operatorname{GL}(n,\mathbb{R})\to \operatorname{GL}(\mathbb{R}^n)\).
- Orthogonal/unitary representations of \(\operatorname{SO}(n)\), \(\operatorname{SU}(n)\) on \(\mathbb{R}^n\), \(\mathbb{C}^n\).
- The {{< knowl id="adjoint-action-of-a-lie-group" text="adjoint representation" >}} \(G\to \operatorname{Aut}(\mathfrak{g})\).

Many structural notions for representations can be studied via the induced Lie algebra representation and tools such as the {{< knowl id="killing-form" text="Killing form" >}} in the semisimple case.
