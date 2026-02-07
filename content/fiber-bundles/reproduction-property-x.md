---
title: "Reproduction property"
description: "The connection form evaluates to the generating Lie algebra element on each fundamental vector field."
---

Let \(\pi:P\to M\) be a principal \(G\)-bundle and let \(\omega\in \Omega^1(P;\mathfrak{g})\) be a {{< knowl id="connection-1-form-on-a-principal-bundle" text="connection 1-form" >}}.

For \(X\in \mathfrak{g}\), the **fundamental vector field** \(X^\#\) is the {{< knowl id="vector-field" text="vector field" >}} on \(P\) defined by
\[
X^\#_p \coloneqq \left.\frac{d}{dt}\right|_{t=0} \bigl(p\cdot \exp(tX)\bigr).
\]

The **reproduction property** is the requirement that
\[
\omega(X^\#)=X \quad \text{for all } X\in \mathfrak{g}.
\]

This condition says that \(\omega\) restricts on each vertical space \(V_p=\ker(d\pi_p)\) to the canonical identification \(V_p\cong \mathfrak{g}\) coming from the infinitesimal right action.

## Examples
1. **Maurer–Cartan form on a Lie group.** For the principal bundle \(G\to \{\ast\}\) (right action by multiplication), the left Maurer–Cartan form \(\theta=g^{-1}dg\) satisfies \(\theta(X^\#)=X\) because \(g^{-1}\frac{d}{dt}(g\exp(tX))|_{0}=X\).

2. **Trivial bundle \(U\times G\).** With \(\omega=\mathrm{Ad}(g^{-1})A + g^{-1}dg\) as in a standard trivialization, a purely vertical vector at \((x,g)\) has the form \((0,(R_g)_*X)\), and one checks \(\omega(0,(R_g)_*X)=X\).

3. **The abelian case \(U(1)\).** Identify \(\mathfrak{u}(1)\cong i\mathbb{R}\). If \(\partial_\theta\) denotes the fundamental field for the standard \(U(1)\)-action, the reproduction property is \(\omega(\partial_\theta)=1\) (after the usual identification of \(i\mathbb{R}\) with \(\mathbb{R}\)).
