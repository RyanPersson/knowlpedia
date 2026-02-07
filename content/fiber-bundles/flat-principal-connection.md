---
title: "Flat principal connection"
description: "A principal connection whose curvature 2-form vanishes identically."
---

Let \(\pi:P\to M\) be a principal \(G\)-bundle equipped with a {{< knowl id="principal-connection" text="principal connection" >}} and curvature \(\Omega\in \Omega^2(P;\mathfrak{g})\).

The connection is called **flat** if its {{< knowl id="curvature-2-form-of-a-principal-connection" text="curvature 2-form" >}} vanishes:
\[
\Omega = 0.
\]
Equivalently, in any local trivialization with local connection form \(A\), the local curvature satisfies \(F=dA+\tfrac12[A\wedge A]=0\).

A flat connection has the key consequence that {{< knowl id="parallel-transport" text="parallel transport" >}} along a curve depends only on the homotopy class of the curve (with endpoints fixed). In particular, parallel transport around loops yields the {{< knowl id="holonomy-representation" text="holonomy representation" >}} of \(\pi_1(M)\) into \(G\), and the associated {{< knowl id="holonomy-group" text="holonomy group" >}} is determined by the image of that representation.

## Examples
1. **Product connection on a trivial bundle.** On \(P=M\times G\), take the connection defined by \(\omega=g^{-1}dg\) (equivalently \(A=0\) in the canonical trivialization). Then \(\Omega=0\), so the connection is flat and parallel transport leaves the \(G\)-coordinate unchanged.

2. **Flat bundle from a representation.** Given a representation \(\rho:\pi_1(M)\to G\), the quotient \(P=(\widetilde M\times G)/\pi_1(M)\) (with \(\gamma\in\pi_1\) acting by deck transformations on \(\widetilde M\) and by right multiplication through \(\rho(\gamma)^{-1}\) on \(G\)) carries a natural flat connection descended from the product connection on \(\widetilde M\times G\).

3. **Constant commuting gauge field on a torus.** On \(T^n\) with a trivial \(G\)-bundle, a connection form \(A=\sum_i A_i\,d\theta^i\) with constant \(A_i\in\mathfrak{g}\) is flat provided \([A_i,A_j]=0\) for all \(i,j\) (so both \(dA=0\) and \([A\wedge A]=0\)).
