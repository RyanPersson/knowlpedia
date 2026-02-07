---
title: "Horizontal subbundle"
description: "A subbundle of the tangent bundle of a total space that complements the vertical tangent bundle."
---

Let $\pi:E\to M$ be a surjective submersion, and let
\[
VE:=\ker(d\pi)\subset TE
\]
be the vertical subbundle.

**Definition.** A horizontal subbundle is a smooth subbundle $HE\subset \,TE$ such that for every $e\in E$,
\[
T_eE = H_eE \oplus V_eE.
\]
Equivalently, $TE=HE\oplus VE$ as vector bundles over $E$.

A choice of horizontal subbundle is exactly the same data as an {{< knowl id="ehresmann-connection" text="Ehresmann connection" >}}. In particular, the restriction of $d\pi_e$ to $H_eE$ is an isomorphism $H_eE\cong T_{\pi(e)}M$, which is what makes the {{< knowl id="horizontal-lift-of-a-tangent-vector" text="horizontal lift of a tangent vector" >}} well-defined and unique.

## Examples
1. **Trivial bundle horizontals.** For $E=M\times F$, the choice $H_{(x,f)}E:=T_xM\oplus\{0\}$ is a horizontal subbundle complementary to $V_{(x,f)}E=\{0\}\oplus T_fF$.
2. **Horizontal subbundle on a principal bundle.** If $P\to M$ carries a principal connection, the horizontal subbundle is the kernel of the connection 1-form inside $TP$.
3. **Horizontal directions in a vector bundle.** Given a linear connection on a vector bundle $E\to M$, there is a canonical splitting of $TE$ into “vertical directions” (changing the vector in the fiber) and “horizontal directions” (moving in the base while keeping the vector parallel).
