---
title: "Adjoint Action of a Lie Group"
description: "The conjugation action of a Lie group on itself and the induced linear action on its Lie algebra."
---

Let \(G\) be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}}. The **conjugation map** by \(g\in G\) is
$$
c_g:G\to G,\qquad c_g(h)=ghg^{-1}.
$$
This defines a smooth action of \(G\) on itself by group automorphisms.

## Induced action on the Lie algebra
Differentiating at the identity gives a linear map
$$
\operatorname{Ad}_g := (dc_g)_e : \mathfrak{g} \to \mathfrak{g},
\qquad \mathfrak{g}=T_eG,
$$
called the **adjoint action** of \(G\) on its Lie algebra. The assignment \(g\mapsto \operatorname{Ad}_g\) is a {{< knowl id="lie-group-homomorphism" text="Lie group homomorphism" >}}
$$
\operatorname{Ad}:G\to \operatorname{Aut}(\mathfrak{g}),
$$
where \(\operatorname{Aut}(\mathfrak{g})\) denotes {{< knowl id="lie-algebra-automorphism" text="Lie algebra automorphisms" >}}.

## Kernel and center
The kernel of \(\operatorname{Ad}\) is the {{< knowl id="center-of-a-lie-group" text="center of the group" >}} \(Z(G)\): elements commuting with all of \(G\).

## Matrix group picture and exponentials
For a matrix Lie group \(G\subseteq \operatorname{GL}(n)\),
$$
\operatorname{Ad}_g(X)=gXg^{-1}.
$$
Moreover, with the {{< knowl id="exponential-map-lie-group" text="exponential map" >}} one has the fundamental relation
$$
\operatorname{Ad}_{\exp(X)} = \exp(\operatorname{ad}_X),
$$
linking \(\operatorname{Ad}\) to the {{< knowl id="adjoint-representation-of-a-lie-algebra" text="adjoint representation of the Lie algebra" >}} and ultimately to the {{< knowl id="baker-campbell-hausdorff-formula" text="Baker–Campbell–Hausdorff formula" >}}.

Adjoint actions play a central role in structure theory (e.g. {{< knowl id="cartan-subalgebra" text="Cartan subalgebras" >}}, {{< knowl id="root-system" text="root systems" >}}, and the {{< knowl id="weyl-group" text="Weyl group" >}}).
