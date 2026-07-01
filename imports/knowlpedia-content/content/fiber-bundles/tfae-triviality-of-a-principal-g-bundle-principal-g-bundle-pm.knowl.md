+++
id = "fiber-bundles/tfae-triviality-of-a-principal-g-bundle-principal-g-bundle-pm"
title = "Equivalent conditions for triviality of a principal bundle"
kind = "knowl"
summary = "A principal G bundle is trivial exactly when it has a global section, or equivalently when its transition cocycle is cohomologous to the identity."
aliases = ["tfae-triviality-of-a-principal-g-bundle-principal-g-bundle-pm", "Equivalent conditions for triviality of a principal bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/tfae-triviality-of-a-principal-g-bundle-principal-g-bundle-pm.md"
+++

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with structure group $G$.

## Theorem (TFAE: principal bundle triviality)
The following are equivalent:

1. (**Bundle isomorphism with the product**)
   $P$ is trivial, i.e. there exists a [[fiber-bundles/principal-bundle-isomorphism|principal bundle isomorphism]]
   \[
   \Phi:P \stackrel{\cong}{\longrightarrow} M\times G
   \]
   commuting with the projections to $M$ and intertwining the right $G$-actions (see [[fiber-bundles/trivial-principal-bundle-mgm|trivial principal bundle]]).

2. (**Existence of a global section**)
   $P$ admits a smooth global section $s:M\to P$ with $\pi\circ s=\mathrm{id}_M$ (see [[fiber-bundles/section-of-ad|section]] for the general notion of section, and compare the principal-bundle criterion [[fiber-bundles/trivial-principal-bundle-criterion-global-section-principal-bundle-is-trivial|global section implies triviality]] together with its converse [[fiber-bundles/converse-triviality-criterion-trivial-principal-bundle-admits-a-global-section|trivial bundles admit sections]]).

3. (**Transition functions can be made trivial**)
   There exists a bundle atlas for $P$ whose transition functions are all the identity element of $G$ on overlaps. Equivalently, the transition cocycle is [[fiber-bundles/equivalence-of-cocycles|equivalent (cohomologous) to the trivial cocycle]] (see [[fiber-bundles/principal-bundle-transition-function|transition functions]] and [[fiber-bundles/cocycle-condition-for-transition-functions|cocycle condition]]).

4. (**A global equivariant trivialization map**)
   There exists a smooth map $f:P\to G$ such that
   \[
   f(pg)=g^{-1}f(p)\qquad\text{for all }p\in P,\ g\in G.
   \]
   (This is the condition that $f$ is equivariant for the right action on $P$ and the right-translation action on $G$; compare [[fiber-bundles/equivariant-map|equivariant maps]].)

The equivalence (1) $\Leftrightarrow$ (2) is the most frequently used in practice: a global section picks a preferred point in each fiber, and translating that point by $G$ produces the explicit trivialization.

## Examples
1. **Hopf bundle is not trivial.**
   The Hopf fibration $S^3\to S^2$ is a nontrivial principal $U(1)$-bundle (see [[fiber-bundles/hopf-fibration-s3s2-as-a-principal-u-bundle|Hopf fibration]]). By the theorem, it admits no global section; this is a standard instance of [[fiber-bundles/counterexample-nontrivial-principal-bundle-admitting-no-global-section|a nontrivial principal bundle with no global section]].

2. **Triviality from a global gauge choice on a trivial bundle.**
   On $P=M\times G$, the map $s(x)=(x,e)$ is a global section, so the theorem recovers triviality immediately. In this case, choosing a section is exactly choosing a global “gauge,” and it identifies principal connections with $\mathfrak g$-valued $1$-forms on $M$ (compare [[fiber-bundles/flat-connection-a0-on-a-trivial-bundle|flat connection on a trivial bundle]] and [[fiber-bundles/pure-gauge-connection-ag-1dg-on-a-trivial-bundle|pure gauge connections]]).

3. **Principal bundles over the circle for connected groups.**
   If $G$ is connected, every principal $G$-bundle over $S^1$ is trivial, hence admits a global section. This aligns with the clutching description in [[fiber-bundles/principal-bundle-over-s1-defined-by-a-clutching-function|principal bundles over S1 via clutching]], where all clutching data become equivalent to the identity when $G$ has a single connected component.
