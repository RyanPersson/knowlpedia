---
title: "Horizontal distribution"
description: "A smooth choice of horizontal tangent subspaces complementing the vertical spaces in a fiber bundle."
---

Let $\pi:E\to M$ be a surjective submersion. For each $e\in E$, write $V_eE=\ker(d\pi_e)\subset T_eE$.

**Definition.** A horizontal distribution is a smooth assignment
\[
e \longmapsto H_eE \subset T_eE
\]
of a constant-rank subspace such that for every $e\in E$,
\[
T_eE = H_eE \oplus V_eE.
\]
“Smooth” means that locally there exist smooth {{< knowl id="vector-field" text="vector fields" >}} on $E$ whose values span $H_eE$ at each point.

A horizontal distribution is the pointwise version of a {{< knowl id="horizontal-subbundle" text="horizontal subbundle" >}}; the two viewpoints are equivalent. The distribution is called integrable precisely when it is involutive, in the sense of {{< knowl id="integrable-horizontal-distribution" text="integrability of horizontals" >}}.

## Examples
1. **Constant horizontals on a product.** On $M\times F$, taking $H_{(x,f)}E=T_xM\oplus\{0\}$ defines a horizontal distribution.
2. **Transverse foliation.** If $E$ is foliated by submanifolds that project locally diffeomorphically onto $M$ (for example, graphs of local sections), then their tangent spaces define a horizontal distribution.
3. **From a connection.** Any Ehresmann connection (or principal connection) determines a horizontal distribution by declaring $H_eE$ to be the horizontal subspace at $e$.
