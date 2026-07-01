+++
id = "fiber-bundles/cartans-second-structure-equation"
title = "Cartan's second structure equation (curvature) in the frame bundle"
kind = "knowl"
summary = "On the frame bundle, the curvature form is given by d omega plus one half the bracket of omega with itself."
aliases = ["cartans-second-structure-equation", "Cartan's second structure equation (curvature) in the frame bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/cartans-second-structure-equation.md"
+++

Let $M$ be an $n$-dimensional [[fiber-bundles/smooth-manifold|smooth manifold]] and let $\pi:F(M)\to M$ be its frame bundle, a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with structure group $G=\mathrm{GL}(n,\mathbb{R})$. Fix a [[fiber-bundles/principal-connection|principal connection]] $\omega\in\Omega^1(F(M);\mathfrak{gl}(n,\mathbb{R}))$, where $\mathfrak{gl}(n,\mathbb{R})$ is the [[lie-groups/lie-algebra|Lie algebra]] of $G$.

## Statement (frame bundle formulation)

The [[fiber-bundles/curvature|curvature]] of $\omega$ is the $\mathfrak{gl}(n,\mathbb{R})$-valued $2$-form $\Omega\in\Omega^2(F(M);\mathfrak{gl}(n,\mathbb{R}))$ defined by
\[
\Omega \;:=\; d\omega \;+\;\tfrac12[\omega\wedge\omega].
\]

This identity is **Cartan’s second structure equation**, where $d$ is the [[fiber-bundles/exterior-derivative|exterior derivative]] and the bracket wedge is defined by
\[
[\omega\wedge\omega](V,W)\;=\;[\omega(V),\omega(W)],
\]
using the [[fiber-bundles/lie-bracket|Lie bracket]] on $\mathfrak{gl}(n,\mathbb{R})$.

The form $\Omega$ is horizontal and $G$-equivariant. Under the usual correspondence between principal connections on $F(M)$ and linear connections on $TM$, $\Omega$ encodes the Riemann curvature tensor of the induced connection on the [[fiber-bundles/tangent-bundle|tangent bundle]].

## Examples

1. **Flat connection in a global frame.**
   If $M=\mathbb{R}^n$ with its standard frame and $\omega=0$, then $\Omega=0$ by the second structure equation.

2. **Constant sectional curvature model.**
   For the round sphere with its Levi-Civita connection, in a local orthonormal coframe one has curvature $2$-forms of the schematic shape
   \[
   \Omega^i{}_j = K\,\theta^i\wedge\theta^j,
   \]
   reflecting constant sectional curvature $K>0$.

3. **Product connections.**
   If $M=M_1\times M_2$ and the connection on $TM\cong TM_1\oplus TM_2$ is the product of connections on the factors, then $\Omega$ is block-diagonal with blocks given by the curvature forms from each factor, and there are no mixed curvature terms.
