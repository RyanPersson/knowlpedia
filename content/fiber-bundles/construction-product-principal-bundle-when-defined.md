---
title: "Product principal bundle (fiber product over the base)"
description: "Construction of a principal G×H-bundle from principal G- and H-bundles over the same base."
---

Let $P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with projection $\pi_P$, and let $Q\to M$ be a principal $H$-bundle with projection $\pi_Q$, where $G,H$ are {{< knowl id="lie-group" text="Lie groups" >}}.

**Construction (fiber product).** Define the fiber product (also called the product over $M$)
\[
P\times_M Q := \{(p,q)\in P\times Q \mid \pi_P(p)=\pi_Q(q)\}.
\]
Because $\pi_P$ and $\pi_Q$ are submersions, $P\times_M Q$ is an embedded submanifold of $P\times Q$, and the map
\[
\pi: P\times_M Q \to M,\qquad \pi(p,q)=\pi_P(p)=\pi_Q(q)
\]
is a submersion. There is a right action of $G\times H$ given by
\[
(p,q)\cdot (g,h) := (pg,qh).
\]
With this action, $\pi:P\times_M Q\to M$ is a principal $(G\times H)$-bundle.

The canonical projections $P\times_M Q\to P$ and $P\times_M Q\to Q$ are principal bundle morphisms covering $\mathrm{id}_M$.

## Examples
1. If $P=M\times G$ and $Q=M\times H$ are trivial, then $P\times_M Q \cong M\times (G\times H)$ as principal $(G\times H)$-bundles.
2. If $P$ is the oriented orthonormal frame bundle of a Riemannian manifold and $Q$ is a principal circle bundle over the same base, then $P\times_M Q$ is a principal $(\mathrm{SO}(n)\times S^1)$-bundle encoding both structures simultaneously.
3. If $H=G$ and $Q=P$, then $P\times_M P$ is a principal $(G\times G)$-bundle; its quotient by the diagonal action of $G$ is canonically identified with the {{< knowl id="construction-adjoint-bundle-ad" text="adjoint bundle" >}} (as a bundle of groups) when $G$ acts by conjugation.
