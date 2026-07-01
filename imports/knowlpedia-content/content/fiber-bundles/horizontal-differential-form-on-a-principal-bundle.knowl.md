+++
id = "fiber-bundles/horizontal-differential-form-on-a-principal-bundle"
title = "Horizontal differential form on a principal bundle"
kind = "knowl"
summary = "A differential form on a principal bundle that vanishes whenever any input vector is vertical"
aliases = ["horizontal-differential-form-on-a-principal-bundle", "Horizontal differential form on a principal bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/horizontal-differential-form-on-a-principal-bundle.md"
+++

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]]. The vertical subbundle is
\[
V:=\ker(d\pi)\subset TP,
\]
as in [[fiber-bundles/vertical-subbundle|vertical subbundle]].

A differential $k$-form $\alpha\in\Omega^k(P)$ is **horizontal** if, for every $p\in P$,
\[
\alpha_p(v_1,\dots,v_k)=0
\quad\text{whenever at least one }v_i\in V_p.
\]
Equivalently, $\alpha$ is horizontal if
\[
\iota_{X^\#}\alpha = 0\quad\text{for every }X\in\mathfrak g,
\]
where $X^\#$ is the [[fiber-bundles/convention-fundamental-vector-field-x-is-defined-using-the-right-action|fundamental vector field]] determined by the right principal action.

Horizontality is only a condition relative to the vertical distribution; it does not require choosing a [[fiber-bundles/horizontal-distribution|horizontal distribution]]. However, once a connection is chosen, horizontal forms can be evaluated on horizontal lifts of tangent vectors (compare [[fiber-bundles/horizontal-lift-of-a-tangent-vector|horizontal lift]]).

A form on $P$ is [[fiber-bundles/basic-differential-form-on-a-principal-bundle|basic]] exactly when it is horizontal and $G$-invariant (see [[fiber-bundles/invariant-differential-form|invariant differential form]]). Basic forms are precisely pullbacks of forms on $M$.

## Examples
1. **Pullbacks from the base are horizontal.**
   If $\beta\in\Omega^k(M)$, then $\pi^*\beta$ is horizontal (and in fact basic). This is the standard example coming from [[fiber-bundles/pullback-of-differential-forms|pullback of differential forms]].

2. **Curvature is horizontal; the connection form is not.**
   For a principal connection with connection 1-form $\omega$, the curvature 2-form $\Omega$ is horizontal (and $\operatorname{Ad}$-equivariant), so it is tensorial. By contrast, $\omega$ is not horizontal because it reproduces vertical generators: $\omega(X^\#)=X$ (compare [[fiber-bundles/reproduction-property-x|reproduction property]]). See [[fiber-bundles/curvature-2-form-of-a-principal-connection|curvature 2-form of a principal connection]] and [[fiber-bundles/connection-1-form-on-a-principal-bundle|connection 1-form]].

3. **Solder form on the frame bundle.**
   On the [[fiber-bundles/frame-bundle-fr-of-a-manifold-m|frame bundle]] of a manifold, the [[fiber-bundles/solder-form-on-the-frame-bundle|solder form]] is a canonical horizontal 1-form with values in $\mathbb R^n$; it vanishes on vertical vectors because it encodes the projection of tangent vectors to the base.
