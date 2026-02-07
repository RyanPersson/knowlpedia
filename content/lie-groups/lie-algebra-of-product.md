---
title: "Lie algebra of a product"
description: "The Lie algebra of a product Lie group is the direct sum of the Lie algebras."
---

Let $G,H$ be {{< knowl id="lie-group" text="Lie groups" section="fiber-bundles">}}, and consider their {{< knowl id="product-lie-group" text="product Lie group" >}} $G\times H$.

## Theorem
There is a natural Lie algebra isomorphism
$$
\operatorname{Lie}(G\times H)\;\cong\; \operatorname{Lie}(G)\oplus \operatorname{Lie}(H),
$$
where the right-hand side is the {{< knowl id="direct-sum-of-lie-algebras" text="direct sum of Lie algebras" >}} with bracket
$$
[(X_1,Y_1),(X_2,Y_2)] = \bigl([X_1,X_2],[Y_1,Y_2]\bigr).
$$

## Construction (canonical identification)
Using the definition {{< knowl id="lie-algebra-of-a-lie-group" text="$\operatorname{Lie}(G)=T_eG$" >}}, we have
$$
T_{(e_G,e_H)}(G\times H)\cong T_{e_G}G \oplus T_{e_H}H.
$$

Under this identification, the Lie bracket on $\operatorname{Lie}(G\times H)$ (defined via brackets of left-invariant vector fields) becomes the componentwise bracket above.

## Example
For matrix groups, this is visible directly: if $G\subset \mathrm{GL}(n,\Bbb R)$ and $H\subset \mathrm{GL}(m,\Bbb R)$, then one model of $G\times H$ sits inside $\mathrm{GL}(n+m,\Bbb R)$ as block-diagonal matrices
$\mathrm{diag}(A,B)$. Differentiating at the identity shows
$$
\operatorname{Lie}(G\times H) = \left\{\begin{pmatrix} X & 0\\ 0 & Y\end{pmatrix} : X\in \operatorname{Lie}(G),\ Y\in \operatorname{Lie}(H)\right\}
\cong \operatorname{Lie}(G)\oplus \operatorname{Lie}(H),
$$
and commutators are computed blockwise.
