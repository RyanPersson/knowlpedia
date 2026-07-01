+++
id = "fiber-bundles/levicivita-connection-connection"
title = "Levi–Civita connection as a principal O(n)-connection"
kind = "knowl"
summary = "The unique torsion-free metric-compatible connection on a Riemannian manifold, viewed on the orthonormal frame bundle."
aliases = ["levicivita-connection-connection", "Levi–Civita connection as a principal O(n)-connection"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/levicivita-connection-connection.md"
+++

Let $(M,g)$ be a Riemannian [[fiber-bundles/smooth-manifold|smooth manifold]] of dimension $n$. Denote by $O(M)\to M$ the orthonormal frame bundle, a principal $O(n)$-bundle.

## Theorem (Levi–Civita connection; principal-bundle formulation)
There exists a unique covariant derivative
\[
\nabla\colon \Gamma(TM)\times \Gamma(TM)\to \Gamma(TM)
\]
on the [[fiber-bundles/tangent-bundle|tangent bundle]] satisfying:

1. (**Metric compatibility**) $X\langle Y,Z\rangle = \langle \nabla_XY, Z\rangle + \langle Y,\nabla_XZ\rangle$ for all vector fields $X,Y,Z$.
2. (**Torsion-free**) $\nabla_XY-\nabla_YX = [X,Y]$, where $[\cdot,\cdot]$ is the [[fiber-bundles/lie-bracket|Lie bracket]] of [[fiber-bundles/vector-field|vector fields]].

This unique connection is the **Levi–Civita connection** of $g$.

Equivalently, there exists a unique [[fiber-bundles/principal-connection|principal connection]] on the principal bundle $O(M)\to M$ whose associated connection on $TM$ (via the defining representation of $O(n)$) is $\nabla$, and whose torsion 2-form (defined using the [[fiber-bundles/solder-form-on-the-frame-bundle|solder form]]) vanishes; this torsion is precisely the object defined in [[fiber-bundles/torsion-2-form|torsion 2-form]].

## Examples
1. **Euclidean space.** On $(\mathbb{R}^n,\text{standard }g)$, $\nabla$ is ordinary differentiation in standard coordinates; in the standard global orthonormal frame, the connection 1-form on $O(\mathbb{R}^n)$ is identically zero.
2. **Round sphere.** On $S^n$ with the round metric, $\nabla$ is the tangential component of the ambient derivative in $\mathbb{R}^{n+1}$; its holonomy is typically all of $SO(n)$ for $n\ge 2$.
3. **Bi-invariant metric on a Lie group.** If a Lie group carries a bi-invariant metric, then for left-invariant vector fields $X,Y$ one has $\nabla_XY=\tfrac12[X,Y]$.
