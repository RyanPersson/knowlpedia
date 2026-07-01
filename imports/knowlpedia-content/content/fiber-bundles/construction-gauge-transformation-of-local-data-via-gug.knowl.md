+++
id = "fiber-bundles/construction-gauge-transformation-of-local-data-via-gug"
title = "Gauge transformation of local bundle data"
kind = "knowl"
summary = "How transition functions and local connection forms change under a change of local sections."
aliases = ["construction-gauge-transformation-of-local-data-via-gug", "Gauge transformation of local bundle data"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/construction-gauge-transformation-of-local-data-via-gug.md"
+++

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with a [[fiber-bundles/principal-connection|principal connection]] given by a [[fiber-bundles/connection-1-form-on-a-principal-bundle|connection 1-form]] $\omega$.

Fix an open cover $\{U_i\}$ and local sections $s_i:U_i\to P$. Let
- $g_{ij}:U_i\cap U_j\to G$ be the transition functions defined by $s_j=s_i\cdot g_{ij}$ (as in [[fiber-bundles/construction-transition-functions-g-iju-iu-jg-from-local-sections|the construction of transition functions from local sections]]),
- $A_i := s_i^*\omega \in \Omega^1(U_i;\mathfrak g)$ be the corresponding [[fiber-bundles/local-connection-1-form|local connection 1-forms]].

A **local gauge change** is a choice of smooth maps $u_i:U_i\to G$ and new sections
\[
s_i' := s_i\cdot u_i.
\]
This is the local form of a [[fiber-bundles/local-gauge-transformation|local gauge transformation]].

## Transformation of transition functions
On an overlap $U_i\cap U_j$,
\[
s_j' = s_j u_j = s_i g_{ij} u_j = s_i u_i\,(u_i^{-1} g_{ij} u_j).
\]
By uniqueness of transition functions, the new transition functions satisfy
\[
g_{ij}' = u_i^{-1}\, g_{ij}\, u_j.
\]
Thus, changing local sections replaces the cocycle $\{g_{ij}\}$ by an [[fiber-bundles/equivalence-of-cocycles|equivalent cocycle]].

## Transformation of local connection forms
The local connection forms transform by the usual gauge rule:
\[
A_i' = (s_i')^*\omega = \mathrm{Ad}_{u_i^{-1}} A_i + u_i^{-1} d u_i.
\]
This is the statement recorded in [[fiber-bundles/lemma-local-gauge-transformation-law-ag-g-1ag-g-1dg|the local gauge transformation law for A]] and matches [[fiber-bundles/gauge-transform-of-a-local-connection-form|gauge-transforming a local connection form]].

If $F_i$ denotes the local curvature 2-form on $U_i$, then
\[
F_i' = \mathrm{Ad}_{u_i^{-1}} F_i,
\]
as in [[fiber-bundles/lemma-local-curvature-transformation-law-fg-g-1fg|the local curvature transformation law]].

These formulas are the standard local expression of a global [[fiber-bundles/gauge-transformation|gauge transformation]] acting on the space of connections.

## Examples
1. **Trivial bundle on one chart.** On $U$ with a trivialization, a local gauge function $u:U\to G$ sends a $\mathfrak g$-valued 1-form $A$ to
   \[
   A^u = \mathrm{Ad}_{u^{-1}}A + u^{-1}du.
   \]
   For an abelian group (e.g. $U(1)$), $\mathrm{Ad}$ is trivial and this reduces to $A^u = A + u^{-1}du$.

2. **Pure gauge becomes zero.** On a trivial bundle, take $A=u^{-1}du$, the [[fiber-bundles/pure-gauge-connection-ag-1dg-on-a-trivial-bundle|pure gauge connection]]. Gauge transforming by $u$ gives
   \[
   A^u = 0,
   \]
   recovering the [[fiber-bundles/flat-connection-a0-on-a-trivial-bundle|flat connection]] in that gauge.

3. **Changing local sections changes the clutching data by conjugation.** If a principal bundle is presented by transition functions on a two-set cover (a “clutching function” presentation as in [[fiber-bundles/clutching-function|clutching functions]]), replacing the chosen local sections by $s_i'=s_i u_i$ modifies the clutching map by $g' = u^{-1} g\, u$ on the overlap. This does not change the isomorphism class of the bundle, precisely because it is an instance of cocycle equivalence.
