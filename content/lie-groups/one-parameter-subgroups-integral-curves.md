---
title: "One-parameter subgroups as integral curves"
description: "Exponentials give flows of invariant vector fields; invariant flows recover one-parameter subgroups."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} with Lie algebra $\mathfrak g$.

## Statement
Fix $X\in\mathfrak g$, and let $X^L$ be the corresponding {{< knowl id="left-invariant-vector-field" text="left-invariant vector field" >}} on $G$ (obtained by translating $X\in T_eG$ via {{< knowl id="left-translation" text="left translations" >}}).

1. The integral curve of $X^L$ starting at the identity is the one-parameter subgroup
   $$
   t\longmapsto \exp(tX),
   $$

   where $\exp$ is the {{< knowl id="exponential-map-lie-group" text="exponential map" >}}. In particular, $\exp(tX)$ solves the ODE $g'(t)=(X^L)_{g(t)}$ with $g(0)=e$.

2. More generally, the integral curve of $X^L$ starting at $g_0\in G$ is
   $$
   t\longmapsto g_0\,\exp(tX).
   $$

There is an analogous statement for the {{< knowl id="right-invariant-vector-field" text="right-invariant vector field" >}} $X^R$, whose integral curves are $t\mapsto \exp(tX)\,g_0$.

## Context
This viewpoint explains why the bracket on $\mathfrak g$ can be recovered from commutators of flows: the Lie bracket is the infinitesimal failure of invariant flows to commute (compare {{< knowl id="left-invariant-fields-lie-algebra-lemma" text="the bracket lemma for left-invariant fields" >}} and the structure encoded by the {{< knowl id="maurer-cartan-equation" text="Maurer–Cartan equation" >}}).
