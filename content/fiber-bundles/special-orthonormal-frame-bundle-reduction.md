---
title: "Special orthonormal frame bundle"
description: "The principal SO(n)-bundle of oriented orthonormal frames for an oriented metric real rank-n bundle."
---

Let $\pi:E\to M$ be a real vector bundle of rank $n$ over a {{< knowl id="smooth-manifold" text="smooth manifold" >}}, equipped with a {{< knowl id="bundle-metric" text="bundle metric" >}} and an {{< knowl id="orientation-of-a-real-vector-bundle" text="orientation" >}}. The **special orthonormal frame bundle**, denoted $\mathrm{SO}(E)$, is the subbundle of the {{< knowl id="orthonormal-frame-bundle-reduction-of-the-frame-bundle" text="orthonormal frame bundle" >}} consisting of orthonormal frames that are oriented:
\[
\mathrm{SO}(E):=\{(e_1,\dots,e_n)\in \mathrm{O}(E)\ :\ (e_1,\dots,e_n)\ \text{is an oriented frame}\}.
\]

The right action of the group $\mathrm{O}(n)$ on $\mathrm{O}(E)$ restricts to a free right action of the special orthogonal group $\mathrm{SO}(n)$, which is a {{< knowl id="lie-group" text="Lie group" >}}. With this action, $\mathrm{SO}(E)\to M$ is a principal bundle with structure group $\mathrm{SO}(n)$.

Equivalently, $\mathrm{SO}(E)$ is the reduction of the full frame bundle to $\mathrm{SO}(n)$ determined jointly by the metric and the orientation.

## Examples
1. **Oriented Riemannian manifolds.** If $E=TM$ and $M$ is oriented and Riemannian, then $\mathrm{SO}(TM)$ is the usual bundle of oriented orthonormal tangent frames used in defining spin structures and Levi-Civita connections.

2. **Trivial oriented bundle.** For $E=M\times\mathbb R^n$ with the standard metric and the standard orientation, $\mathrm{SO}(E)\cong M\times \mathrm{SO}(n)$.

3. **Rank-one case.** If $n=1$, then $\mathrm{SO}(1)=\{1\}$, and $\mathrm{SO}(E)\to M$ is canonically isomorphic to $M$ whenever $E$ is oriented and metrized (there is a unique oriented unit vector in each fiber).
