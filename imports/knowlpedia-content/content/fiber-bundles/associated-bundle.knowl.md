+++
id = "fiber-bundles/associated-bundle"
title = "Associated bundle"
kind = "knowl"
summary = "A fiber bundle built from a principal bundle and a left group action on a model fiber by taking a quotient of the product."
aliases = ["associated-bundle", "Associated bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/associated-bundle.md"
+++

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with right action $p\cdot g$, and let $F$ be a smooth manifold equipped with a smooth left action of the [[fiber-bundles/lie-group|Lie group]] $G$.

The **associated bundle** with fiber $F$ is the quotient
\[
P\times_G F := (P\times F)/\sim,
\]
where the equivalence relation is
\[
(p\cdot g,\, f)\sim (p,\, g\cdot f)\qquad (p\in P,\; f\in F,\; g\in G).
\]
Write $[p,f]$ for the equivalence class of $(p,f)$. The projection map
\[
\pi_F:P\times_G F \to M,\qquad \pi_F([p,f])=\pi(p)
\]
is well-defined, and $P\times_G F$ is a smooth fiber bundle over $M$ with typical fiber $F$.

Concretely, $P\times_G F$ is a [[fiber-bundles/bundle-of-orbits|bundle of orbits]]: it is obtained from the product $P\times F$ by dividing out the diagonal $G$-action determined by the right action on $P$ and the left action on $F$. When $F$ is a vector space with a linear action, this specializes to an [[fiber-bundles/associated-vector-bundle|associated vector bundle]].

## Examples
1. **Tangent bundle from frames.** If $P=\mathrm{Fr}(M)$ and $F=\mathbb{R}^n$ with the standard left action of $GL(n)$, then $P\times_G F$ is canonically isomorphic to the [[fiber-bundles/tangent-bundle|tangent bundle]] $TM$.
2. **Line bundles from $U(1)$-bundles.** If $G=U(1)$ and $F=\mathbb{C}$ with the usual multiplication action, then $P\times_{U(1)}\mathbb{C}$ is a complex line bundle whose unit circle bundle recovers $P$.
3. **Adjoint bundle.** Taking $F=G$ with conjugation action produces the adjoint bundle $\mathrm{Ad}(P)$ (a bundle of groups over $M$).
