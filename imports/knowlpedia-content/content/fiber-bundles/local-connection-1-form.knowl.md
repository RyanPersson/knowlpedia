+++
id = "fiber-bundles/local-connection-1-form"
title = "Local connection 1-form"
kind = "knowl"
summary = "A Lie algebra valued 1-form on an open set obtained by pulling back a principal connection along a local section"
aliases = ["local-connection-1-form", "Local connection 1-form"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/local-connection-1-form.md"
+++

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with Lie algebra $\mathfrak g$, and let $\omega\in\Omega^1(P;\mathfrak g)$ be a [[fiber-bundles/connection-1-form-on-a-principal-bundle|connection 1-form]] representing a [[fiber-bundles/principal-connection|principal connection]].

Given a local section $s:U\to P$ over an open set $U\subseteq M$, the **local connection 1-form** (also called the gauge potential in that trivialization) is the $\mathfrak g$-valued 1-form
\[
A:=s^*\omega \in \Omega^1(U;\mathfrak g).
\]
This is the local representative of the global connection in the trivialization determined by $s$ (compare [[fiber-bundles/construction-local-trivialization-from-a-local-section|local trivialization from a local section]]).

### Change of section (local gauge transformation)
If $s'(x)=s(x)\cdot g(x)$ for a smooth map $g:U\to G$ (a [[fiber-bundles/local-gauge-transformation|local gauge transformation]]), then the pulled-back forms satisfy the standard transformation law
\[
A' = g^{-1} A g + g^{-1}dg,
\]
as recorded in [[fiber-bundles/lemma-local-gauge-transformation-law-ag-g-1ag-g-1dg|the local gauge transformation law]].

### On overlaps
If $\{s_i:U_i\to P\}$ is a system of local sections and $g_{ij}:U_i\cap U_j\to G$ are the associated transition functions defined by $s_j=s_i\,g_{ij}$ (see [[fiber-bundles/construction-transition-functions-g-iju-iu-jg-from-local-sections|transition functions from local sections]]), then on $U_i\cap U_j$ the local forms obey
\[
A_j = g_{ij}^{-1} A_i g_{ij} + g_{ij}^{-1}dg_{ij}.
\]

The corresponding local curvature 2-form is
\[
F:=dA + A\wedge A,
\]
as in [[fiber-bundles/local-curvature-formula-f-da-aa|the local curvature formula]], and it transforms by conjugation (see [[fiber-bundles/lemma-local-curvature-transformation-law-fg-g-1fg|local curvature transformation law]]).

## Examples
1. **Trivial principal bundle.**
   If $P\cong M\times G$ is trivial, choosing the global section $s(x)=(x,e)$ identifies a principal connection with a single global $\mathfrak g$-valued 1-form $A$ on $M$. The [[fiber-bundles/flat-connection-a0-on-a-trivial-bundle|flat connection]] corresponds to $A=0$, while a [[fiber-bundles/pure-gauge-connection-ag-1dg-on-a-trivial-bundle|pure gauge]] connection has the form $A=g^{-1}dg$.

2. **Dirac monopole on the Hopf bundle.**
   For the [[fiber-bundles/hopf-fibration-s3s2-as-a-principal-u-bundle|Hopf fibration]] as a principal $U(1)$-bundle, the [[fiber-bundles/dirac-monopole-connection-on-the-hopf-bundle|Dirac monopole connection]] is described by two local connection 1-forms $A_N$ and $A_S$ on the northern and southern charts of $S^2$, related on the overlap by a $U(1)$-valued gauge function.

3. **Levi-Civita connection in a local frame.**
   For a Riemannian manifold, the [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]] can be viewed as a principal connection on the [[fiber-bundles/orthonormal-frame-bundle-o-of-a-riemannian-manifold|orthonormal frame bundle]]. Choosing a local orthonormal frame gives a matrix-valued local connection 1-form whose entries are the usual connection coefficients; its curvature is the matrix of curvature 2-forms in that frame (see [[fiber-bundles/curvature-2-form-in-a-frame|curvature 2-form in a frame]]).
