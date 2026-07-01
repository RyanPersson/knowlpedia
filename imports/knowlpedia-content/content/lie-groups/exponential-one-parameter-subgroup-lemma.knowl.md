+++
id = "lie-groups/exponential-one-parameter-subgroup-lemma"
title = "Exponentials and one-parameter subgroups"
kind = "knowl"
summary = "The curve t ↦ exp(tX) is the unique one-parameter subgroup with initial velocity X."
aliases = ["exponential-one-parameter-subgroup-lemma", "Exponentials and one-parameter subgroups"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/exponential-one-parameter-subgroup-lemma.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] with [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra]] $\mathfrak g = T_eG$, and let $\exp:\mathfrak g\to G$ be the [[lie-groups/exponential-map-lie-group|exponential map]].

**Lemma (Exponential–one-parameter subgroup).**
For each $X\in\mathfrak g$, the map
\[
\gamma_X:\mathbb R\to G,\qquad \gamma_X(t)=\exp(tX)
\]
is a smooth group homomorphism $(\mathbb R,+)\to G$, i.e. a [[lie-groups/one-parameter-subgroup|one-parameter subgroup]]. Moreover,
\[
\gamma_X'(0)=X \in T_eG.
\]
Conversely, if $\gamma:\mathbb R\to G$ is a one-parameter subgroup, then there exists a unique $X\in\mathfrak g$ such that $\gamma(t)=\exp(tX)$ for all $t$; equivalently $X=\gamma'(0)$.

**Context.**
This lemma packages the correspondence between elements of $\mathfrak g$ and flows of left-invariant vector fields: the curve $\gamma_X$ is the integral curve through $e$ of the left-invariant field determined by $X$ (compare [[lie-groups/one-parameter-subgroups-integral-curves|one-parameter subgroups as integral curves]]). Locally, it is compatible with the fact that $\exp$ is a [[lie-groups/exponential-local-diffeomorphism|local diffeomorphism near 0]].
