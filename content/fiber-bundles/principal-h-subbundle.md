---
title: "Principal H-subbundle"
description: "An H-invariant submanifold of a principal G-bundle that is itself a principal H-bundle over the same base."
---

Let $P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure group a {{< knowl id="lie-group" text="Lie group" >}} $G$, and let $H\subset G$ be a Lie subgroup.

A **principal H-subbundle** of $P$ is a submanifold $Q\subset P$ such that:
1. $\pi(Q)=M$ and $\pi|_Q:Q\to M$ is a surjective submersion,
2. $Q$ is preserved by the restricted {{< knowl id="right-principal-action" text="right action" >}} of $H$, i.e. $q\cdot h\in Q$ for all $q\in Q$, $h\in H$,
3. the $H$-action on $Q$ is free and transitive on the fibers of $\pi|_Q$.

Then $(Q,\pi|_Q,M,H)$ is a principal $H$-bundle, and the inclusion $Q\hookrightarrow P$ is $H$-equivariant. Giving such a subbundle is precisely the concrete form of a {{< knowl id="reduction-of-structure-group" text="reduction of structure group" >}} from $G$ to $H$.

## Examples
1. **Orthonormal frames.** For a Riemannian manifold, the orthonormal frame bundle is a principal $O(n)$-subbundle of the full frame bundle (a $GL(n)$-bundle).
2. **Trivial bundle subgroups.** If $P=M\times G$, then $Q:=M\times H$ is a principal $H$-subbundle.
3. **Unit circle subbundle of a line bundle.** For a Hermitian complex line bundle $L\to M$, the unit circle bundle $S(L)$ is a principal $U(1)$-subbundle of the principal $\mathbb{C}^\ast$-bundle of nonzero vectors in $L$.
