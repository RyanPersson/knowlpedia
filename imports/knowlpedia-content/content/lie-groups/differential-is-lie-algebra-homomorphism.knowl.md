+++
id = "lie-groups/differential-is-lie-algebra-homomorphism"
title = "Differential of a Lie group homomorphism"
kind = "knowl"
summary = "If is a Lie group homomorphism, then is a Lie algebra homomorphism."
aliases = ["differential-is-lie-algebra-homomorphism", "Differential of a Lie group homomorphism"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/differential-is-lie-algebra-homomorphism.md"
+++

Let $\Phi:G\to H$ be a [[lie-groups/lie-group-homomorphism|Lie group homomorphism]] between [[fiber-bundles/lie-group|Lie groups]], and let $\mathfrak g=\mathrm{Lie}(G)$ and $\mathfrak h=\mathrm{Lie}(H)$ (see [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra of a Lie group]]).

## Theorem
The differential at the identity,
\[
d\Phi_e:\mathfrak g \longrightarrow \mathfrak h,
\]
is a [[lie-groups/lie-algebra-homomorphism|Lie algebra homomorphism]]; i.e.
\[
d\Phi_e([X,Y]) = [\,d\Phi_e(X),\, d\Phi_e(Y)\,]
\qquad\text{for all }X,Y\in\mathfrak g.
\]

Moreover, $\Phi$ intertwines exponential maps:
\[
\Phi(\exp_G X) \;=\; \exp_H\!\bigl(d\Phi_e(X)\bigr)
\quad\text{for all }X\in\mathfrak g,
\]
where $\exp_G$ and $\exp_H$ are the [[lie-groups/exponential-map-lie-group|exponential maps]] of $G$ and $H$.

## Idea of proof
Identify $\mathfrak g$ and $\mathfrak h$ with [[lie-groups/left-invariant-vector-field|left-invariant vector fields]] using [[lie-groups/left-invariant-fields-lie-algebra-lemma|the left-invariant fields Lie algebra lemma]]. The pushforward $\Phi_*$ carries left-invariant vector fields on $G$ to left-invariant vector fields on $H$, and pushforwards preserve Lie brackets of vector fields. Evaluating at $e$ yields bracket preservation for $d\Phi_e$.

**Context.** This is the functorial bridge from global group maps to infinitesimal algebra maps; it is the starting point for studying [[lie-groups/representation-of-a-lie-group|representations of Lie groups]] via their differentiated [[lie-groups/representation-of-a-lie-algebra|Lie algebra representations]].
