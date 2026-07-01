+++
id = "fiber-bundles/local-gauge-transformation"
title = "Local gauge transformation"
kind = "knowl"
summary = "A smooth group-valued function on an open set that represents a gauge transformation in a chosen local trivialization."
aliases = ["local-gauge-transformation", "Local gauge transformation"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/local-gauge-transformation.md"
+++

Let $\pi:P\to M$ be a principal $G$-bundle, and let $U\subset M$ be an open set (typically from an [[topology/open-cover|open cover]]) on which we choose an [[fiber-bundles/equivariant-local-trivialization|equivariant local trivialization]] $\psi:\pi^{-1}(U)\to U\times G$.

A **local gauge transformation** on $U$ is a smooth map
\[
g:U\to G
\]
viewed as acting on the local product $U\times G$ by
\[
(x,h)\longmapsto (x,\,g(x)\,h).
\]
Equivalently, it acts on the associated local section $s(x)=\psi^{-1}(x,e)$ by
\[
s(x)\longmapsto s(x)\cdot g(x).
\]

If $\Phi$ is a global [[fiber-bundles/gauge-transformation|gauge transformation]] of $P$, then in any chosen trivialization over $U$ it is represented by a unique local gauge transformation $g:U\to G$ via
\[
\psi\circ\Phi\circ\psi^{-1}(x,h)=(x,\,g(x)\,h).
\]

When a [[fiber-bundles/principal-connection|principal connection]] is present, local gauge transformations also act on the resulting local connection 1-forms by the usual formula
\[
A \mapsto g^{-1}Ag + g^{-1}dg,
\]
where $dg$ is computed using the [[fiber-bundles/exterior-derivative|exterior derivative]].

## Examples
1. **Electromagnetism.** For $G=U(1)$, a local gauge transformation is $g=e^{i\chi}$ with $\chi:U\to\mathbb{R}$, and the local potential transforms by $A\mapsto A+d\chi$.
2. **Change of local frame.** For a rank-$n$ vector bundle, a change of local frame on $U$ is given by $g:U\to GL(n)$; it is exactly a local gauge transformation for the associated frame bundle.
3. **Transition functions as local gauge data.** On an overlap $U_i\cap U_j$, the transition function $g_{ij}:U_i\cap U_j\to G$ describes how local sections differ, and can be read as the local gauge transformation relating two trivializations.
