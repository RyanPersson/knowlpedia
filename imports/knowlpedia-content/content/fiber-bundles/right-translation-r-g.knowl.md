+++
id = "fiber-bundles/right-translation-r-g"
title = "Right Translation on a Lie Group"
kind = "knowl"
summary = "For g G, the diffeomorphism R_g:G G, R_g(h)=hg, used to transport geometric data by right multiplication."
aliases = ["right-translation-r-g", "Right Translation on a Lie Group"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/right-translation-r-g.md"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] and fix an element \(g\in G\).

**Definition (right translation).**
The **right translation by \(g\)** is the map
\[
R_g:G\longrightarrow G,\qquad R_g(h)=hg.
\]
Since multiplication in a Lie group is a [[fiber-bundles/smooth-map|smooth map]], each \(R_g\) is smooth. Moreover, \(R_g\) is a [[fiber-bundles/diffeomorphism|diffeomorphism]] with inverse \(R_{g^{-1}}\).

Its [[fiber-bundles/differential-pushforward-of-a-smooth-map|differential (pushforward)]] gives linear isomorphisms
\[
(dR_g)_h:T_hG\longrightarrow T_{hg}G,
\]
so right translations also transport vectors between [[fiber-bundles/tangent-space-at-a-point|tangent spaces]]. They are used to define [[lie-groups/right-invariant-vector-field|right-invariant vector fields]].

The family \(\{R_g\}_{g\in G}\) satisfies
\[
R_g\circ R_h=R_{hg},\qquad R_e=\mathrm{id}_G,
\]
so the assignment \(g\mapsto R_g\) is an antihomomorphism into the diffeomorphism group. For a left-multiplicative analogue, compare with [[fiber-bundles/left-translation-l-g|left translations]].

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
