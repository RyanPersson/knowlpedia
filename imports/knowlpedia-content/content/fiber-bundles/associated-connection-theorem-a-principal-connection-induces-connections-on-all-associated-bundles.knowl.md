+++
id = "fiber-bundles/associated-connection-theorem-a-principal-connection-induces-connections-on-all-associated-bundles"
title = "Associated connection theorem"
kind = "knowl"
summary = "A principal connection induces a compatible connection on every associated bundle and every associated vector bundle."
aliases = ["associated-connection-theorem-a-principal-connection-induces-connections-on-all-associated-bundles", "Associated connection theorem"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/associated-connection-theorem-a-principal-connection-induces-connections-on-all-associated-bundles.md"
+++

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with structure group $G$, and let $\omega$ be a [[fiber-bundles/principal-connection|principal connection]] on $P$ (equivalently a horizontal distribution; see [[fiber-bundles/horizontal-distribution|horizontal distribution]] and [[fiber-bundles/connection-1-form-on-a-principal-bundle|connection 1-form]]).

Let $F$ be a smooth left $G$-space (see [[fiber-bundles/smooth-action-of-a-lie-group-on-a-manifold|smooth G-action]]) and form the [[fiber-bundles/associated-bundle|associated bundle]]
\[
E := P\times_G F,
\]
as in [[fiber-bundles/construction-associated-bundle-p-g-f-from-a-left-g-space-f|the standard associated bundle construction]].

## Theorem (Induced connection on an associated bundle)
The principal connection $\omega$ induces a unique Ehresmann connection on $E\to M$ characterized by either of the following equivalent descriptions:

1. (**Horizontal lift description**)
   For each $p\in P$ and $X\in T_{\pi(p)}M$, let $\widetilde X\in T_pP$ be the $\omega$-horizontal lift (see [[fiber-bundles/horizontal-lift-of-a-tangent-vector|horizontal lift of a tangent vector]]). For $[p,f]\in E$, define the horizontal subspace
   \[
   H_{[p,f]}E := (d q)_{(p,f)}\big(H_pP \times \{0\}\big),
   \]
   where $q:P\times F\to P\times_G F$ is the quotient map. This gives a smooth horizontal distribution complementary to the vertical bundle of $E$.

2. (**Parallel transport description**)
   The principal connection defines parallel transport in $P$ (see [[fiber-bundles/construction-parallel-transport-map-along-a-curve|parallel transport along a curve]] and [[fiber-bundles/parallel-transport|parallel transport]]). Transporting $(p,f)\in P\times F$ by transporting $p$ horizontally and keeping $f$ fixed produces a well-defined transport in $E$, which is exactly the induced connection.

If $F=V$ is a vector space and the $G$-action comes from a representation $\rho:G\to \mathrm{GL}(V)$, then $E=P\times_\rho V$ is an [[fiber-bundles/associated-vector-bundle|associated vector bundle]], and the induced Ehresmann connection is equivalent to a vector bundle connection $\nabla$ on $E$ (compare [[fiber-bundles/connection-on-a-vector-bundle|connection on a vector bundle]]). One concrete formulation is that $\nabla$ acts on sections via the covariant derivative obtained from horizontal lifts, as in [[fiber-bundles/construction-induced-covariant-derivative-on-associated-vector-bundle-sections|the induced covariant derivative on associated sections]].

Moreover, the curvature of the induced connection is obtained by applying the representation to the principal curvature (see [[fiber-bundles/curvature-2-form-of-a-principal-connection|principal curvature]] and [[fiber-bundles/construction-curvature-of-an-induced-associated-connection-via-representation|curvature of induced associated connections]]).

## Examples
1. **Levi-Civita connection induces the usual covariant derivative on tensor bundles.**
   On a Riemannian manifold, the orthonormal frame bundle $O(M)\to M$ (see [[fiber-bundles/orthonormal-frame-bundle-o-of-a-riemannian-manifold|orthonormal frame bundle]]) carries the [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]]. Any tensor bundle built from the standard representation of $O(n)$ (e.g. $TM$, $T^*M$, $\Lambda^kT^*M$) is an associated vector bundle, and the theorem recovers the usual Levi-Civita covariant derivative on those bundles.

2. **Adjoint bundle connection.**
   Taking $F=\mathfrak g$ with the adjoint action, the associated bundle is $\mathrm{ad}(P)=P\times_{\mathrm{Ad}}\mathfrak g$ (see [[fiber-bundles/adjoint-bundle-p-g-g-with-conjugation-action|adjoint bundle]]). The induced connection is the standard “adjoint bundle connection,” and the associated covariant exterior derivative on $\mathfrak g$-valued tensorial forms is exactly the operator described in [[fiber-bundles/covariant-exterior-derivative-on-ad-valued-forms|covariant exterior derivative on adjoint-valued forms]].

3. **Dirac monopole as an induced connection on a line bundle.**
   The Hopf fibration $S^3\to S^2$ is a principal $U(1)$-bundle (see [[fiber-bundles/hopf-fibration-s3s2-as-a-principal-u-bundle|Hopf fibration]]). A principal connection on it (for instance the [[fiber-bundles/dirac-monopole-connection-on-the-hopf-bundle|Dirac monopole connection]]) induces a connection on every associated complex line bundle $S^3\times_{U(1)}\mathbb C$, recovering the usual covariant derivative used in the monopole picture.
