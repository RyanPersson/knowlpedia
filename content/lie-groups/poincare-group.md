---
title: "Poincaré group"
description: "The isometry group of Minkowski space: translations semidirect the Lorentz group."
---

Let $\Bbb R^{1,3}$ denote Minkowski space with its standard bilinear form of signature $(1,3)$.

The **Poincaré group** is the group of affine isometries of Minkowski space. Concretely, it is the semidirect product
$$
\mathrm{ISO}(1,3)=\Bbb R^{1,3}\rtimes O(1,3),
$$

where $O(1,3)$ is the {{< knowl id="lorentz-group" text="Lorentz group" >}} acting linearly on $\Bbb R^{1,3}$.

An element is a pair $(a,\Lambda)$ with $a\in \Bbb R^{1,3}$ (a translation) and $\Lambda\in O(1,3)$, with group law
$$
(a,\Lambda)\,(b,\Gamma)=(a+\Lambda b,\ \Lambda\Gamma).
$$

A standard matrix model realizes $\mathrm{ISO}(1,3)$ as block matrices of the form
$$
\begin{pmatrix}
\Lambda & a\\
0 & 1
\end{pmatrix},
\quad \Lambda\in O(1,3),\ a\in \Bbb R^{1,3},
$$
with multiplication matching the semidirect product rule.

## Lie algebra
Its Lie algebra is a semidirect sum
$$
\mathfrak{iso}(1,3)=\Bbb R^{1,3}\rtimes \mathfrak{so}(1,3),
$$

where $\mathfrak{so}(1,3)$ is the Lorentz Lie algebra (an instance of {{< knowl id="orthogonal-lie-algebra" text="orthogonal Lie algebras" >}}). Writing elements as pairs $(v,X)$ with $v\in \Bbb R^{1,3}$ and $X\in \mathfrak{so}(1,3)$, the bracket is
$$
[(v,X),(w,Y)] = (Xw-Yv,\ [X,Y]).
$$

## Action and orbits
The Poincaré group acts transitively on Minkowski space by affine transformations, so Minkowski space is a {{< knowl id="homogeneous-space" text="homogeneous space" >}} for $\mathrm{ISO}(1,3)$. Stabilizers and {{< knowl id="orbit-lie-group" text="orbits" >}} are central tools in representation theory and in the geometry of relativistic symmetries.
