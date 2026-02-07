---
title: "Bundle map"
description: "A morphism of fibered manifolds, i.e. a smooth map of total spaces compatible with the projections."
---

Let \(\pi:E\to M\) and \(\pi':E'\to M'\) be {{< knowl id="fibered-manifold" text="fibered manifolds" >}}. A **bundle map** (morphism of fibered manifolds) is a pair of smooth maps \((F,f)\) with \(F:E\to E'\) and \(f:M\to M'\) such that
\[
\pi'\circ F \;=\; f\circ \pi.
\]
Equivalently, \(F\) is a {{< knowl id="fiber-preserving-map" text="fiber-preserving map" >}} for which both projections are surjective submersions; when \(f\) is understood one says “\(F\) is a bundle map over \(f\)”.

Differentiating the commutative square gives, for each \(e\in E\),
\[
d\pi'_{F(e)}\circ dF_e \;=\; df_{\pi(e)}\circ d\pi_e.
\]
In particular, \(dF_e\) maps \(\ker(d\pi_e)\) into \(\ker(d\pi'_{F(e)})\), so it sends the {{< knowl id="vertical-tangent-space" text="vertical tangent space" >}} at \(e\) into the vertical tangent space at \(F(e)\). On the level of the {{< knowl id="tangent-bundle" text="tangent bundles" >}}, this says \(dF:TE\to TE'\) is compatible with the vertical subbundles.

## Examples
1. **Differential of a smooth map:** for a {{< knowl id="smooth-map" text="smooth map" >}} \(\varphi:M\to N\), the differential \(d\varphi:TM\to TN\) is a bundle map over \(\varphi\).
2. **Product-type maps:** if \(\pi=\mathrm{pr}_1:M\times F\to M\) and \(\pi'=\mathrm{pr}_1:M'\times F'\to M'\), then any map \((x,u)\mapsto(f(x),h(x,u))\) defines a bundle map over \(f\).
3. **Composition:** if \(F:E\to E'\) is over \(f\) and \(G:E'\to E''\) is over \(g\), then \(G\circ F\) is a bundle map over \(g\circ f\).
