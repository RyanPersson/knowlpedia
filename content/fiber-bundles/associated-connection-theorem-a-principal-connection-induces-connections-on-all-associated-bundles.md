---
title: "Associated connection theorem"
description: "A principal connection induces a compatible connection on every associated bundle and every associated vector bundle."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure group $G$, and let $\omega$ be a {{< knowl id="principal-connection" text="principal connection" >}} on $P$ (equivalently a horizontal distribution; see {{< knowl id="horizontal-distribution" text="horizontal distribution" >}} and {{< knowl id="connection-1-form-on-a-principal-bundle" text="connection 1-form" >}}).

Let $F$ be a smooth left $G$-space (see {{< knowl id="smooth-action-of-a-lie-group-on-a-manifold" text="smooth G-action" >}}) and form the {{< knowl id="associated-bundle" text="associated bundle" >}}
\[
E := P\times_G F,
\]
as in {{< knowl id="construction-associated-bundle-p-g-f-from-a-left-g-space-f" text="the standard associated bundle construction" >}}.

## Theorem (Induced connection on an associated bundle)
The principal connection $\omega$ induces a unique Ehresmann connection on $E\to M$ characterized by either of the following equivalent descriptions:

1. (**Horizontal lift description**)  
   For each $p\in P$ and $X\in T_{\pi(p)}M$, let $\widetilde X\in T_pP$ be the $\omega$-horizontal lift (see {{< knowl id="horizontal-lift-of-a-tangent-vector" text="horizontal lift of a tangent vector" >}}). For $[p,f]\in E$, define the horizontal subspace
   \[
   H_{[p,f]}E := (d q)_{(p,f)}\big(H_pP \times \{0\}\big),
   \]
   where $q:P\times F\to P\times_G F$ is the quotient map. This gives a smooth horizontal distribution complementary to the vertical bundle of $E$.

2. (**Parallel transport description**)  
   The principal connection defines parallel transport in $P$ (see {{< knowl id="construction-parallel-transport-map-along-a-curve" text="parallel transport along a curve" >}} and {{< knowl id="parallel-transport" text="parallel transport" >}}). Transporting $(p,f)\in P\times F$ by transporting $p$ horizontally and keeping $f$ fixed produces a well-defined transport in $E$, which is exactly the induced connection.

If $F=V$ is a vector space and the $G$-action comes from a representation $\rho:G\to \mathrm{GL}(V)$, then $E=P\times_\rho V$ is an {{< knowl id="associated-vector-bundle" text="associated vector bundle" >}}, and the induced Ehresmann connection is equivalent to a vector bundle connection $\nabla$ on $E$ (compare {{< knowl id="connection-on-a-vector-bundle" text="connection on a vector bundle" >}}). One concrete formulation is that $\nabla$ acts on sections via the covariant derivative obtained from horizontal lifts, as in {{< knowl id="construction-induced-covariant-derivative-on-associated-vector-bundle-sections" text="the induced covariant derivative on associated sections" >}}.

Moreover, the curvature of the induced connection is obtained by applying the representation to the principal curvature (see {{< knowl id="curvature-2-form-of-a-principal-connection" text="principal curvature" >}} and {{< knowl id="construction-curvature-of-an-induced-associated-connection-via-representation" text="curvature of induced associated connections" >}}).

## Examples
1. **Levi-Civita connection induces the usual covariant derivative on tensor bundles.**  
   On a Riemannian manifold, the orthonormal frame bundle $O(M)\to M$ (see {{< knowl id="orthonormal-frame-bundle-o-of-a-riemannian-manifold" text="orthonormal frame bundle" >}}) carries the {{< knowl id="levicivita-connection-connection" text="Levi-Civita connection" >}}. Any tensor bundle built from the standard representation of $O(n)$ (e.g. $TM$, $T^*M$, $\Lambda^kT^*M$) is an associated vector bundle, and the theorem recovers the usual Levi-Civita covariant derivative on those bundles.

2. **Adjoint bundle connection.**  
   Taking $F=\mathfrak g$ with the adjoint action, the associated bundle is $\mathrm{ad}(P)=P\times_{\mathrm{Ad}}\mathfrak g$ (see {{< knowl id="adjoint-bundle-p-g-g-with-conjugation-action" text="adjoint bundle" >}}). The induced connection is the standard “adjoint bundle connection,” and the associated covariant exterior derivative on $\mathfrak g$-valued tensorial forms is exactly the operator described in {{< knowl id="covariant-exterior-derivative-on-ad-valued-forms" text="covariant exterior derivative on adjoint-valued forms" >}}.

3. **Dirac monopole as an induced connection on a line bundle.**  
   The Hopf fibration $S^3\to S^2$ is a principal $U(1)$-bundle (see {{< knowl id="hopf-fibration-s3s2-as-a-principal-u-bundle" text="Hopf fibration" >}}). A principal connection on it (for instance the {{< knowl id="dirac-monopole-connection-on-the-hopf-bundle" text="Dirac monopole connection" >}}) induces a connection on every associated complex line bundle $S^3\times_{U(1)}\mathbb C$, recovering the usual covariant derivative used in the monopole picture.
