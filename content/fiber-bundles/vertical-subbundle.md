---
title: "Vertical subbundle"
description: "The smooth subbundle of TE consisting of vectors tangent to the fibers of a surjective submersion."
---

Let \(\pi:E\to M\) be a {{< knowl id="fibered-manifold" text="fibered manifold" >}}. The differential of \(\pi\) defines a smooth vector bundle map between the {{< knowl id="tangent-bundle" text="tangent bundles" >}}
\[
d\pi:TE\longrightarrow TM,\qquad v\in T_eE\mapsto d\pi_e(v)\in T_{\pi(e)}M.
\]
The **vertical subbundle** of \(E\) is the kernel of this map:
\[
VE \;:=\; \ker(d\pi)\;=\;\{v\in TE\mid d\pi(v)=0\}\subset TE.
\]
Equivalently, \(VE\) is the smooth subbundle whose fiber at \(e\in E\) is the {{< knowl id="vertical-tangent-space" text="vertical tangent space" >}} \(V_eE\subset T_eE\).

Since \(\pi\) is a submersion, \(d\pi\) has constant rank, and therefore \(\ker(d\pi)\) has constant rank \(\dim(E)-\dim(M)\); this implies \(VE\) is a smooth vector subbundle of \(TE\). A {{< knowl id="vertical-vector-field" text="vertical vector field" >}} is exactly a smooth section of \(VE\).

## Examples
1. **Product projection:** for \(\pi=\mathrm{pr}_1:M\times F\to M\), the vertical subbundle is \(\{0\}\times TF\subset T(M\times F)\cong TM\times TF\).
2. **Tangent bundle:** for \(\tau:TM\to M\), the vertical subbundle \(V(TM)=\ker(d\tau)\subset T(TM)\) is the distribution tangent to the fibers \(T_xM\).
3. **Fibers as leaves:** for any fibered manifold, \(VE\) is tangent to each fiber \(E_x\); in fact \(VE|_{E_x}=TE_x\).
