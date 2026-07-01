+++
id = "lie-groups/maurer-cartan-equation"
title = "Maurer–Cartan equation"
kind = "knowl"
summary = "The structure equation satisfied by the Maurer–Cartan form on a Lie group."
aliases = ["maurer-cartan-equation", "Maurer–Cartan equation"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/maurer-cartan-equation.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] with Lie algebra $\mathfrak g$.

## Statement
Let $\theta$ denote the [[lie-groups/left-maurer-cartan-form|left Maurer–Cartan form]] on $G$, i.e. the $\mathfrak g$-valued 1-form characterized by
- $\theta_e=\mathrm{id}_{\mathfrak g}$ under the identification $T_eG\cong \mathfrak g$, and
- left-invariance: $(L_g)^*\theta=\theta$ for all $g\in G$.

Then $\theta$ satisfies the **Maurer–Cartan equation**
$$
d\theta + \frac12[\theta,\theta]=0.
$$

Here $[\theta,\theta]$ denotes the $\mathfrak g$-valued 2-form obtained by combining wedge product with the [[fiber-bundles/lie-bracket|Lie bracket]]:
for vector fields $X,Y$ on $G$,
$$
[\theta,\theta](X,Y) = [\theta(X),\theta(Y)].
$$

## Equivalent form (often used in calculations)
For any vector fields $X,Y$ on $G$,
$$
(d\theta)(X,Y) = -[\theta(X),\theta(Y)].
$$
A clean proof is packaged in [[lie-groups/maurer-cartan-equation-lemma|the Maurer–Cartan equation lemma]].

## Context
This equation is the differential-geometric encoding of the Lie algebra structure inside the group: it is the reason that brackets of [[lie-groups/left-invariant-vector-field|left-invariant vector fields]] are controlled by the structure constants of $\mathfrak g$, and it underlies many constructions with [[lie-groups/left-invariant-differential-form|left-invariant differential forms]] and [[lie-groups/bi-invariant-differential-form|bi-invariant forms]].
