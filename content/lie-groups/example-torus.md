---
title: "Example: the torus $T^n$"
description: "The -torus is a connected abelian Lie group with Lie algebra and exponential map ."
---

The **$n$-torus** is the Lie group
\[
T^n := (S^1)^n \cong (\mathbb R/2\pi\mathbb Z)^n.
\]
It is a connected {{< knowl id="abelian-lie-group" text="abelian Lie group" >}}.

## Lie algebra and exponential (explicit)
The Lie algebra is
\[
\mathrm{Lie}(T^n)\cong \mathbb R^n
\]
as an {{< knowl id="abelian-lie-algebra" text="abelian Lie algebra" >}}. Writing a vector $\theta=(\theta_1,\dots,\theta_n)\in\mathbb R^n$, the {{< knowl id="exponential-map-lie-group" text="exponential map" >}} is
\[
\exp(\theta) = (e^{i\theta_1},\dots,e^{i\theta_n})\in (S^1)^n.
\]
The kernel is the lattice
\[
\ker(\exp)= (2\pi\mathbb Z)^n,
\]
so $\mathbb R^n \to T^n$ is the universal covering homomorphism (compare {{< knowl id="covering-lie-group" text="covering Lie groups" >}} and {{< knowl id="universal-covering-group" text="universal cover" >}}).

## One-parameter subgroups (calculation)
Given $a=(a_1,\dots,a_n)\in\mathbb R^n$, the associated {{< knowl id="one-parameter-subgroup" text="one-parameter subgroup" >}} is
\[
\gamma_a(t)=\exp(ta)=(e^{ita_1},\dots,e^{ita_n}).
\]
This subgroup is closed (a subtorus) iff the coordinates of $a$ are rationally related; otherwise its image is dense in a subtorus.

**Context.** The torus is the model for maximal tori in compact Lie groups (see {{< knowl id="maximal-torus-theorem" text="maximal torus theorem" >}}) and for the structure of connected abelian Lie groups (see {{< knowl id="connected-abelian-lie-group-structure" text="connected abelian Lie group structure" >}}).
