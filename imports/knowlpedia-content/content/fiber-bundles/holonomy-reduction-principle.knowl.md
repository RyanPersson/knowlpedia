+++
id = "fiber-bundles/holonomy-reduction-principle"
title = "Holonomy reduction principle"
kind = "knowl"
summary = "If the holonomy of a connection lies in a subgroup H, the principal bundle admits an H-reduction preserved by the connection."
aliases = ["holonomy-reduction-principle", "Holonomy reduction principle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/holonomy-reduction-principle.md"
+++

Let $M$ be a connected [[fiber-bundles/smooth-manifold|smooth manifold]] and let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with structure group a [[fiber-bundles/lie-group|Lie group]] $G$. Fix a [[fiber-bundles/principal-connection|principal connection]] $\omega$ on $P$. Let $H\subseteq G$ be a Lie subgroup.

## Principle (holonomy containment implies reduction)

Suppose there exists a point $p\in P$ such that the [[fiber-bundles/holonomy-group|holonomy group]] satisfies
\[
\mathrm{Hol}_p(\omega)\subseteq H.
\]
Then there exists a principal $H$-subbundle $Q\subseteq P$ (an $H$-reduction of structure group) with the following properties:

1. $Q$ is preserved by the horizontal distribution of $\omega$ (equivalently, any $\omega$-horizontal curve starting in $Q$ remains in $Q$), and
2. the restriction of $\omega$ to $Q$ is a principal connection on $Q$ with values in the Lie algebra $\mathfrak{h}$.

Conversely, if $Q\subseteq P$ is a principal $H$-subbundle such that the restriction $\omega|_Q$ is an $H$-connection on $Q$, then for every $q\in Q$ one has $\mathrm{Hol}_q(\omega)\subseteq H$.

Equivalently (and often more practical): there exists such an $H$-reduction preserved by $\omega$ if and only if the associated bundle $P\times_G (G/H)\to M$ admits a global section that is parallel with respect to the induced connection (i.e., constant under [[fiber-bundles/parallel-transport|parallel transport]]).

## Examples

1. **Riemannian holonomy yields an orthonormal frame reduction.**
   For a Riemannian manifold, the Levi-Civita connection has holonomy contained in $\mathrm{O}(n)$, so the $\mathrm{GL}(n,\mathbb{R})$ frame bundle reduces to the orthonormal frame bundle in a way preserved by the connection.

2. **Kähler holonomy reduces to a unitary group.**
   For a Kähler manifold, the Levi-Civita holonomy is contained in $\mathrm{U}(n)$, so the real frame bundle reduces to a $\mathrm{U}(n)$-subbundle compatible with the complex structure and metric.

3. **Holonomy contained in the identity gives a global parallel frame on simply connected bases.**
   If $\mathrm{Hol}_p(\omega)=\{e\}$ and $M$ is simply connected, then parallel transport is path-independent and produces a global trivialization by parallel frames; in particular one gets a reduction to the trivial subgroup.
