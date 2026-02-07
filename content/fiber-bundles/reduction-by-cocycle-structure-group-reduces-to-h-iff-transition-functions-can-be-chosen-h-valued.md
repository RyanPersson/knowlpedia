---
title: "Theorem: Reduction by cocycle (H-reduction iff H-valued transition functions exist)"
description: "A principal G-bundle reduces to a subgroup H exactly when its transition functions can be chosen to land in H."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure {{< knowl id="lie-group" text="Lie group" >}} $G$, and let $H\subseteq G$ be a Lie subgroup.

## Theorem

The following are equivalent:

1. (**Existence of an $H$-reduction**) There exists a principal $H$-bundle $P_H\to M$ and an $H$-equivariant embedding $P_H\hookrightarrow P$ over $M$ such that $P$ is obtained from $P_H$ by extension of structure group along the inclusion $H\hookrightarrow G$.

2. (**$H$-valued transition functions**) There exists an open cover $\{U_i\}$ and local trivializations $P|_{U_i}\cong U_i\times G$ for which the transition functions $g_{ij}:U_{ij}\to G$ take values in $H$.

Moreover, if (2) holds, an explicit $H$-reduction is produced by
{{< knowl id="construction-reduction-of-structure-group-to-h-via-transition-functions-valued-in-h" text="gluing U_i×H with the same cocycle" >}}.

## Examples

1. **Orientation reduction.** The frame bundle of a rank-$n$ real vector bundle reduces from $\mathrm{GL}(n,\mathbb R)$ to $\mathrm{GL}^+(n,\mathbb R)$ exactly when one can choose transition maps with positive determinant, i.e. when the bundle is orientable.

2. **Metric reduction.** Choosing a fiber metric on a vector bundle allows transition functions between orthonormal frames to land in $\mathrm{O}(n)$, giving an $\mathrm{O}(n)$-reduction of the frame bundle.

3. **Unitary reduction.** A Hermitian structure on a complex rank-$n$ bundle yields transition maps valued in $U(n)$; equivalently, the $\mathrm{GL}(n,\mathbb C)$ frame bundle reduces to $U(n)$.
