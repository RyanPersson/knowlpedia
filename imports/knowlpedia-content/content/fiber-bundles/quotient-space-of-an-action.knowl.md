+++
id = "fiber-bundles/quotient-space-of-an-action"
title = "Quotient space of an action (orbit space)"
kind = "knowl"
summary = "The topological space obtained by identifying points lying in the same orbit of a group action."
aliases = ["quotient-space-of-an-action", "Quotient space of an action (orbit space)"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/quotient-space-of-an-action.md"
+++

Let $G$ act on a manifold $M$.

The **quotient space of the action** (also called the **orbit space**) is the set of [[fiber-bundles/orbit-of-a-group-action|orbits]]
\[
M/G := \{\, G\cdot x \mid x\in M\,\},
\]
equipped with the **quotient topology** for the canonical surjection
\[
\pi:M\to M/G,\qquad \pi(x)=G\cdot x.
\]
Concretely, a subset $U\subseteq M/G$ is open if and only if $\pi^{-1}(U)$ is open in $M$.

In general $M/G$ need not be a manifold (it may fail to be Hausdorff or locally Euclidean). Under the stronger hypothesis of a [[fiber-bundles/principal-action|principal action]], the orbit space becomes a smooth manifold (see [[fiber-bundles/quotient-manifold|quotient manifold]]).

## Examples
1. **Rotations of the plane.** For $SO(2)\curvearrowright \mathbb{R}^2$, the quotient $\mathbb{R}^2/SO(2)$ is naturally homeomorphic to $[0,\infty)$ via the radius function.
2. **Translations by integers.** For the action of $\mathbb{Z}$ on $\mathbb{R}$ by translations, the quotient $\mathbb{R}/\mathbb{Z}$ is (homeomorphic to) the circle $S^1$.
3. **Conjugacy classes.** For the conjugation action of a Lie group on itself, $G/G$ is the set of conjugacy classes; for many noncompact groups this quotient is not Hausdorff.
