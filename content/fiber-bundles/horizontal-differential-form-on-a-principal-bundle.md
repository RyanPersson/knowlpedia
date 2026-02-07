---
title: "Horizontal differential form on a principal bundle"
description: "A differential form on a principal bundle that vanishes whenever any input vector is vertical"
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}. The vertical subbundle is
\[
V:=\ker(d\pi)\subset TP,
\]
as in {{< knowl id="vertical-subbundle" text="vertical subbundle" >}}.

A differential $k$-form $\alpha\in\Omega^k(P)$ is **horizontal** if, for every $p\in P$,
\[
\alpha_p(v_1,\dots,v_k)=0
\quad\text{whenever at least one }v_i\in V_p.
\]
Equivalently, $\alpha$ is horizontal if
\[
\iota_{X^\#}\alpha = 0\quad\text{for every }X\in\mathfrak g,
\]
where $X^\#$ is the {{< knowl id="convention-fundamental-vector-field-x-is-defined-using-the-right-action" text="fundamental vector field" >}} determined by the right principal action.

Horizontality is only a condition relative to the vertical distribution; it does not require choosing a {{< knowl id="horizontal-distribution" text="horizontal distribution" >}}. However, once a connection is chosen, horizontal forms can be evaluated on horizontal lifts of tangent vectors (compare {{< knowl id="horizontal-lift-of-a-tangent-vector" text="horizontal lift" >}}).

A form on $P$ is {{< knowl id="basic-differential-form-on-a-principal-bundle" text="basic" >}} exactly when it is horizontal and $G$-invariant (see {{< knowl id="invariant-differential-form" text="invariant differential form" >}}). Basic forms are precisely pullbacks of forms on $M$.

## Examples
1. **Pullbacks from the base are horizontal.**  
   If $\beta\in\Omega^k(M)$, then $\pi^*\beta$ is horizontal (and in fact basic). This is the standard example coming from {{< knowl id="pullback-of-differential-forms" text="pullback of differential forms" >}}.

2. **Curvature is horizontal; the connection form is not.**  
   For a principal connection with connection 1-form $\omega$, the curvature 2-form $\Omega$ is horizontal (and $\operatorname{Ad}$-equivariant), so it is tensorial. By contrast, $\omega$ is not horizontal because it reproduces vertical generators: $\omega(X^\#)=X$ (compare {{< knowl id="reproduction-property-x" text="reproduction property" >}}). See {{< knowl id="curvature-2-form-of-a-principal-connection" text="curvature 2-form of a principal connection" >}} and {{< knowl id="connection-1-form-on-a-principal-bundle" text="connection 1-form" >}}.

3. **Solder form on the frame bundle.**  
   On the {{< knowl id="frame-bundle-fr-of-a-manifold-m" text="frame bundle" >}} of a manifold, the {{< knowl id="solder-form-on-the-frame-bundle" text="solder form" >}} is a canonical horizontal 1-form with values in $\mathbb R^n$; it vanishes on vertical vectors because it encodes the projection of tangent vectors to the base.
