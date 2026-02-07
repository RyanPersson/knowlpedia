---
title: "Covariant exterior derivative preserves tensoriality"
description: "For a principal connection, the covariant exterior derivative sends tensorial forms to tensorial forms."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with right action $R_g:P\to P$, and let $\rho:G\to \mathrm{GL}(V)$ be a finite-dimensional representation with differential $\rho_*:\mathfrak g\to \mathfrak{gl}(V)$ (see {{< knowl id="representation-of-a-lie-group" text="representation of a Lie group" section="lie-groups">}}).

A $V$-valued $k$-form $\alpha\in \Omega^k(P;V)$ is **tensorial of type $\rho$** if
1. (**Horizontality**) $\alpha_p(v_1,\dots,v_k)=0$ whenever at least one $v_i$ is vertical (i.e. tangent to the fiber), equivalently $\iota_{X^\#}\alpha=0$ for all fundamental vertical vector fields $X^\#$ (compare {{< knowl id="vertical-subbundle" text="vertical subbundle" >}} and {{< knowl id="convention-fundamental-vector-field-x-is-defined-using-the-right-action" text="fundamental vector fields" >}}).
2. (**$\rho$-equivariance**) $(R_g)^*\alpha=\rho(g^{-1})\alpha$ for all $g\in G$ (compare {{< knowl id="equivariant-map" text="equivariance" >}}).

Fix a {{< knowl id="principal-connection" text="principal connection" >}} with connection $1$-form $\omega\in \Omega^1(P;\mathfrak g)$ (see {{< knowl id="connection-1-form-on-a-principal-bundle" text="connection 1-form" >}}). Let $\mathrm{hor}:TP\to TP$ denote the horizontal projection determined by $\omega$. The **covariant exterior derivative** of a $V$-valued $k$-form is the operator
\[
D^\omega:\Omega^k(P;V)\longrightarrow \Omega^{k+1}(P;V),
\qquad
(D^\omega\alpha)(v_0,\dots,v_k):=d\alpha(\mathrm{hor}\,v_0,\dots,\mathrm{hor}\,v_k).
\]
Equivalently, on tensorial forms one may write the usual local formula
\[
D^\omega\alpha = d\alpha + \rho_*(\omega)\wedge \alpha,
\]
where the wedge combines $\mathfrak{gl}(V)$ acting on $V$ with the exterior product.

## Lemma
If $\alpha$ is tensorial of type $\rho$, then $D^\omega\alpha$ is also tensorial of type $\rho$.

In other words, the covariant exterior derivative restricts to a well-defined map
\[
D^\omega:\Omega^k_{\mathrm{tens}}(P;V)\longrightarrow \Omega^{k+1}_{\mathrm{tens}}(P;V),
\]
where $\Omega^k_{\mathrm{tens}}(P;V)$ denotes $V$-valued tensorial $k$-forms. This is the basic mechanism behind induced connections on {{< knowl id="associated-bundle" text="associated bundles" >}} and, in the vector bundle case, on {{< knowl id="associated-vector-bundle" text="associated vector bundles" >}}.

## Examples
1. **From equivariant functions to covariant derivatives.**  
   A tensorial $0$-form of type $\rho$ is just a $\rho$-equivariant function $f:P\to V$. Under the identification of such functions with sections of the associated bundle $E=P\times_\rho V$ (see {{< knowl id="equivariant-map-pf-associated-to-a-section-of-p-g-f" text="equivariant maps and sections" >}}), the tensorial $1$-form $D^\omega f$ corresponds to the covariant derivative $\nabla s$ of the associated section $s\in \Gamma(E)$ (see {{< knowl id="covariant-derivative-of-a-section" text="covariant derivative of a section" >}}).

2. **Adjoint-valued forms and the Bianchi identity setting.**  
   Taking $V=\mathfrak g$ with the adjoint representation (see {{< knowl id="adjoint-action-of-a-lie-group" text="adjoint action" section="lie-groups">}}), tensorial $\mathfrak g$-valued forms are the same objects that appear in {{< knowl id="covariant-exterior-derivative-on-ad-valued-forms" text="covariant exterior derivatives on adjoint-valued forms" >}}. In particular, the curvature form $F^\omega\in\Omega^2(P;\mathfrak g)$ (see {{< knowl id="curvature-2-form-of-a-principal-connection" text="curvature 2-form" >}}) is tensorial, hence $D^\omega F^\omega$ is a well-defined tensorial $3$-form.

3. **Frame bundle viewpoint.**  
   On the frame bundle of a vector bundle (see {{< knowl id="construction-frame-bundle-fr-of-a-vector-bundle-e" text="frame bundle construction" >}}), tensorial forms of the defining representation encode tensor fields on the base. The lemma guarantees that applying $D^\omega$ to such a tensorial form produces another tensorial form, which is exactly what is needed for defining covariant derivatives of tensor fields via the frame bundle picture (compare {{< knowl id="tfae-vector-bundle-connections-via-frame-bundles-rank-n-vector-bundle-em" text="connections via frame bundles" >}}).
