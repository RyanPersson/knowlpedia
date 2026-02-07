---
title: "Smooth submersion"
description: "A smooth map whose differential is surjective at every point."
---

Let \(M\) and \(N\) be {{< knowl id="smooth-manifold" text="smooth manifolds" >}} of dimensions \(m\) and \(n\), and let \(f : M \to N\) be a {{< knowl id="smooth-map" text="smooth map" >}}.

The map \(f\) is a **smooth submersion** if for every \(p\in M\), the {{< knowl id="differential-pushforward-of-a-smooth-map" text="differential (pushforward)" >}}
\[
d f_p : T_p M \longrightarrow T_{f(p)}N
\]
is surjective, where \(T_pM\) is the {{< knowl id="tangent-space-at-a-point" text="tangent space" >}} at \(p\).

Equivalently, \(\operatorname{rank}(d f_p)=n\) for all \(p\in M\). In particular, if a submersion \(M^m \to N^n\) exists then \(m \ge n\).

## Local normal form (Submersion theorem)
If \(f : M^m \to N^n\) is a smooth submersion and \(p\in M\), then there exist smooth charts \((U,\varphi)\) around \(p\) and \((V,\psi)\) around \(f(p)\) (see {{< knowl id="smooth-chart-coordinate-chart" text="coordinate charts" >}}) such that, in these coordinates,
\[
(\psi\circ f \circ \varphi^{-1})(x^1,\dots,x^m)=(x^1,\dots,x^n)\in \mathbb{R}^n.
\]
So a submersion is locally just a projection map.

A useful viewpoint is that if \(f\) is a smooth submersion, then every \(y\in N\) is a {{< knowl id="regular-value" text="regular value" >}} of \(f\). Consequently, each {{< knowl id="fiber-of-a-map-preimage-fiber" text="fiber" >}} \(f^{-1}(y)\) is (locally) a smooth submanifold of codimension \(n\).

## Examples
1. **Projection from a product.** For smooth manifolds \(M\) and \(F\), the projection
   \[
   \pi_M : M\times F \to M,\qquad \pi_M(m,f)=m
   \]
   is a smooth submersion: its differential is surjective at every point. (This is the basic model for bundle projections, and its fibers are the slices \(\{m\}\times F\).)

2. **Coordinate projection.** The map \(\mathbb{R}^3\to \mathbb{R}^2\), \((x,y,z)\mapsto (x,y)\), is a smooth submersion since its Jacobian matrix has rank \(2\) everywhere.

3. **Determinant on \(GL(n,\mathbb{R})\).** The determinant map
   \[
   \det:GL(n,\mathbb{R}) \to \mathbb{R}\setminus\{0\}
   \]
   is a smooth submersion. At \(A\in GL(n,\mathbb{R})\), one has
   \[
   d(\det)_A(B)=\det(A)\,\mathrm{tr}(A^{-1}B),
   \]
   and since \(\det(A)\neq 0\) we can choose \(B\) so that \(d(\det)_A(B)\) is any prescribed real number, proving surjectivity.
