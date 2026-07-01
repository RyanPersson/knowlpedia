+++
id = "lie-groups/orthogonal-lie-algebra"
title = "Orthogonal Lie algebra"
kind = "knowl"
summary = "The Lie algebra of the orthogonal group: skew-symmetric endomorphisms (or their indefinite analogues)."
aliases = ["orthogonal-lie-algebra", "Orthogonal Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/orthogonal-lie-algebra.md"
+++

## Definition (Euclidean signature)
The **orthogonal Lie algebra** $\mathfrak{so}(n)$ is the Lie algebra of the [[lie-groups/orthogonal-group|orthogonal group]] $O(n)$. Concretely,
$$
\mathfrak{so}(n)=\{X\in \mathfrak{gl}(n,\Bbb R)\mid X^T+X=0\},
$$

with Lie bracket given by the commutator $[X,Y]=XY-YX$ (the [[fiber-bundles/lie-bracket|standard bracket]] on matrix Lie algebras). Here $\mathfrak{gl}(n,\Bbb R)$ is the [[lie-groups/general-linear-lie-algebra|general linear Lie algebra]].

A standard basis is given by $E_{ij}-E_{ji}$ for $1\le i<j\le n$, so
$$
\dim \mathfrak{so}(n)=\frac{n(n-1)}{2}.
$$

## Indefinite signature
If $\eta$ is a symmetric, invertible matrix of signature $(p,q)$, define
$$
\mathfrak{so}(p,q)=\{X\in \mathfrak{gl}(n,\Bbb R)\mid X^T\eta+\eta X=0\},
\quad n=p+q.
$$

This is the Lie algebra of $O(p,q)$. In particular, the Lie algebra of the [[lie-groups/lorentz-group|Lorentz group]] $O(1,n-1)$ is $\mathfrak{so}(1,n-1)$.

## Context
Orthogonal Lie algebras are basic examples of classical semisimple Lie algebras and play a central role in the classification via [[lie-groups/dynkin-diagram|Dynkin diagrams]] and root data.
