---
title: "Fibered manifold"
description: "A smooth manifold E equipped with a surjective submersion onto a base manifold M."
---

Let \(E\) and \(M\) be {{< knowl id="smooth-manifold" text="smooth manifolds" >}} and let \(\pi:E\to M\) be a {{< knowl id="smooth-map" text="smooth map" >}}. The triple \((E,\pi,M)\) is called a **fibered manifold** if \(\pi\) is a **surjective submersion**, i.e. \(\pi\) is surjective and for every \(e\in E\) the differential
\[
d\pi_e:T_eE\longrightarrow T_{\pi(e)}M
\]
is surjective.

For each \(x\in M\), the **fiber** over \(x\) is \(E_x:=\pi^{-1}(x)\). By the submersion theorem, each fiber \(E_x\) is an embedded submanifold of \(E\) of dimension \(\dim E-\dim M\), and the inclusion \(E_x\hookrightarrow E\) identifies
\[
T_eE_x=\ker(d\pi_e).
\]
This kernel is the {{< knowl id="vertical-tangent-space" text="vertical tangent space" >}} at \(e\).

Equivalently, \(\pi\) induces a fiberwise surjective bundle map \(d\pi:TE\to TM\) between the {{< knowl id="tangent-bundle" text="tangent bundles" >}}. A {{< knowl id="smooth-fiber-bundle" text="smooth fiber bundle" >}} is a fibered manifold equipped with local product charts; {{< knowl id="vector-bundle" text="vector bundles" >}} and {{< knowl id="principal-g-bundle" text="principal G-bundles" >}} are standard examples.

## Examples
1. **Product projection:** for any manifolds \(M\) and \(F\), the map \(\mathrm{pr}_1:M\times F\to M\) is a surjective submersion, hence a fibered manifold.
2. **Tangent bundle:** the projection \(\tau:TM\to M\) is a surjective submersion.
3. **Any smooth fiber bundle:** if \(\pi:E\to M\) is a smooth fiber bundle, then \((E,\pi,M)\) is automatically a fibered manifold.
