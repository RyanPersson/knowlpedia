---
title: "Horizontal lift of a tangent vector"
description: "The unique horizontal vector at a point in the total space that projects to a given base tangent vector."
---

Let $\pi:E\to M$ be a surjective submersion equipped with an {{< knowl id="ehresmann-connection" text="Ehresmann connection" >}}, i.e. a splitting $TE=HE\oplus VE$ by a {{< knowl id="horizontal-subbundle" text="horizontal subbundle" >}} $HE$.

Fix $e\in E$ with $x=\pi(e)$. Since $d\pi_e$ restricts to an isomorphism $H_eE\to T_xM$, each base tangent vector has a unique horizontal representative.

**Definition.** For $v\in T_xM$, the horizontal lift of $v$ at $e$ is the unique vector $v^{\mathrm h}\in H_eE$ such that
\[
d\pi_e(v^{\mathrm h})=v.
\]
Equivalently, it is the value at $v$ of the inverse linear map $(d\pi_e|_{H_eE})^{-1}:T_xM\to H_eE\subset T_eE$.

## Examples
1. **Product bundle.** For $E=M\times F$ with product horizontals, the lift of $v\in T_xM$ at $(x,f)$ is $(v,0)\in T_xM\oplus T_fF$.
2. **Principal bundle viewpoint.** On a principal bundle with connection, the horizontal lift of $v\in T_xM$ at $p\in\pi^{-1}(x)$ is the unique $v^{\mathrm h}\in T_pP$ with $d\pi_p(v^{\mathrm h})=v$ and connection 1-form equal to zero on $v^{\mathrm h}$.
3. **Vector bundle with linear connection.** If $E\to M$ is a vector bundle with linear connection, the horizontal lift at a vector $e\in E_x$ encodes “moving $e$ along a base direction $v$ while keeping it parallel.”
