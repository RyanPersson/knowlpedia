+++
id = "fiber-bundles/smooth-immersion"
title = "Smooth immersion"
kind = "knowl"
summary = "A smooth map whose differential is injective at every point."
aliases = ["smooth-immersion", "Smooth immersion"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/smooth-immersion.md"
+++

Let \(M\) and \(N\) be [[fiber-bundles/smooth-manifold|smooth manifolds]] of dimensions \(m\) and \(n\), and let \(f : M \to N\) be a [[fiber-bundles/smooth-map|smooth map]].

The map \(f\) is a **smooth immersion** if for every \(p \in M\), the [[fiber-bundles/differential-pushforward-of-a-smooth-map|differential (pushforward)]]
\[
d f_p : T_p M \longrightarrow T_{f(p)}N
\]
is injective, where \(T_p M\) denotes the [[fiber-bundles/tangent-space-at-a-point|tangent space at \(p\)]].

Equivalently, \(\operatorname{rank}(d f_p)=m\) for all \(p\in M\). In particular, if an immersion \(M^m \to N^n\) exists then \(m \le n\).

## Local normal form (Immersion theorem)
If \(f : M^m \to N^n\) is a smooth immersion and \(p\in M\), then there exist smooth charts \((U,\varphi)\) about \(p\) and \((V,\psi)\) about \(f(p)\) (see [[fiber-bundles/smooth-chart-coordinate-chart|coordinate charts]]) such that, in coordinates, \(f\) becomes the standard inclusion:
\[
(\psi\circ f \circ \varphi^{-1})(x^1,\dots,x^m)=(x^1,\dots,x^m,0,\dots,0)\in \mathbb{R}^n.
\]
Thus an immersion is locally an embedding into \(N\), but globally it need not be injective. When an immersion is also a homeomorphism onto its image (with the subspace topology), it is a [[fiber-bundles/smooth-embedding|smooth embedding]]. A [[fiber-bundles/diffeomorphism|diffeomorphism]] is in particular both a smooth immersion and a [[fiber-bundles/smooth-submersion|smooth submersion]].

## Examples
1. **Linear inclusion.** The map \(i:\mathbb{R}^m \to \mathbb{R}^n\) for \(m\le n\) defined by
   \[
   i(x^1,\dots,x^m)=(x^1,\dots,x^m,0,\dots,0)
   \]
   is a smooth immersion: for every point, the differential is the injective inclusion \(\mathbb{R}^m \hookrightarrow \mathbb{R}^n\).

2. **Standard circle in the plane.** The map \(f:\mathbb{R}\to \mathbb{R}^2\) given by
   \[
   f(t)=(\cos t,\sin t)
   \]
   is a smooth immersion since \(f'(t)=(-\sin t,\cos t)\neq 0\) for all \(t\). It is not injective as a map \(\mathbb{R}\to\mathbb{R}^2\), but it factors through the quotient \(\mathbb{R}\to S^1\) to give an embedding \(S^1\hookrightarrow \mathbb{R}^2\).

3. **An immersion with self-intersections.** The “figure-eight” map \(g:S^1\to \mathbb{R}^2\) defined (using an angle parameter \(t\)) by
   \[
   g(t)=(\sin t,\sin 2t)
   \]
   is a smooth immersion: \(g'(t)=(\cos t,2\cos 2t)\) never vanishes. However, \(g(0)=g(\pi)=(0,0)\), so it is not a [[fiber-bundles/smooth-embedding|smooth embedding]].
