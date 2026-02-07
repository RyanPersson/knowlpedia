---
title: "Left Translation"
description: "The diffeomorphism of a Lie group given by multiplying on the left by a fixed element."
---

Let \(G\) be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} and fix \(g\in G\). The **left translation** by \(g\) is the map
$$
L_g:G\to G,\qquad L_g(h)=gh.
$$

## Smoothness and inverse
Because group multiplication is {{< knowl id="smooth-map" section="fiber-bundles" text="smooth" >}}, \(L_g\) is a diffeomorphism with inverse \(L_{g^{-1}}\).

## Differential
For each \(h\in G\), the differential
$$
(dL_g)_h : T_hG \to T_{gh}G
$$
is a linear isomorphism of {{< knowl id="tangent-space" section="differential-geometry" text="tangent spaces" >}}; see {{< knowl id="differential-of-a-smooth-map" section="fiber-bundles" text="differential" >}}.

## Why it matters
Left translations let you “move” tangent vectors around the group and are used to define
{{< knowl id="left-invariant-vector-field" text="left-invariant vector fields" >}} and the canonical identification
\(\mathfrak{g}=T_eG\) with left-invariant vector fields (see {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra of a Lie group" >}}).
