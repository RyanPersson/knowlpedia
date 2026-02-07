---
title: "Peter–Weyl theorem"
description: "Finite-dimensional unitary representations of a compact Lie group span the regular representation."
---

Let $G$ be a {{< knowl id="compact-lie-group" text="compact Lie group" >}}.

## Theorem (Peter–Weyl)
Consider the left-regular representation of $G$ on $L^2(G)$ (with respect to Haar measure). Then:

1. (**Density of matrix coefficients**) The complex vector space spanned by matrix coefficients of finite-dimensional continuous unitary {{< knowl id="representation-of-a-lie-group" text="representations of $G$" >}} is dense in $C(G)$ in the uniform norm, and dense in $L^2(G)$ in the $L^2$-norm.

2. (**Hilbert space decomposition**) As a unitary representation,
$$
L^2(G)\ \cong\ \widehat{\bigoplus}_{\pi\in \widehat G}\ (\dim \pi)\, \pi,
$$

a Hilbert direct sum over the set $\widehat G$ of isomorphism classes of {{< knowl id="irreducible-representation-lie-group" text="irreducible representations" >}}, where each irreducible $\pi$ occurs with multiplicity $\dim \pi$.

3. (**Orthogonality**) Matrix coefficients of inequivalent irreducibles are orthogonal in $L^2(G)$, refining the {{< knowl id="schur-orthogonality-lie-groups" text="Schur orthogonality relations" >}}.

## Consequences
- Every finite-dimensional continuous representation of a compact Lie group is completely reducible (compare {{< knowl id="completely-reducible-representation-lie" text="complete reducibility" >}}).
- Harmonic analysis on $G$ reduces to the study of its irreducibles; for connected compact $G$, these are classified by highest weights (see {{< knowl id="highest-weight-theorem" text="the highest weight theorem" >}}).

## Context
Peter–Weyl is the nonabelian analogue of Fourier series on a torus: irreducible representations play the role of characters, and their matrix coefficients play the role of exponentials.
