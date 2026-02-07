---
title: "Right Translation on a Lie Group"
description: "For g G, the diffeomorphism R_g:G G, R_g(h)=hg, used to transport geometric data by right multiplication."
---

Let \(G\) be a {{< knowl id="lie-group" text="Lie group" >}} and fix an element \(g\in G\).

**Definition (right translation).**  
The **right translation by \(g\)** is the map
\[
R_g:G\longrightarrow G,\qquad R_g(h)=hg.
\]
Since multiplication in a Lie group is a {{< knowl id="smooth-map" text="smooth map" >}}, each \(R_g\) is smooth. Moreover, \(R_g\) is a {{< knowl id="diffeomorphism" text="diffeomorphism" >}} with inverse \(R_{g^{-1}}\).

Its {{< knowl id="differential-pushforward-of-a-smooth-map" text="differential (pushforward)" >}} gives linear isomorphisms
\[
(dR_g)_h:T_hG\longrightarrow T_{hg}G,
\]
so right translations also transport vectors between {{< knowl id="tangent-space-at-a-point" text="tangent spaces" >}}. They are used to define {{< knowl id="right-invariant-vector-field" text="right-invariant vector fields" section="lie-groups">}}.

The family \(\{R_g\}_{g\in G}\) satisfies
\[
R_g\circ R_h=R_{hg},\qquad R_e=\mathrm{id}_G,
\]
so the assignment \(g\mapsto R_g\) is an antihomomorphism into the diffeomorphism group. For a left-multiplicative analogue, compare with {{< knowl id="left-translation-l-g" text="left translations" >}}.

### Examples

1. **\((\mathbb R^n,+)\).**  
   For the additive Lie group, \(R_a(x)=x+a\). As with left translation, \((dR_a)_x\) is the identity on \(\mathbb R^n\).

2. **Matrix groups.**  
   If \(G\subseteq GL(n,\mathbb R)\), then \(R_A(B)=BA\). On tangent vectors represented by matrices \(V\), the differential acts by right multiplication:
   \[
   (dR_A)_B(V)=VA.
   \]

3. **Circle group \(S^1\).**  
   Writing elements as complex numbers, \(R_{e^{i\theta}}(e^{it})=e^{i(t+\theta)}\). For the abelian group \(S^1\), left and right translations agree.
