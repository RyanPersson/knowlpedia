---
title: "Maximal torus theorem"
description: "In a compact connected Lie group, maximal tori exist and are all conjugate."
---

Let $G$ be a {{< knowl id="compact-lie-group" text="compact Lie group" >}} that is also {{< knowl id="connected-lie-group" text="connected" >}}. A **torus** means a Lie group isomorphic to $(S^1)^r$; see {{< knowl id="example-torus" text="the torus example" >}} and {{< knowl id="connected-abelian-lie-group-structure" text="the structure of connected abelian Lie groups" >}}.

## Theorem (maximal tori)
1. (**Existence**) $G$ contains a maximal torus $T\subseteq G$, i.e. a connected, compact, abelian Lie subgroup not properly contained in any larger connected, compact, abelian subgroup.

2. (**Conjugacy**) Any two maximal tori $T_1,T_2\subseteq G$ are conjugate: there exists $g\in G$ such that
   $$
   T_2=gT_1g^{-1}.
   $$

3. (**Every element lies in a maximal torus**) For every $x\in G$ there exists a maximal torus $T\subseteq G$ with $x\in T$.

## Why it matters
A maximal torus is the compact-group analogue of a {{< knowl id="cartan-subalgebra" text="Cartan subalgebra" >}}: its Lie algebra $\mathfrak t=\operatorname{Lie}(T)$ is a maximal abelian subalgebra of $\mathfrak g=\operatorname{Lie}(G)$ consisting of semisimple elements (over $\Bbb C$). The conjugacy statement implies that many structural invariants of $G$ can be computed from $\mathfrak t$ up to the action of the {{< knowl id="weyl-group" text="Weyl group" >}}, leading to root data and classification results.
