+++
id = "fiber-bundles/direct-sum-vector-bundle"
title = "Direct sum vector bundle (Whitney sum)"
kind = "knowl"
summary = "The bundle over a common base whose fiber is the direct sum of the fibers of two bundles."
aliases = ["direct-sum-vector-bundle", "Direct sum vector bundle (Whitney sum)"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/direct-sum-vector-bundle.md"
+++

Let $\pi_E:E\to M$ and $\pi_F:F\to M$ be smooth vector bundles over the same [[fiber-bundles/smooth-manifold|smooth manifold]] $M$. Their **direct sum bundle** (or **Whitney sum**) is the vector bundle
\[
\pi_{E\oplus F}:E\oplus F \to M
\]
defined by
\[
E\oplus F := \{(e,f)\in E\times F : \pi_E(e)=\pi_F(f)\},
\qquad
\pi_{E\oplus F}(e,f):=\pi_E(e)=\pi_F(f),
\]
with fiberwise vector space structure
\[
(E\oplus F)_x \cong E_x\oplus F_x.
\]
Local trivializations of $E$ and $F$ over an open set $U$ induce a local trivialization of $E\oplus F$ over $U$ by taking the product trivialization and using the usual direct sum on $\mathbb F^{r}\oplus\mathbb F^{s}$.

The projections $\mathrm{pr}_E:E\oplus F\to E$ and $\mathrm{pr}_F:E\oplus F\to F$ are [[fiber-bundles/vector-bundle-morphism|vector bundle morphisms]] over $\mathrm{id}_M$.

The rank satisfies $\mathrm{rank}(E\oplus F)=\mathrm{rank}(E)+\mathrm{rank}(F)$ (see [[fiber-bundles/rank-of-a-vector-bundle|rank of a vector bundle]]).

## Examples
1. **Tangent plus cotangent.** $TM\oplus T^*M$ is a bundle whose fiber at $x$ is $T_xM\oplus T_x^*M$; it is fundamental in generalized geometry.

2. **Trivial sums.** If $E\cong M\times \mathbb F^r$ and $F\cong M\times \mathbb F^s$, then $E\oplus F\cong M\times \mathbb F^{r+s}$.

3. **Splitting by a metric.** If $E$ has a [[fiber-bundles/bundle-metric|bundle metric]] and $S\subset E$ is a subbundle, then (under standard hypotheses) $E$ can be identified with $S\oplus S^\perp$ by mapping $(s,t)$ to $s+t$ fiberwise.
