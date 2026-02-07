---
title: "Example: $U(1)$ (the circle group)"
description: "has Lie algebra and exponential map with kernel ."
---

The circle group is the compact Lie group
\[
U(1)=\{z\in\mathbb C:|z|=1\}\cong S^1.
\]
It is connected and {{< knowl id="abelian-lie-group" text="abelian" >}}.

## Lie algebra
Its Lie algebra (as a real Lie algebra) is
\[
\mathfrak u(1)= i\mathbb R,
\]
with trivial bracket, so it is an {{< knowl id="abelian-lie-algebra" text="abelian Lie algebra" >}} (compare {{< knowl id="unitary-lie-algebra" text="unitary Lie algebra" >}} for general $U(n)$).

## Exponential map and universal cover (explicit calculation)
Identifying $\mathfrak u(1)\cong \mathbb R$ via $t\mapsto it$, the {{< knowl id="exponential-map-lie-group" text="exponential map" >}} is
\[
\exp(it)=e^{it}.
\]
Its kernel is
\[
\ker(\exp)=\{2\pi k\,i : k\in\mathbb Z\}\cong 2\pi\mathbb Z,
\]
so the map
\[
p:\mathbb R\to U(1),\qquad p(t)=e^{it},
\]
is a {{< knowl id="covering-lie-group" text="covering homomorphism" >}} and in fact the {{< knowl id="universal-covering-group" text="universal covering group" >}} of $U(1)$.

## One-parameter subgroups
Every {{< knowl id="one-parameter-subgroup" text="one-parameter subgroup" >}} of $U(1)$ has the form $t\mapsto e^{iat}$ for some $a\in\mathbb R$.

**Context.** $U(1)$ is the basic building block of tori (compare {{< knowl id="example-torus" text="the torus example" >}}) and the prototypical example where the exponential map is surjective but not injective.
