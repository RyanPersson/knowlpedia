---
title: "Special unitary frame bundle"
description: "The principal SU(n)-bundle obtained by restricting to unitary frames with determinant one."
---

Let $E\to M$ be a complex rank-$n$ vector bundle over a {{< knowl id="smooth-manifold" text="smooth manifold" >}} equipped with a {{< knowl id="hermitian-metric" text="Hermitian metric" >}}. Let $\mathrm{U}(E)$ be its unitary frame bundle. The **special unitary frame bundle** is, informally, the subbundle of $\mathrm{U}(E)$ consisting of unitary frames whose determinant is $1$.

To make this precise intrinsically, note that the top exterior power
\[
\det(E):=\Lambda^n E
\]
is a complex line bundle (see {{< knowl id="exterior-power-bundle" text="exterior power bundle" >}}), and the Hermitian metric on $E$ induces a Hermitian metric on $\det(E)$. A **special unitary reduction** of $(E,h)$ is any of the following equivalent pieces of data:

1. A principal subbundle $\mathrm{SU}(E)\subset \mathrm{U}(E)$ with structure group $\mathrm{SU}(n)$ (a {{< knowl id="lie-group" text="Lie group" >}}), such that the inclusion is $\mathrm{SU}(n)$-equivariant and fiberwise identifies $\mathrm{SU}(E)_x$ with the set of unitary bases of $E_x$ having determinant $1$.

2. A choice of nowhere-vanishing section $\Omega$ of $\det(E)$ with unit norm (with respect to the induced metric), i.e. a trivialization of $\det(E)$ compatible with the metric; in this case, $\mathrm{SU}(E)$ consists of unitary frames whose wedge $e_1\wedge\cdots\wedge e_n$ equals $\Omega$.

Thus, an $\mathrm{SU}(n)$-reduction exists if and only if $\det(E)$ is (unitarily) trivial.

## Examples
1. **Trivial bundle.** For $E=M\times\mathbb C^n$ with the standard Hermitian metric and the constant volume form $\Omega=\mathbf e_1\wedge\cdots\wedge \mathbf e_n$, one has $\mathrm{SU}(E)\cong M\times \mathrm{SU}(n)$.

2. **Rank one.** If $n=1$, then $\mathrm{SU}(1)=\{1\}$, and any Hermitian line bundle has $\mathrm{U}(E)$ as a principal $\mathrm{U}(1)$-bundle, while the special unitary frame bundle is canonically just the base manifold whenever a unit-norm trivialization of $E$ is chosen.

3. **Bundles with trivial determinant.** If $E$ is a complex rank-$n$ bundle with $\det(E)$ trivial (as a complex line bundle), then choosing a unit-norm trivializing section of $\det(E)$ produces an $\mathrm{SU}(n)$-reduction as above.
