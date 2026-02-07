---
title: "TFAE: Flat principal bundles (principal G-bundle with connection)"
description: "Equivalent conditions for a principal bundle connection to be flat, including vanishing curvature and homotopy-invariant parallel transport."
---

Let $M$ be a connected {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure group a {{< knowl id="lie-group" text="Lie group" >}} $G$. Fix a {{< knowl id="principal-connection" text="principal connection" >}} $\omega$ on $P$ with curvature form $\Omega$.

## Theorem (TFAE)

The following are equivalent:

1. **Zero curvature.**  
   $\Omega=0$ (equivalently, the {{< knowl id="curvature" text="curvature" >}} of $\omega$ vanishes identically).

2. **Local horizontal sections.**  
   Every point of $M$ has a neighborhood $U$ admitting a smooth local section $s:U\to P$ such that $s^*\omega=0$ (so $s$ is horizontal, and in that trivialization the connection $1$-form vanishes).

3. **Homotopy-invariant parallel transport.**  
   {{< knowl id="parallel-transport" text="Parallel transport" >}} along piecewise smooth curves depends only on the endpoint-fixed homotopy class of the curve. In particular, parallel transport around any contractible loop is the identity.

4. **Trivial restricted holonomy.**  
   The identity component of the {{< knowl id="holonomy-group" text="holonomy group" >}} is trivial: $\mathrm{Hol}^0_p(\omega)=\{e\}$ for (equivalently, for every) $p\in P$.

5. **Classification by monodromy representation (when $M$ is connected).**  
   Choosing a basepoint $x\in M$ and $p\in P_x$, there is a homomorphism (monodromy)
   \[
   \rho:\pi_1(M,x)\to G
   \]
   such that $(P,\omega)$ is isomorphic (as a bundle with connection) to the quotient of the universal cover $\widetilde M\times G$ by the diagonal action of $\pi_1(M,x)$ given by deck transformations on $\widetilde M$ and right multiplication via $\rho$.

## Examples

1. **Trivial bundle with the product (zero) connection.**  
   For $P=M\times G$ and the connection with horizontal distribution $TM\oplus\{0\}$, one has $\Omega=0$, parallel transport is constant in the $G$-factor, and holonomy is trivial.

2. **Flat bundles over the circle classified by a single element of $G$.**  
   Over $M=S^1$, any choice of $h\in G$ defines a flat bundle as the quotient $(\mathbb{R}\times G)/\mathbb{Z}$ where $1\in\mathbb{Z}$ acts by $(t,g)\mapsto(t+1,hg)$. The curvature vanishes, and the holonomy around the generator of $\pi_1(S^1)$ is exactly $h$.

3. **Representations of the torus or surface group.**  
   A homomorphism $\rho:\pi_1(T^2)\to G$ (or $\pi_1(\Sigma_g)\to G$ for a surface) produces a flat principal bundle via the quotient $\widetilde M\times_\rho G$. Distinct conjugacy classes of $\rho$ correspond to distinct flat bundles with connection up to isomorphism.
