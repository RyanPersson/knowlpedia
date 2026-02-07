---
title: "Maurer–Cartan equation"
description: "The structure equation satisfied by the Maurer–Cartan form on a Lie group."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} with Lie algebra $\mathfrak g$.

## Statement
Let $\theta$ denote the {{< knowl id="left-maurer-cartan-form" text="left Maurer–Cartan form" >}} on $G$, i.e. the $\mathfrak g$-valued 1-form characterized by
- $\theta_e=\mathrm{id}_{\mathfrak g}$ under the identification $T_eG\cong \mathfrak g$, and
- left-invariance: $(L_g)^*\theta=\theta$ for all $g\in G$.

Then $\theta$ satisfies the **Maurer–Cartan equation**
$$
d\theta + \frac12[\theta,\theta]=0.
$$

Here $[\theta,\theta]$ denotes the $\mathfrak g$-valued 2-form obtained by combining wedge product with the {{< knowl id="lie-bracket" text="Lie bracket" section="fiber-bundles">}}:
for vector fields $X,Y$ on $G$,
$$
[\theta,\theta](X,Y) = [\theta(X),\theta(Y)].
$$

## Equivalent form (often used in calculations)
For any vector fields $X,Y$ on $G$,
$$
(d\theta)(X,Y) = -[\theta(X),\theta(Y)].
$$
A clean proof is packaged in {{< knowl id="maurer-cartan-equation-lemma" text="the Maurer–Cartan equation lemma" >}}.

## Context
This equation is the differential-geometric encoding of the Lie algebra structure inside the group: it is the reason that brackets of {{< knowl id="left-invariant-vector-field" text="left-invariant vector fields" >}} are controlled by the structure constants of $\mathfrak g$, and it underlies many constructions with {{< knowl id="left-invariant-differential-form" text="left-invariant differential forms" >}} and {{< knowl id="bi-invariant-differential-form" text="bi-invariant forms" >}}.
