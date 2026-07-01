+++
id = "lie-groups/right-translation"
title = "Right Translation"
kind = "knowl"
summary = "The diffeomorphism of a Lie group given by multiplying on the right by a fixed element."
aliases = ["right-translation", "Right Translation"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/right-translation.md"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] and fix \(g\in G\). The **right translation** by \(g\) is the map
$$
R_g:G\to G,\qquad R_g(h)=hg.
$$

## Smoothness and inverse
Since multiplication is [[fiber-bundles/smooth-map|smooth]], \(R_g\) is a diffeomorphism with inverse \(R_{g^{-1}}\).

## Differential
For each \(h\in G\), the differential
$$
(dR_g)_h : T_hG \to T_{hg}G
$$
is a linear isomorphism between [[differential-geometry/tangent-space|tangent spaces]].

## Relation to conjugation
Conjugation by \(g\) can be written as a composition of translations:
$$
c_g = L_g \circ R_{g^{-1}},
$$
which underlies the [[lie-groups/adjoint-action-of-a-lie-group|adjoint action]].

Right translations are used to define [[lie-groups/right-invariant-vector-field|right-invariant vector fields]].
