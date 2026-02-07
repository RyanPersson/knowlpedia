---
title: "Exterior covariant derivative"
description: "A differential operator on tensorial forms on a principal bundle obtained by differentiating and projecting to horizontal directions."
---

Fix a principal \(G\)-bundle \(\pi:P\to M\) with a {{< knowl id="principal-connection" text="principal connection" >}} and associated connection form \(\omega\). Let \(V\) be a representation of \(G\).

A \(V\)-valued \(k\)-form \(\alpha\in \Omega^k(P;V)\) is called **tensorial (of type \(V\))** if:
- (**Horizontality**) \(\alpha(X_1,\dots,X_k)=0\) whenever one of the \(X_i\) is vertical, and
- (**Equivariance**) \(R_g^*\alpha=\rho(g^{-1})\alpha\), where \(\rho:G\to \mathrm{GL}(V)\) is the representation.

Given such \(\alpha\), the **exterior covariant derivative** is the operator
\[
d_\omega:\Omega^k_{\mathrm{tens}}(P;V)\to \Omega^{k+1}_{\mathrm{tens}}(P;V)
\]
defined by
\[
(d_\omega \alpha)_p(X_0,\dots,X_k)\coloneqq (d\alpha)_p(X_0^H,\dots,X_k^H),
\]
where \(d\) is the {{< knowl id="exterior-derivative" text="exterior derivative" >}} and \(X_i^H\) denotes the horizontal projection of \(X_i\in T_pP\) using the connection (equivalently, the horizontal lift determined by \(\ker\omega\)).

This definition is independent of choices and produces another tensorial form. In local trivializations it becomes the familiar “\(d\) plus connection term” formula, and its square is governed by the curvature: for tensorial \(\alpha\),
\[
d_\omega^2\alpha \;\text{is the action of}\; \Omega \;\text{on}\; \alpha,
\]
where \(\Omega\) is the {{< knowl id="curvature-2-form-of-a-principal-connection" text="curvature 2-form" >}}.

## Examples
1. **Equivariant functions (degree 0).** If \(f:P\to V\) is equivariant, then \(d_\omega f\) is the horizontal part of \(df\). Under the associated bundle viewpoint, this corresponds to the covariant derivative of the section defined by \(f\).

2. **Adjoint-valued local formula.** For the adjoint representation \(V=\mathfrak{g}\), the descended operator on local \(\mathfrak{g}\)-valued forms is \(d_A=d+[A\wedge\cdot]\). This matches \(d_\omega\) applied to tensorial forms on \(P\).

3. **Bianchi identity as a covariant closure.** Applying \(d_\omega\) to the curvature \(\Omega\) yields \(d_\omega \Omega=0\), the (first) Bianchi identity in principal-bundle form.
