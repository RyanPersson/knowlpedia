---
title: "Parallel transport respects concatenation of paths"
description: "Parallel transport along a concatenated path equals the composition of parallel transports along the two pieces."
---

Let \(E\to M\) be a vector bundle equipped with a {{< knowl id="connection-on-a-vector-bundle" text="connection on a vector bundle" >}} \(\nabla\). For a piecewise smooth path \(\gamma:[0,1]\to M\), write
\[
\mathrm{PT}_\gamma : E_{\gamma(0)}\to E_{\gamma(1)}
\]
for the {{< knowl id="parallel-transport" text="parallel transport" >}} map determined by \(\nabla\).

## Proposition (compatibility with concatenation)
Let \(\gamma_1:[0,1]\to M\) and \(\gamma_2:[0,1]\to M\) be piecewise smooth with \(\gamma_1(1)=\gamma_2(0)\). Let \(\gamma_2\ast \gamma_1\) denote their concatenation (first traverse \(\gamma_1\), then \(\gamma_2\)). Then
\[
\mathrm{PT}_{\gamma_2\ast \gamma_1} \;=\; \mathrm{PT}_{\gamma_2}\circ \mathrm{PT}_{\gamma_1}.
\]
Equivalently, if \(s(t)\) is a \(\nabla\)-parallel section along \(\gamma_2\ast\gamma_1\) with initial value \(s(0)=v\in E_{\gamma_1(0)}\), then the value at the intermediate point is \(s(1/2)=\mathrm{PT}_{\gamma_1}(v)\) (after reparametrization), and the final value is obtained by transporting further along \(\gamma_2\).

The same statement holds for parallel transport in a principal \(G\)-bundle with a principal connection: transport along a concatenated path is the composition of the two transport maps between fibers.

## Examples
1. **Trivial connection on \(M\times V\).** If \(\nabla=d\), then \(\mathrm{PT}_\gamma\) is the identity on \(V\) for every \(\gamma\), so the concatenation identity holds tautologically.
2. **Piecewise geodesic transport.** On a Riemannian manifold with its Levi–Civita connection, transporting a tangent vector along a broken geodesic is the same as transporting along the first segment and then along the second; the proposition encodes this “do it in steps” rule.
3. **Holonomy as a product.** For a loop written as a concatenation of subloops, the resulting holonomy element is the product of the holonomies of the pieces (with the same order as the concatenation).
