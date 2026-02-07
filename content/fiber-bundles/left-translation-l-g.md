---
title: "Left Translation on a Lie Group"
description: "For g G, the diffeomorphism L_g:G G, L_g(h)=gh, used to transport geometric data by left multiplication."
---

Let \(G\) be a {{< knowl id="lie-group" text="Lie group" >}} and fix an element \(g\in G\).

**Definition (left translation).**  
The **left translation by \(g\)** is the map
\[
L_g:G\longrightarrow G,\qquad L_g(h)=gh.
\]
Because group multiplication on a Lie group is a {{< knowl id="smooth-map" text="smooth map" >}}, each \(L_g\) is smooth. Moreover, \(L_g\) is a {{< knowl id="diffeomorphism" text="diffeomorphism" >}} with inverse \(L_{g^{-1}}\).

Applying the {{< knowl id="differential-pushforward-of-a-smooth-map" text="differential (pushforward)" >}} gives linear isomorphisms on tangent spaces:
\[
(dL_g)_h:T_hG\longrightarrow T_{gh}G.
\]
This is a fundamental way to move tangent vectors between the {{< knowl id="tangent-space-at-a-point" text="tangent spaces" >}} of \(G\). In particular, left translations are used to define {{< knowl id="left-invariant-vector-field" text="left-invariant vector fields" section="lie-groups">}} and to construct the {{< knowl id="exponential-map-lie-group-exponential" text="exponential map" >}} via flows.

The family \(\{L_g\}_{g\in G}\) satisfies the representation property
\[
L_g\circ L_h=L_{gh},\qquad L_e=\mathrm{id}_G.
\]
For comparison, one can also transport data via {{< knowl id="right-translation-r-g" text="right translations" >}}.

### Examples

1. **\((\mathbb R^n,+)\).**  
   For the additive Lie group, \(L_a(x)=a+x\). The differential \((dL_a)_x\) is the identity map on \(\mathbb R^n\) for every \(x\).

2. **Matrix groups.**  
   If \(G\subseteq GL(n,\mathbb R)\), then \(L_A(B)=AB\). Identifying \(T_BG\) with an appropriate subspace of matrices, \((dL_A)_B\) acts by left multiplication:
   \[
   (dL_A)_B(V)=AV.
   \]

3. **Circle group \(S^1\).**  
   Writing elements as complex numbers of unit modulus, \(L_{e^{i\theta}}(e^{it})=e^{i(\theta+t)}\). Geometrically, left translation rotates the circle by angle \(\theta\).
