---
title: "Induced covariant derivative on sections of an associated vector bundle"
description: "How a principal connection induces a covariant derivative on sections of an associated vector bundle."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure group $G$, and let $\rho:G\to \mathrm{GL}(V)$ be a {{< knowl id="representation-of-a-lie-group" text="representation of a Lie group" section="lie-groups">}} on a vector space $V$.

Form the {{< knowl id="associated-vector-bundle" text="associated vector bundle" >}} $E := P\times_G V$ (using the {{< knowl id="convention-associated-bundles-use-a-left-g-action-on-the-fiber-f" text="standard left action convention on the fiber" >}}).

Assume $P$ is equipped with a {{< knowl id="principal-connection" text="principal connection" >}} (equivalently, a {{< knowl id="connection-1-form-on-a-principal-bundle" text="connection 1-form" >}} $\omega$ on $P$). Let $H\subset TP$ denote the associated horizontal subbundle.

## Construction (horizontal differentiation)
A smooth section $s\in\Gamma(E)$ can be represented by a smooth **$\rho$-equivariant** map $f:P\to V$ satisfying
\[
f(p\cdot g)=\rho(g^{-1})\,f(p).
\]
Given a vector field $X$ on $M$ and a point $x\in M$, pick $p\in P_x$ and let $\widetilde{X}_p\in H_p$ be the {{< knowl id="horizontal-lift-of-a-tangent-vector" text="horizontal lift" >}} of $X_x$ at $p$. Define
\[
(\nabla_X s)(x) := [\,p,\; df_p(\widetilde{X}_p)\,]\in E_x.
\]

### Why this is well-defined
- If $p$ is replaced by $p\cdot g$, then $\widetilde{X}_{p\cdot g} = (dR_g)_p(\widetilde{X}_p)$ because the horizontal distribution is $G$-invariant.
- Using the equivariance $f(p\cdot g)=\rho(g^{-1})f(p)$ and differentiating along a horizontal direction shows that $df_{p\cdot g}(\widetilde{X}_{p\cdot g})$ represents the same element of the fiber quotient $P\times_G V$.

The operator $s\mapsto \nabla s$ is a {{< knowl id="connection-on-a-vector-bundle" text="connection on the vector bundle" >}} $E$, and it satisfies the Leibniz rule (see {{< knowl id="proposition-induced-connection-on-an-associated-vector-bundle-satisfies-the-leibniz-rule" text="the induced connection satisfies the Leibniz rule" >}}). In particular, this construction is the section-level version of {{< knowl id="construction-induced-connection-on-an-associated-bundle-using-horizontals" text="inducing connections on associated bundles using horizontals" >}}.

### Local formula
Choose a local section $s_0:U\to P$. Writing a section of $E$ as $s(x)=[s_0(x),v(x)]$ with $v:U\to V$, let
\[
A := s_0^*\omega \in \Omega^1(U;\mathfrak g)
\]
be the {{< knowl id="local-connection-1-form" text="local connection 1-form" >}}. Let $\rho_*:\mathfrak g\to \mathrm{End}(V)$ be the induced Lie algebra representation (obtained by differentiating $\rho$, as in {{< knowl id="differential-of-a-lie-group-homomorphism-lie-algebra-homomorphism" text="differentiating a Lie group map" >}}). Then locally,
\[
\nabla v = dv + \rho_*(A)\,v.
\]

## Examples
1. **Trivial bundle with a matrix-valued potential.** For $P=U\times G$ and $E=U\times V$, a choice of $A\in\Omega^1(U;\mathfrak g)$ produces
   \[
   \nabla = d + \rho_*(A).
   \]
   If $A=0$ this reduces to the ordinary derivative and corresponds to the {{< knowl id="flat-connection-a0-on-a-trivial-bundle" text="flat connection on a trivial bundle" >}}.

2. **Adjoint bundle.** Take $V=\mathfrak g$ with $\rho=\mathrm{Ad}$. Then $E$ is the {{< knowl id="adjoint-bundle-p-g-g-with-conjugation-action" text="adjoint bundle" >}} $\mathrm{Ad}(P)$. In a local trivialization with local connection form $A$, the induced covariant derivative on a section $\phi$ of $\mathrm{Ad}(P)$ has the familiar form
   \[
   \nabla \phi = d\phi + [A,\phi],
   \]
   which underlies the {{< knowl id="covariant-exterior-derivative-on-ad-valued-forms" text="covariant exterior derivative on adjoint-valued forms" >}}.

3. **Tangent bundle from the frame bundle.** Let $P=\mathrm{Fr}(TM)$ be the {{< knowl id="frame-bundle-fr-of-a-manifold-m" text="frame bundle of a manifold" >}} and let $V=\mathbb R^n$ with the standard representation of $\mathrm{GL}(n,\mathbb R)$. Then $TM\cong P\times_{\mathrm{GL}(n)}\mathbb R^n$, and a principal connection on $P$ induces the usual covariant derivative on vector fields. In the Riemannian case, choosing the orthonormal frame bundle and its connection recovers the {{< knowl id="levicivita-connection-connection" text="Levi-Civita connection" >}}.
