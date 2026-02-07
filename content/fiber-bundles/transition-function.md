---
title: "Transition function"
description: "The change-of-trivialization data on overlaps, encoding how local bundle charts glue."
---

Let \(\pi:E\to M\) be a smooth fiber bundle with typical fiber \(F\), and let \((U_i,\Phi_i)\) and \((U_j,\Phi_j)\) be {{< knowl id="local-trivialization" text="local trivializations" >}}. On the overlap \(U_{ij}=U_i\cap U_j\), the change of trivialization is the map
\[
\Phi_{ij}:=\Phi_i\circ \Phi_j^{-1}:U_{ij}\times F\longrightarrow U_{ij}\times F.
\]
It is a {{< knowl id="diffeomorphism" text="diffeomorphism" >}} over \(\mathrm{id}_{U_{ij}}\), so it necessarily has the form
\[
\Phi_{ij}(x,f)=(x,\,t_{ij}(x)(f)),
\]
where \(t_{ij}(x)\in \mathrm{Diff}(F)\). The map
\[
t_{ij}:U_{ij}\longrightarrow \mathrm{Diff}(F)
\]
is the **transition function** (or transition map) of the two trivializations. It is a {{< knowl id="smooth-map" text="smooth map" >}} when \(\mathrm{Diff}(F)\) is interpreted as “smoothly varying diffeomorphisms,” i.e. when the induced map \(U_{ij}\times F\to F\), \((x,f)\mapsto t_{ij}(x)(f)\), is smooth.

## Examples
1. **Möbius line bundle:** with two trivializations over overlapping arcs, the transition function is the constant map \(t_{12}\equiv(-1)\in \mathrm{GL}(1,\mathbb{R})\subset \mathrm{Diff}(\mathbb{R})\).
2. **Tangent bundle:** if \((U_i,x)\) and \((U_j,y)\) are overlapping coordinate charts, then \(t_{ij}(p)\) is given by the Jacobian matrix of the coordinate change \(y(x)\) at \(p\).
3. **Vector bundles:** in a {{< knowl id="vector-bundle" text="vector bundle" >}} of rank \(k\), transition functions take values in \(\mathrm{GL}(k,\mathbb{R})\) because trivializations are fiberwise linear.
