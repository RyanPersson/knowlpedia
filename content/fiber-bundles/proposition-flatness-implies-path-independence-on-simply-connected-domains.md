---
title: "Flatness implies path-independence on simply connected domains"
description: "On a simply connected region where the curvature vanishes, parallel transport depends only on the endpoints."
---

Let \(E\to M\) be a vector bundle with a {{< knowl id="connection-on-a-vector-bundle" text="connection on a vector bundle" >}} \(\nabla\), and let \(F_\nabla\) denote its {{< knowl id="curvature" text="curvature" >}}.

## Proposition (endpoint dependence on simply connected sets)
Let \(U\subset M\) be a connected, simply connected open set such that \(F_\nabla|_U=0\). Then for any two points \(x,y\in U\), the {{< knowl id="parallel-transport" text="parallel transport" >}} map
\[
\mathrm{PT}_\gamma : E_x \to E_y
\]
depends only on the endpoints \(x,y\), not on the choice of piecewise smooth path \(\gamma\) in \(U\) from \(x\) to \(y\).

Equivalently, if \(\gamma_0,\gamma_1\) are two such paths with the same endpoints, then \(\mathrm{PT}_{\gamma_0}=\mathrm{PT}_{\gamma_1}\).

A parallel statement holds for a principal bundle with a flat principal connection: on a simply connected \(U\) where curvature vanishes, the transport \(P_x\to P_y\) is independent of the path in \(U\).

## Examples
1. **Euclidean space.** On \(U=\mathbb R^n\) with the trivial bundle \(U\times V\) and \(\nabla=d\), curvature vanishes and parallel transport is the identity, hence depends only on endpoints.
2. **Restriction of a flat but globally nontrivial situation.** A flat connection on a bundle over \(S^1\) can have nontrivial holonomy around the circle, but on any simply connected arc \(U\subset S^1\) the proposition applies, so transport inside \(U\) is path-independent.
3. **Why simply connectedness matters.** On \(S^1\), take a flat \(U(1)\)-connection with holonomy \(e^{i\theta}\neq 1\). Curvature is still zero, but transport from a point to itself along the generator loop is multiplication by \(e^{i\theta}\), so dependence on the homotopy class of the path persists when the domain is not simply connected.
