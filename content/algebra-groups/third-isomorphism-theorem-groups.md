---
title: "Third Isomorphism Theorem (Groups)"
description: "If N ⊆ K ⊲ G with N ⊲ G, then (G/N)/(K/N) ≅ G/K"
---

**Third Isomorphism Theorem (Groups).**
Let $G$ be a {{< knowl id="group" text="group" >}} and let $N \trianglelefteq G$ and $K \trianglelefteq G$ be {{< knowl id="normal-subgroup" text="normal subgroups" >}} with $N \subseteq K$. Then $K/N$ is a normal subgroup of $G/N$, and there is a canonical isomorphism of {{< knowl id="quotient-group" text="quotient groups" >}}
$$
(G/N)/(K/N) \cong G/K,
$$
induced by the map $gN \mapsto gK$.

This theorem formalizes the idea that "quotienting by $N$ and then by $K/N$" is the same as quotienting directly by $K$. It can be viewed as a special case of {{< knowl id="correspondence-theorem-groups" text="the correspondence theorem" >}}, or proved directly using {{< knowl id="first-isomorphism-theorem-groups" text="the first isomorphism theorem" >}}.

**Proof sketch.**
Define a homomorphism $G/N \to G/K$ by $gN \mapsto gK$; it is surjective. Its kernel is precisely $K/N$. Apply the first isomorphism theorem to conclude $(G/N)/(K/N) \cong G/K$.
