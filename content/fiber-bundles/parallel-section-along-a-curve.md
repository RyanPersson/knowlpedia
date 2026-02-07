---
title: "Parallel section along a curve"
description: "A section along a curve whose covariant derivative along the curve vanishes."
---

Let \( \pi:E\to M \) be a smooth vector bundle over a {{< knowl id="smooth-manifold" text="smooth manifold" >}} \(M\), equipped with a {{< knowl id="connection-on-a-vector-bundle" text="connection on a vector bundle" >}} \(\nabla\).

Let \(I\subset \mathbb{R}\) be an interval and \(\gamma:I\to M\) a smooth curve. A **section of \(E\) along \(\gamma\)** is a smooth map \(s:I\to E\) such that \(\pi\circ s=\gamma\). Using \(\nabla\), one defines the covariant derivative of \(s\) along \(\gamma\) by
\[
\frac{D s}{dt}(t) \coloneqq \nabla_{\dot\gamma(t)} \tilde s \big|_{\gamma(t)},
\]
where \(\tilde s\) is any smooth extension of \(s\) to a neighborhood of \(\gamma(t)\) in \(M\). This is well-defined (independent of the choice of extension) by the locality and \(C^\infty(M)\)-linearity properties of a connection.

A section \(s\) along \(\gamma\) is called **parallel along \(\gamma\)** if
\[
\frac{D s}{dt}(t)=0 \quad \text{for all } t\in I.
\]

Equivalently: given \(t_0\in I\) and \(v_0\in E_{\gamma(t_0)}\), there is a unique parallel section \(s\) along \(\gamma\) with \(s(t_0)=v_0\). The resulting identification of fibers is the {{< knowl id="parallel-transport" text="parallel transport" >}} determined by \(\nabla\) along \(\gamma\).

## Examples
1. **Trivial bundle over an interval.** Let \(E=I\times \mathbb{R}^n\to I\) with the standard (componentwise) connection. A section along the identity curve \(\gamma(t)=t\) is a map \(s(t)=(t,v(t))\). The parallel condition is \(v'(t)=0\), so parallel sections are exactly the constant vectors \(v(t)\equiv v_0\).

2. **Tangent bundle of Euclidean space.** Take \(E= T\mathbb{R}^m\) with the standard flat connection. Along any smooth curve \(\gamma\), a vector field \(V(t)\in T_{\gamma(t)}\mathbb{R}^m\cong \mathbb{R}^m\) is parallel iff its coordinate vector in \(\mathbb{R}^m\) is constant in \(t\).

3. **A rank-one connection written as an ODE.** On a trivial real line bundle \(E=M\times \mathbb{R}\), any connection can be written locally as \(\nabla=d+\alpha\) for a 1-form \(\alpha\) on \(M\). Along \(\gamma\), a section is a function \(f(t)\), and the parallel condition becomes
   \[
   f'(t) + \alpha(\dot\gamma(t))\,f(t)=0,
   \]
   so \(f(t)=f(t_0)\exp\!\left(-\int_{t_0}^t \alpha(\dot\gamma(\tau))\,d\tau\right)\).
