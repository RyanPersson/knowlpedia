+++
id = "lie-groups/example-u1-circle"
title = "Example: $U(1)$ (the circle group)"
kind = "knowl"
summary = "has Lie algebra and exponential map with kernel ."
aliases = ["example-u1-circle", "Example: $U(1)$ (the circle group)"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/example-u1-circle.md"
+++

The circle group is the compact Lie group
\[
U(1)=\{z\in\mathbb C:|z|=1\}\cong S^1.
\]
It is connected and [[lie-groups/abelian-lie-group|abelian]].

## Lie algebra
Its Lie algebra (as a real Lie algebra) is
\[
\mathfrak u(1)= i\mathbb R,
\]
with trivial bracket, so it is an [[lie-groups/abelian-lie-algebra|abelian Lie algebra]] (compare [[lie-groups/unitary-lie-algebra|unitary Lie algebra]] for general $U(n)$).

## Exponential map and universal cover (explicit calculation)
Identifying $\mathfrak u(1)\cong \mathbb R$ via $t\mapsto it$, the [[lie-groups/exponential-map-lie-group|exponential map]] is
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
is a [[lie-groups/covering-lie-group|covering homomorphism]] and in fact the [[lie-groups/universal-covering-group|universal covering group]] of $U(1)$.

## One-parameter subgroups
Every [[lie-groups/one-parameter-subgroup|one-parameter subgroup]] of $U(1)$ has the form $t\mapsto e^{iat}$ for some $a\in\mathbb R$.

**Context.** $U(1)$ is the basic building block of tori (compare [[lie-groups/example-torus|the torus example]]) and the prototypical example where the exponential map is surjective but not injective.
