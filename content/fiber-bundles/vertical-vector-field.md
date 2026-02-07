---
title: "Vertical vector field"
description: "A vector field on the total space of a fibered manifold that is tangent to every fiber."
---

Let \(\pi:E\to M\) be a {{< knowl id="fibered-manifold" text="fibered manifold" >}}. A {{< knowl id="vector-field" text="vector field" >}} \(X\) on \(E\) is **vertical** if for every \(e\in E\),
\[
X_e\in V_eE\quad\text{equivalently}\quad d\pi_e(X_e)=0,
\]
where \(V_eE\) is the {{< knowl id="vertical-tangent-space" text="vertical tangent space" >}} at \(e\).

Equivalently, \(X\) is a smooth section of the {{< knowl id="vertical-subbundle" text="vertical subbundle" >}} \(VE\subset TE\). Any integral curve of a vertical vector field lies entirely inside a single fiber \(E_x\). Consequently, wherever the local flow of \(X\) is defined, it yields fiberwise local {{< knowl id="diffeomorphism" text="diffeomorphisms" >}} of \(E\) covering \(\mathrm{id}_M\); in particular, each time-\(t\) map is a {{< knowl id="fiber-preserving-map" text="fiber-preserving map" >}} over \(\mathrm{id}_M\).

## Examples
1. **Product projection:** on \(M\times F\to M\), any field of the form \(X_{(x,f)}=(0,Y_{(x,f)})\) (no component along \(M\)) is vertical; for instance \(X(x,f)=(0,Y_f)\) for a fixed vector field \(Y\) on \(F\).
2. **Principal bundles:** on a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} \(P\to M\), each \(\xi\) in the {{< knowl id="lie-algebra" text="Lie algebra" section="lie-groups">}} \(\mathfrak g\) defines a vertical fundamental vector field \(\xi_P\) generating the right \(G\)-action.
3. **Vector bundles:** on a {{< knowl id="vector-bundle" text="vector bundle" >}} \(E\to M\), the Euler (radial) vector field that differentiates fiberwise scalar multiplication \(t\cdot e\) is vertical.
