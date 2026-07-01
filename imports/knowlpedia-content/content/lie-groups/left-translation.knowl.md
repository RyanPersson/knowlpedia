+++
id = "lie-groups/left-translation"
title = "Left Translation"
kind = "knowl"
summary = "The diffeomorphism of a Lie group given by multiplying on the left by a fixed element."
aliases = ["left-translation", "Left Translation"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/left-translation.md"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] and fix \(g\in G\). The **left translation** by \(g\) is the map
$$
L_g:G\to G,\qquad L_g(h)=gh.
$$

## Smoothness and inverse
Because group multiplication is [[fiber-bundles/smooth-map|smooth]], \(L_g\) is a diffeomorphism with inverse \(L_{g^{-1}}\).

## Differential
For each \(h\in G\), the differential
$$
(dL_g)_h : T_hG \to T_{gh}G
$$
is a linear isomorphism of [[differential-geometry/tangent-space|tangent spaces]]; see [[fiber-bundles/differential-of-a-smooth-map|differential]].

## Why it matters
Left translations let you “move” tangent vectors around the group and are used to define
[[lie-groups/left-invariant-vector-field|left-invariant vector fields]] and the canonical identification
\(\mathfrak{g}=T_eG\) with left-invariant vector fields (see [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra of a Lie group]]).
