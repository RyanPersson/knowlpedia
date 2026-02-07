---
title: "Exponentials and one-parameter subgroups"
description: "The curve t ↦ exp(tX) is the unique one-parameter subgroup with initial velocity X."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} with {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra" >}} $\mathfrak g = T_eG$, and let $\exp:\mathfrak g\to G$ be the {{< knowl id="exponential-map-lie-group" text="exponential map" >}}.

**Lemma (Exponential–one-parameter subgroup).**  
For each $X\in\mathfrak g$, the map
\[
\gamma_X:\mathbb R\to G,\qquad \gamma_X(t)=\exp(tX)
\]
is a smooth group homomorphism $(\mathbb R,+)\to G$, i.e. a {{< knowl id="one-parameter-subgroup" text="one-parameter subgroup" >}}. Moreover,
\[
\gamma_X'(0)=X \in T_eG.
\]
Conversely, if $\gamma:\mathbb R\to G$ is a one-parameter subgroup, then there exists a unique $X\in\mathfrak g$ such that $\gamma(t)=\exp(tX)$ for all $t$; equivalently $X=\gamma'(0)$.

**Context.**  
This lemma packages the correspondence between elements of $\mathfrak g$ and flows of left-invariant vector fields: the curve $\gamma_X$ is the integral curve through $e$ of the left-invariant field determined by $X$ (compare {{< knowl id="one-parameter-subgroups-integral-curves" text="one-parameter subgroups as integral curves" >}}). Locally, it is compatible with the fact that $\exp$ is a {{< knowl id="exponential-local-diffeomorphism" text="local diffeomorphism near 0" >}}.
