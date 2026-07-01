+++
id = "fiber-bundles/torsion-2-form"
title = "Torsion 2-form"
kind = "knowl"
summary = "The R^n-valued 2-form on a frame bundle that measures failure of a connection to be torsion-free."
aliases = ["torsion-2-form", "Torsion 2-form"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/torsion-2-form.md"
+++

Let $M$ be an $n$-dimensional [[fiber-bundles/smooth-manifold|smooth manifold]], let $FM\to M$ be its frame bundle, and let $\theta$ be the [[fiber-bundles/solder-form-on-the-frame-bundle|solder form]].

Fix a [[fiber-bundles/principal-connection|principal connection]] on $FM$, with connection 1-form $\omega$ valued in $\mathfrak{gl}(n,\mathbb{R})$.

## Definition (Torsion 2-form)
The **torsion 2-form** of $\omega$ is the $\mathbb{R}^n$-valued 2-form
\[
\Theta \in \Omega^2(FM;\mathbb{R}^n)
\]
defined by the (first) Cartan structure equation
\[
\Theta := d\theta + \omega \wedge \theta.
\]
Here $\omega\wedge\theta$ denotes the natural action of $\mathfrak{gl}(n,\mathbb{R})$ on $\mathbb{R}^n$ combined with the wedge product of differential forms.

This torsion form corresponds on the base to the torsion tensor of the induced connection $\nabla$ on $TM$:
\[
T(X,Y) := \nabla_XY - \nabla_YX - [X,Y],
\]
for [[fiber-bundles/vector-field|vector fields]] $X,Y$.

A connection is **torsion-free** if and only if $\Theta=0$ (equivalently, $T\equiv 0$). The Levi–Civita connection is characterized by torsion-free plus metric compatibility (see [[fiber-bundles/levicivita-connection-connection|Levi–Civita connection]]).

## Examples
1. **Levi–Civita.** For any Riemannian manifold, the torsion 2-form of the Levi–Civita connection vanishes identically.
2. **Left-invariant “zero” connection on a Lie group.** On a Lie group $G$ with a chosen left-invariant framing, declaring the frame to be parallel (so connection coefficients vanish in that frame) produces torsion equal to minus the bracket of left-invariant fields, hence typically nonzero.
3. **A coordinate connection with asymmetric Christoffel symbols.** On $\mathbb{R}^n$, defining a connection by $\nabla_{\partial_i}\partial_j = \Gamma^k_{ij}\partial_k$ with $\Gamma^k_{ij}\neq \Gamma^k_{ji}$ yields torsion components $T^k_{ij}=\Gamma^k_{ij}-\Gamma^k_{ji}$.
