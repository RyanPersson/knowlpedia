+++
id = "differential-geometry/tangent-space"
title = "Tangent Space"
kind = "knowl"
summary = "The vector space of tangent vectors at a point, defined intrinsically using derivations or curves."
aliases = ["tangent-space", "Tangent Space"]
domains = ["differential-geometry"]
legacy_source_path = "differential-geometry/tangent-space.md"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]] and \(p\in M\). The **tangent space** at \(p\), denoted \(T_pM\), is a [[linear-algebra/vector-space|vector space]] capturing first-order directions through \(p\).

## Derivation definition
Let \(C^\infty_p(M)\) denote the germs of smooth real-valued functions near \(p\). A **tangent vector at \(p\)** is a linear map
$$
v: C^\infty_p(M)\to \mathbb{R}
$$
such that \(v\) satisfies the Leibniz rule
$$
v(fg)=v(f)\,g(p)+f(p)\,v(g).
$$
The set of all such derivations is \(T_pM\), with addition and scalar multiplication defined pointwise.

## Coordinate description
Given a chart \((U,x)\) with \(p\in U\) and \(x=(x^1,\dots,x^n)\), there are distinguished tangent vectors \(\left.\frac{\partial}{\partial x^i}\right|_p\) defined by
$$
\left.\frac{\partial}{\partial x^i}\right|_p(f)=\frac{\partial (f\circ x^{-1})}{\partial u^i}\Big|_{u=x(p)}.
$$
These form a [[algebra-modules/basis-module|basis]] of \(T_pM\), so \(\dim T_pM = \dim M\).

## Curve viewpoint
Equivalently, \(T_pM\) can be described using equivalence classes of smooth curves \(\gamma:(-\epsilon,\epsilon)\to M\) with \(\gamma(0)=p\), where \(\gamma_1\sim\gamma_2\) if they have the same first derivative in any (hence every) chart.

## Example
If \(M=\mathbb{R}^n\), then \(T_p\mathbb{R}^n\cong \mathbb{R}^n\) canonically, and derivations correspond to directional derivatives (see [[real-analysis/derivative|derivative]]).
