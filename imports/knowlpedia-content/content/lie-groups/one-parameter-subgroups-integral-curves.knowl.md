+++
id = "lie-groups/one-parameter-subgroups-integral-curves"
title = "One-parameter subgroups as integral curves"
kind = "knowl"
summary = "Exponentials give flows of invariant vector fields; invariant flows recover one-parameter subgroups."
aliases = ["one-parameter-subgroups-integral-curves", "One-parameter subgroups as integral curves"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/one-parameter-subgroups-integral-curves.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] with Lie algebra $\mathfrak g$.

## Statement
Fix $X\in\mathfrak g$, and let $X^L$ be the corresponding [[lie-groups/left-invariant-vector-field|left-invariant vector field]] on $G$ (obtained by translating $X\in T_eG$ via [[lie-groups/left-translation|left translations]]).

1. The integral curve of $X^L$ starting at the identity is the one-parameter subgroup
   $$
   t\longmapsto \exp(tX),
   $$

   where $\exp$ is the [[lie-groups/exponential-map-lie-group|exponential map]]. In particular, $\exp(tX)$ solves the ODE $g'(t)=(X^L)_{g(t)}$ with $g(0)=e$.

2. More generally, the integral curve of $X^L$ starting at $g_0\in G$ is
   $$
   t\longmapsto g_0\,\exp(tX).
   $$

There is an analogous statement for the [[lie-groups/right-invariant-vector-field|right-invariant vector field]] $X^R$, whose integral curves are $t\mapsto \exp(tX)\,g_0$.

## Context
This viewpoint explains why the bracket on $\mathfrak g$ can be recovered from commutators of flows: the Lie bracket is the infinitesimal failure of invariant flows to commute (compare [[lie-groups/left-invariant-fields-lie-algebra-lemma|the bracket lemma for left-invariant fields]] and the structure encoded by the [[lie-groups/maurer-cartan-equation|Maurer–Cartan equation]]).
