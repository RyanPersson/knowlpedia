+++
id = "fiber-bundles/construction-induced-covariant-derivative-on-associated-vector-bundle-sections"
title = "Induced covariant derivative on sections of an associated vector bundle"
kind = "knowl"
summary = "How a principal connection induces a covariant derivative on sections of an associated vector bundle."
aliases = ["construction-induced-covariant-derivative-on-associated-vector-bundle-sections", "Induced covariant derivative on sections of an associated vector bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/construction-induced-covariant-derivative-on-associated-vector-bundle-sections.md"
+++

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with structure group $G$, and let $\rho:G\to \mathrm{GL}(V)$ be a [[lie-groups/representation-of-a-lie-group|representation of a Lie group]] on a vector space $V$.

Form the [[fiber-bundles/associated-vector-bundle|associated vector bundle]] $E := P\times_G V$ (using the [[fiber-bundles/convention-associated-bundles-use-a-left-g-action-on-the-fiber-f|standard left action convention on the fiber]]).

Assume $P$ is equipped with a [[fiber-bundles/principal-connection|principal connection]] (equivalently, a [[fiber-bundles/connection-1-form-on-a-principal-bundle|connection 1-form]] $\omega$ on $P$). Let $H\subset TP$ denote the associated horizontal subbundle.

## Construction (horizontal differentiation)
A smooth section $s\in\Gamma(E)$ can be represented by a smooth **$\rho$-equivariant** map $f:P\to V$ satisfying
\[
f(p\cdot g)=\rho(g^{-1})\,f(p).
\]
Given a vector field $X$ on $M$ and a point $x\in M$, pick $p\in P_x$ and let $\widetilde{X}_p\in H_p$ be the [[fiber-bundles/horizontal-lift-of-a-tangent-vector|horizontal lift]] of $X_x$ at $p$. Define
\[
(\nabla_X s)(x) := [\,p,\; df_p(\widetilde{X}_p)\,]\in E_x.
\]

### Why this is well-defined
- If $p$ is replaced by $p\cdot g$, then $\widetilde{X}_{p\cdot g} = (dR_g)_p(\widetilde{X}_p)$ because the horizontal distribution is $G$-invariant.
- Using the equivariance $f(p\cdot g)=\rho(g^{-1})f(p)$ and differentiating along a horizontal direction shows that $df_{p\cdot g}(\widetilde{X}_{p\cdot g})$ represents the same element of the fiber quotient $P\times_G V$.

The operator $s\mapsto \nabla s$ is a [[fiber-bundles/connection-on-a-vector-bundle|connection on the vector bundle]] $E$, and it satisfies the Leibniz rule (see [[fiber-bundles/proposition-induced-connection-on-an-associated-vector-bundle-satisfies-the-leibniz-rule|the induced connection satisfies the Leibniz rule]]). In particular, this construction is the section-level version of [[fiber-bundles/construction-induced-connection-on-an-associated-bundle-using-horizontals|inducing connections on associated bundles using horizontals]].

### Local formula
Choose a local section $s_0:U\to P$. Writing a section of $E$ as $s(x)=[s_0(x),v(x)]$ with $v:U\to V$, let
\[
A := s_0^*\omega \in \Omega^1(U;\mathfrak g)
\]
be the [[fiber-bundles/local-connection-1-form|local connection 1-form]]. Let $\rho_*:\mathfrak g\to \mathrm{End}(V)$ be the induced Lie algebra representation (obtained by differentiating $\rho$, as in [[fiber-bundles/differential-of-a-lie-group-homomorphism-lie-algebra-homomorphism|differentiating a Lie group map]]). Then locally,
\[
\nabla v = dv + \rho_*(A)\,v.
\]

## Examples
1. **Trivial bundle with a matrix-valued potential.** For $P=U\times G$ and $E=U\times V$, a choice of $A\in\Omega^1(U;\mathfrak g)$ produces
   \[
   \nabla = d + \rho_*(A).
   \]
   If $A=0$ this reduces to the ordinary derivative and corresponds to the [[fiber-bundles/flat-connection-a0-on-a-trivial-bundle|flat connection on a trivial bundle]].

2. **Adjoint bundle.** Take $V=\mathfrak g$ with $\rho=\mathrm{Ad}$. Then $E$ is the [[fiber-bundles/adjoint-bundle-p-g-g-with-conjugation-action|adjoint bundle]] $\mathrm{Ad}(P)$. In a local trivialization with local connection form $A$, the induced covariant derivative on a section $\phi$ of $\mathrm{Ad}(P)$ has the familiar form
   \[
   \nabla \phi = d\phi + [A,\phi],
   \]
   which underlies the [[fiber-bundles/covariant-exterior-derivative-on-ad-valued-forms|covariant exterior derivative on adjoint-valued forms]].

3. **Tangent bundle from the frame bundle.** Let $P=\mathrm{Fr}(TM)$ be the [[fiber-bundles/frame-bundle-fr-of-a-manifold-m|frame bundle of a manifold]] and let $V=\mathbb R^n$ with the standard representation of $\mathrm{GL}(n,\mathbb R)$. Then $TM\cong P\times_{\mathrm{GL}(n)}\mathbb R^n$, and a principal connection on $P$ induces the usual covariant derivative on vector fields. In the Riemannian case, choosing the orthonormal frame bundle and its connection recovers the [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]].
