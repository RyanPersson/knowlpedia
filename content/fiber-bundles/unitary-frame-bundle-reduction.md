---
title: "Unitary frame bundle"
description: "The principal U(n)-bundle of unitary frames determined by a Hermitian metric on a complex rank-n bundle."
---

Let $\pi:E\to M$ be a complex vector bundle of rank $n$ over a {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let $h$ be a {{< knowl id="hermitian-metric" text="Hermitian metric" >}} on $E$. The **unitary frame bundle** of $(E,h)$, denoted $\mathrm{U}(E)$, is the submanifold of the (complex) frame bundle $\mathrm{Fr}(E)$ consisting of frames that are unitary with respect to $h$:
\[
\mathrm{U}(E):=\{(e_1,\dots,e_n)\in \mathrm{Fr}(E)\ :\ h(e_i,e_j)=\delta_{ij}\ \text{fiberwise}\}.
\]

The right action of $\mathrm{GL}(n,\mathbb C)$ on $\mathrm{Fr}(E)$ restricts to a free right action of the unitary group $\mathrm{U}(n)$ on $\mathrm{U}(E)$. With this action, $\mathrm{U}(E)\to M$ is a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure group $\mathrm{U}(n)$.

Equivalently, giving a Hermitian metric on $E$ is the same as specifying a reduction of the structure group from $\mathrm{GL}(n,\mathbb C)$ to $\mathrm{U}(n)$.

## Examples
1. **Trivial bundle.** For $E=M\times\mathbb C^n$ with the standard Hermitian form, $\mathrm{U}(E)\cong M\times \mathrm{U}(n)$.

2. **Complexified real bundle with metric.** If $E_\mathbb R$ is a real rank-$n$ bundle with a bundle metric, then its complexification inherits a Hermitian metric, and the corresponding unitary frame bundle can be described as the complexification of the orthonormal frames.

3. **Unitary frames for a complex tangent bundle.** If a manifold carries additional structure making $TM$ into a complex rank-$n$ bundle with a Hermitian metric (e.g. in almost Hermitian geometry), then $\mathrm{U}(TM)$ is the unitary frame bundle used to define canonical connections.
