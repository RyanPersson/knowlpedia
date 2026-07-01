+++
id = "lie-groups/example-torus"
title = "Example: the torus $T^n$"
kind = "knowl"
summary = "The -torus is a connected abelian Lie group with Lie algebra and exponential map ."
aliases = ["example-torus", "Example: the torus $T^n$"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/example-torus.md"
+++

The **$n$-torus** is the Lie group
\[
T^n := (S^1)^n \cong (\mathbb R/2\pi\mathbb Z)^n.
\]
It is a connected [[lie-groups/abelian-lie-group|abelian Lie group]].

## Lie algebra and exponential (explicit)
The Lie algebra is
\[
\mathrm{Lie}(T^n)\cong \mathbb R^n
\]
as an [[lie-groups/abelian-lie-algebra|abelian Lie algebra]]. Writing a vector $\theta=(\theta_1,\dots,\theta_n)\in\mathbb R^n$, the [[lie-groups/exponential-map-lie-group|exponential map]] is
\[
\exp(\theta) = (e^{i\theta_1},\dots,e^{i\theta_n})\in (S^1)^n.
\]
The kernel is the lattice
\[
\ker(\exp)= (2\pi\mathbb Z)^n,
\]
so $\mathbb R^n \to T^n$ is the universal covering homomorphism (compare [[lie-groups/covering-lie-group|covering Lie groups]] and [[lie-groups/universal-covering-group|universal cover]]).

## One-parameter subgroups (calculation)
Given $a=(a_1,\dots,a_n)\in\mathbb R^n$, the associated [[lie-groups/one-parameter-subgroup|one-parameter subgroup]] is
\[
\gamma_a(t)=\exp(ta)=(e^{ita_1},\dots,e^{ita_n}).
\]
This subgroup is closed (a subtorus) iff the coordinates of $a$ are rationally related; otherwise its image is dense in a subtorus.

**Context.** The torus is the model for maximal tori in compact Lie groups (see [[lie-groups/maximal-torus-theorem|maximal torus theorem]]) and for the structure of connected abelian Lie groups (see [[lie-groups/connected-abelian-lie-group-structure|connected abelian Lie group structure]]).
