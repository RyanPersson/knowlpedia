+++
id = "fiber-bundles/section-of-ad"
title = "Section of Ad(P)"
kind = "knowl"
summary = "A smooth choice of an element in each fiber of the adjoint bundle, equivalently a globally defined gauge function with conjugation gluing laws."
aliases = ["section-of-ad", "Section of Ad(P)"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/section-of-ad.md"
+++

Let $\mathrm{Ad}(P)\to M$ be the [[fiber-bundles/adjoint-bundle-p-g-g-with-conjugation-action|adjoint bundle]] of a principal $G$-bundle $P$.

A **section of $\mathrm{Ad}(P)$** is a smooth map
\[
s:M\to \mathrm{Ad}(P)
\]
such that $\pi_{\mathrm{Ad}}\circ s=\mathrm{id}_M$, where $\pi_{\mathrm{Ad}}:\mathrm{Ad}(P)\to M$ is the bundle projection.

Equivalently, choose an [[topology/open-cover|open cover]] $\{U_i\}$ and local trivializations of $P$ with [[fiber-bundles/principal-bundle-transition-function|transition functions]] $g_{ij}:U_i\cap U_j\to G$. Then a section $s$ is represented by smooth maps $a_i:U_i\to G$ such that on overlaps
\[
a_j(x)=g_{ij}(x)^{-1}\,a_i(x)\,g_{ij}(x).
\]
This is the “gauge function” gluing law: local representatives differ by conjugation with the bundle cocycle.

Under pointwise multiplication in the fibers, the set of sections $\Gamma(\mathrm{Ad}(P))$ is a group, canonically isomorphic to the [[fiber-bundles/gauge-group|gauge group]] of $P$.

## Examples
1. **Trivial or trivialized case.** If $\mathrm{Ad}(P)\cong M\times G$, then sections are exactly smooth maps $a:M\to G$.
2. **Abelian groups.** If $G$ is abelian, conjugation is trivial, so every section is again just a smooth map $M\to G$, regardless of whether $P$ is trivial.
3. **Central elements.** If $z\in Z(G)$, then the constant choice “$z$ in every fiber” defines a global section of $\mathrm{Ad}(P)$; it corresponds to the gauge transformation $p\mapsto p\cdot z$.
