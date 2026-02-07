---
title: "Differential of a Lie group homomorphism"
description: "If is a Lie group homomorphism, then is a Lie algebra homomorphism."
---

Let $\Phi:G\to H$ be a {{< knowl id="lie-group-homomorphism" text="Lie group homomorphism" >}} between {{< knowl id="lie-group" text="Lie groups" section="fiber-bundles">}}, and let $\mathfrak g=\mathrm{Lie}(G)$ and $\mathfrak h=\mathrm{Lie}(H)$ (see {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra of a Lie group" >}}).

## Theorem
The differential at the identity,
\[
d\Phi_e:\mathfrak g \longrightarrow \mathfrak h,
\]
is a {{< knowl id="lie-algebra-homomorphism" text="Lie algebra homomorphism" >}}; i.e.
\[
d\Phi_e([X,Y]) = [\,d\Phi_e(X),\, d\Phi_e(Y)\,]
\qquad\text{for all }X,Y\in\mathfrak g.
\]

Moreover, $\Phi$ intertwines exponential maps:
\[
\Phi(\exp_G X) \;=\; \exp_H\!\bigl(d\Phi_e(X)\bigr)
\quad\text{for all }X\in\mathfrak g,
\]
where $\exp_G$ and $\exp_H$ are the {{< knowl id="exponential-map-lie-group" text="exponential maps" >}} of $G$ and $H$.

## Idea of proof
Identify $\mathfrak g$ and $\mathfrak h$ with {{< knowl id="left-invariant-vector-field" text="left-invariant vector fields" >}} using {{< knowl id="left-invariant-fields-lie-algebra-lemma" text="the left-invariant fields Lie algebra lemma" >}}. The pushforward $\Phi_*$ carries left-invariant vector fields on $G$ to left-invariant vector fields on $H$, and pushforwards preserve Lie brackets of vector fields. Evaluating at $e$ yields bracket preservation for $d\Phi_e$.

**Context.** This is the functorial bridge from global group maps to infinitesimal algebra maps; it is the starting point for studying {{< knowl id="representation-of-a-lie-group" text="representations of Lie groups" >}} via their differentiated {{< knowl id="representation-of-a-lie-algebra" text="Lie algebra representations" >}}.
