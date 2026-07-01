+++
id = "lie-groups/schur-orthogonality-lie-groups"
title = "Schur orthogonality for compact Lie groups"
kind = "knowl"
summary = "Matrix coefficients of distinct irreducible unitary representations are orthogonal in L²(G), with a sharp normalization."
aliases = ["schur-orthogonality-lie-groups", "Schur orthogonality for compact Lie groups"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/schur-orthogonality-lie-groups.md"
+++

Let $G$ be a [[lie-groups/compact-lie-group|compact Lie group]]. Fix the normalized Haar measure $dg$ on $G$ (so $\int_G 1\,dg=1$). Let $(\pi,V)$ and $(\sigma,W)$ be finite-dimensional continuous unitary representations of $G$ (see [[lie-groups/representation-of-a-lie-group|representation of a Lie group]]), with $\pi,\sigma$ irreducible (see [[lie-groups/irreducible-representation-lie-group|irreducible representation]]). Choose orthonormal bases so that $\pi(g)$ and $\sigma(g)$ have matrix entries $\pi_{ij}(g)$ and $\sigma_{kl}(g)$.

**Schur orthogonality** asserts:
\[
\int_G \pi_{ij}(g)\,\overline{\sigma_{kl}(g)}\,dg
\;=\;
\begin{cases}
\frac{1}{\dim V}\,\delta_{ik}\delta_{jl}, & \text{if }\pi\simeq \sigma,\\[6pt]
0, & \text{if }\pi\not\simeq \sigma.
\end{cases}
\]
Equivalently, the matrix coefficients of irreducible unitary representations form an orthogonal family in $L^2(G)$, and within a fixed irreducible representation they are orthogonal with the explicit scale factor $1/\dim V$.

This is the analytic avatar of Schur’s lemma and is one of the key inputs in the [[lie-groups/peter-weyl-theorem|Peter–Weyl theorem]], which decomposes $L^2(G)$ into finite-dimensional isotypic pieces. In practice, Schur orthogonality is the tool that turns representation theory into concrete integral identities on compact groups (compare also [[lie-groups/completely-reducible-representation-lie|complete reducibility]]).
