+++
id = "lie-groups/maurer-cartan-equation-lemma"
title = "Maurer–Cartan equation lemma"
kind = "knowl"
summary = "A computational identity: the exterior derivative of the Maurer–Cartan form is the negative bracket."
aliases = ["maurer-cartan-equation-lemma", "Maurer–Cartan equation lemma"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/maurer-cartan-equation-lemma.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] with Lie algebra $\mathfrak g$, and let $\theta$ be the [[lie-groups/left-maurer-cartan-form|left Maurer–Cartan form]].

## Lemma
For any smooth vector fields $X,Y$ on $G$,
$$
(d\theta)(X,Y) = -[\theta(X),\theta(Y)].
$$
Equivalently,
$$
d\theta + \frac12[\theta,\theta]=0,
$$
which is the [[lie-groups/maurer-cartan-equation|Maurer–Cartan equation]].

## Context
This lemma is the workhorse behind computations with invariant forms and is the differential-geometric source of the Lie bracket, complementary to the flow-based viewpoint via [[lie-groups/one-parameter-subgroups-integral-curves|one-parameter subgroups as integral curves]].
