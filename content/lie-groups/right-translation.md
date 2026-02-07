---
title: "Right Translation"
description: "The diffeomorphism of a Lie group given by multiplying on the right by a fixed element."
---

Let \(G\) be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} and fix \(g\in G\). The **right translation** by \(g\) is the map
$$
R_g:G\to G,\qquad R_g(h)=hg.
$$

## Smoothness and inverse
Since multiplication is {{< knowl id="smooth-map" section="fiber-bundles" text="smooth" >}}, \(R_g\) is a diffeomorphism with inverse \(R_{g^{-1}}\).

## Differential
For each \(h\in G\), the differential
$$
(dR_g)_h : T_hG \to T_{hg}G
$$
is a linear isomorphism between {{< knowl id="tangent-space" section="differential-geometry" text="tangent spaces" >}}.

## Relation to conjugation
Conjugation by \(g\) can be written as a composition of translations:
$$
c_g = L_g \circ R_{g^{-1}},
$$
which underlies the {{< knowl id="adjoint-action-of-a-lie-group" text="adjoint action" >}}.

Right translations are used to define {{< knowl id="right-invariant-vector-field" text="right-invariant vector fields" >}}.
