+++
id = "lie-groups/adjoint-action-of-a-lie-group"
title = "Adjoint Action of a Lie Group"
kind = "knowl"
summary = "The conjugation action of a Lie group on itself and the induced linear action on its Lie algebra."
aliases = ["adjoint-action-of-a-lie-group", "Adjoint Action of a Lie Group"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/adjoint-action-of-a-lie-group.md"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]]. The **conjugation map** by \(g\in G\) is
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
called the **adjoint action** of \(G\) on its Lie algebra. The assignment \(g\mapsto \operatorname{Ad}_g\) is a [[lie-groups/lie-group-homomorphism|Lie group homomorphism]]
$$
\operatorname{Ad}:G\to \operatorname{Aut}(\mathfrak{g}),
$$
where \(\operatorname{Aut}(\mathfrak{g})\) denotes [[lie-groups/lie-algebra-automorphism|Lie algebra automorphisms]].

## Kernel and center
The kernel of \(\operatorname{Ad}\) is the [[lie-groups/center-of-a-lie-group|center of the group]] \(Z(G)\): elements commuting with all of \(G\).

## Matrix group picture and exponentials
For a matrix Lie group \(G\subseteq \operatorname{GL}(n)\),
$$
\operatorname{Ad}_g(X)=gXg^{-1}.
$$
Moreover, with the [[lie-groups/exponential-map-lie-group|exponential map]] one has the fundamental relation
$$
\operatorname{Ad}_{\exp(X)} = \exp(\operatorname{ad}_X),
$$
linking \(\operatorname{Ad}\) to the [[lie-groups/adjoint-representation-of-a-lie-algebra|adjoint representation of the Lie algebra]] and ultimately to the [[lie-groups/baker-campbell-hausdorff-formula|Baker–Campbell–Hausdorff formula]].

Adjoint actions play a central role in structure theory (e.g. [[lie-groups/cartan-subalgebra|Cartan subalgebras]], [[lie-groups/root-system|root systems]], and the [[lie-groups/weyl-group|Weyl group]]).
