---
title: "Maurer–Cartan equation lemma"
description: "A computational identity: the exterior derivative of the Maurer–Cartan form is the negative bracket."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} with Lie algebra $\mathfrak g$, and let $\theta$ be the {{< knowl id="left-maurer-cartan-form" text="left Maurer–Cartan form" >}}.

## Lemma
For any smooth vector fields $X,Y$ on $G$,
$$
(d\theta)(X,Y) = -[\theta(X),\theta(Y)].
$$
Equivalently,
$$
d\theta + \frac12[\theta,\theta]=0,
$$
which is the {{< knowl id="maurer-cartan-equation" text="Maurer–Cartan equation" >}}.

## Context
This lemma is the workhorse behind computations with invariant forms and is the differential-geometric source of the Lie bracket, complementary to the flow-based viewpoint via {{< knowl id="one-parameter-subgroups-integral-curves" text="one-parameter subgroups as integral curves" >}}.
