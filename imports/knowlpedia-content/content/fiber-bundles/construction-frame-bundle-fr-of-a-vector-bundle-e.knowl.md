+++
id = "fiber-bundles/construction-frame-bundle-fr-of-a-vector-bundle-e"
title = "Construction: Frame bundle Fr(E) of a vector bundle E"
kind = "knowl"
summary = "Define the principal GL(n)-bundle of frames of a rank-n vector bundle."
aliases = ["construction-frame-bundle-fr-of-a-vector-bundle-e", "Construction: Frame bundle Fr(E) of a vector bundle E"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/construction-frame-bundle-fr-of-a-vector-bundle-e.md"
+++

Let $\pi:E\to M$ be a smooth real vector bundle of rank $n$ over a [[fiber-bundles/smooth-manifold|smooth manifold]] $M$.

## Construction (frame bundle)

The **frame bundle** of $E$ is
\[
\mathrm{Fr}(E):=\bigsqcup_{x\in M}\mathrm{Iso}(\mathbb R^n,E_x),
\]
the set of linear isomorphisms $u:\mathbb R^n\to E_x$ for varying $x$. An element of $\mathrm{Fr}(E)$ is called a **frame** (or ordered basis) of the fiber $E_x$.

There is a smooth projection $\mathrm{Fr}(E)\to M$ sending $u$ to its basepoint $x$. The general linear group $\mathrm{GL}(n,\mathbb R)$ acts on the right by
\[
u\cdot A := u\circ A,\qquad A\in \mathrm{GL}(n,\mathbb R),
\]
making $\mathrm{Fr}(E)\to M$ into a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with $G=\mathrm{GL}(n,\mathbb R)$.

Local trivializations of $E$ give local trivializations of $\mathrm{Fr}(E)$: if $E|_{U}\cong U\times\mathbb R^n$, then
\[
\mathrm{Fr}(E)|_U \cong U\times \mathrm{GL}(n,\mathbb R).
\]

## Examples

1. **Tangent bundle.** For $E=TM$, the [[fiber-bundles/tangent-bundle|tangent bundle]] of $M$, $\mathrm{Fr}(TM)$ is the usual frame bundle of the manifold.

2. **Trivial bundle.** If $E\cong M\times\mathbb R^n$, then $\mathrm{Fr}(E)\cong M\times \mathrm{GL}(n,\mathbb R)$ as principal bundles.

3. **Oriented frames.** If $E$ is oriented, the subspace of positively oriented frames forms a principal $\mathrm{GL}^+(n,\mathbb R)$-subbundle of $\mathrm{Fr}(E)$.
