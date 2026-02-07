---
title: "Vertical tangent space"
description: "The subspace of a tangent space consisting of vectors tangent to a fiber of a surjective submersion."
---

Let \(\pi:E\to M\) be a {{< knowl id="fibered-manifold" text="fibered manifold" >}} and let \(e\in E\) with \(x=\pi(e)\). The **vertical tangent space** at \(e\) is
\[
V_eE \;:=\; \ker(d\pi_e)\subset T_eE.
\]
Equivalently, viewing \(d\pi\) as a smooth bundle map \(d\pi:TE\to TM\) between the {{< knowl id="tangent-bundle" text="tangent bundle" >}}s, \(V_eE\) is the kernel of \(d\pi\) on the fiber over \(e\).

By the submersion theorem, the fiber \(E_x=\pi^{-1}(x)\) is an embedded submanifold of \(E\), and
\[
T_e(E_x)=V_eE.
\]
In particular, \(\dim(V_eE)=\dim(E)-\dim(M)\), so the vertical tangent space has constant dimension along each connected component of \(E\). As \(e\) varies, the spaces \(V_eE\) assemble into the {{< knowl id="vertical-subbundle" text="vertical subbundle" >}} \(VE\subset TE\).

## Examples
1. **Product projection:** for \(\pi=\mathrm{pr}_1:M\times F\to M\), one has \(V_{(x,f)}(M\times F)\cong \{0\}\times T_fF\).
2. **Tangent bundle:** for \(\tau:TM\to M\) and \(v\in T_xM\), the vertical space \(V_v(TM)=\ker(d\tau_v)\) is canonically identified with \(T_xM\) (it is the tangent space to the fiber \(T_xM\) at \(v\)).
3. **Principal bundle:** if \(\pi:P\to M\) is a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure group \(G\) and {{< knowl id="lie-algebra" text="Lie algebra" section="lie-groups">}} \(\mathfrak g\), then \(V_pP\) is the tangent space to the orbit \(p\cdot G\), and the fundamental vector field construction gives a linear isomorphism \(\mathfrak g\cong V_pP\).
