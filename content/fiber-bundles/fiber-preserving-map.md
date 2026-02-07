---
title: "Fiber-preserving map"
description: "A smooth map between total spaces that sends fibers to fibers over a base map."
---

Let \(E,M,E',M'\) be {{< knowl id="smooth-manifold" text="smooth manifolds" >}} and let \(\pi:E\to M\) and \(\pi':E'\to M'\) be {{< knowl id="smooth-map" text="smooth maps" >}}. A smooth map \(F:E\to E'\) is **fiber-preserving** if there exists a smooth map \(f:M\to M'\) such that
\[
\pi'\circ F \;=\; f\circ \pi.
\]
In this situation one says that \(F\) **covers** \(f\), or that \(F\) is a map **over** \(f\). If \(\pi\) is surjective, then the base map \(f\) is uniquely determined by \(F\).

When \(\pi\) and \(\pi'\) are surjective submersions (i.e. when they define {{< knowl id="fibered-manifold" text="fibered manifolds" >}}), a fiber-preserving smooth map is the same structure as a {{< knowl id="bundle-map" text="bundle map" >}}. A basic example is the differential \(d\varphi:TM\to TN\) associated to a smooth map \(\varphi:M\to N\), which is fiber-preserving between the {{< knowl id="tangent-bundle" text="tangent bundles" >}} and covers \(\varphi\).

## Examples
1. **Maps between products:** given \(f:M\to M'\) and a smooth map \(g:M\times F\to F'\), the map \(F:M\times F\to M'\times F'\), \(F(x,u)=(f(x),g(x,u))\), is fiber-preserving over \(f\).
2. **Differential of a map:** for any \(\varphi:M\to N\), the differential \(d\varphi:TM\to TN\) satisfies \(\tau_N\circ d\varphi=\varphi\circ\tau_M\).
3. **Restriction to an open set:** for an open inclusion \(i:U\hookrightarrow M\), the inclusion \(\pi^{-1}(U)\hookrightarrow E\) is fiber-preserving over \(i\).
