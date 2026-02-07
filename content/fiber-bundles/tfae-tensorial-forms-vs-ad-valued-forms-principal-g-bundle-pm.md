---
title: "Tensorial forms and ad(P)-valued forms"
description: "Equivalence between horizontal equivariant Lie-algebra-valued forms on a principal bundle and differential forms on the base with values in the adjoint bundle."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} over a {{< knowl id="smooth-manifold" text="smooth manifold" >}} $M$, where $G$ is a {{< knowl id="lie-group" text="Lie group" >}} with {{< knowl id="lie-algebra" text="Lie algebra" section="lie-groups">}} $\mathfrak g$.

The **adjoint bundle** of $P$ is the associated vector bundle
\[
\operatorname{ad}(P):=P\times_{\operatorname{Ad}}\mathfrak g \;\longrightarrow\; M,
\]
where $G$ acts on $\mathfrak g$ by the adjoint representation $\operatorname{Ad}$.

A $\mathfrak g$-valued {{< knowl id="differential-k-form" text="differential k-form" >}} $\omega\in\Omega^k(P;\mathfrak g)$ is called **tensorial of type $\operatorname{Ad}$** if it satisfies:

1. **Horizontality:** $\omega_p(v_1,\dots,v_k)=0$ whenever at least one $v_i\in\ker(d\pi_p)$ (i.e., a vertical tangent vector).
2. **Equivariance:** for every $g\in G$,
   \[
   (R_g)^*\omega = \operatorname{Ad}(g^{-1})\,\omega,
   \]
   where $R_g:P\to P$ is the right action.

Write $\Omega^k_{\mathrm{tens}}(P;\mathfrak g)$ for the vector space of such tensorial forms.

## Theorem (TFAE: tensorial forms vs ad(P)-valued forms)
There is a natural vector space isomorphism
\[
\Omega^k_{\mathrm{tens}}(P;\mathfrak g)\;\cong\;\Omega^k\!\bigl(M;\operatorname{ad}(P)\bigr).
\]

More explicitly:

- Given $\omega\in\Omega^k_{\mathrm{tens}}(P;\mathfrak g)$, define $\alpha\in\Omega^k(M;\operatorname{ad}(P))$ by
  \[
  \alpha_x(u_1,\dots,u_k)\;:=\;\bigl[p,\;\omega_p(\tilde u_1,\dots,\tilde u_k)\bigr]\in \operatorname{ad}(P)_x,
  \]
  where $p\in P$ satisfies $\pi(p)=x$, and $\tilde u_i\in T_pP$ are any tangent vectors with $d\pi_p(\tilde u_i)=u_i$.
  This is well-defined because vertical components do not affect $\omega$ (horizontality) and changing $p$ in the fiber changes $\omega$ by $\operatorname{Ad}(g^{-1})$ (equivariance), exactly matching the associated-bundle identification.

- Conversely, given $\alpha\in\Omega^k(M;\operatorname{ad}(P))$, define $\omega\in\Omega^k(P;\mathfrak g)$ by requiring that for $p\in P$ and $v_i\in T_pP$,
  \[
  \alpha_{\pi(p)}(d\pi_p v_1,\dots,d\pi_p v_k)=\bigl[p,\;\omega_p(v_1,\dots,v_k)\bigr]\in\operatorname{ad}(P)_{\pi(p)}.
  \]
  This forces $\omega$ to be horizontal, and the associated-bundle relation forces $\operatorname{Ad}$-equivariance.

These constructions are inverse to each other and are natural with respect to bundle morphisms covering the identity on $M$.

A key application is that the {{< knowl id="curvature" text="curvature" >}} of a {{< knowl id="principal-connection" text="principal connection" >}} is tensorial of type $\operatorname{Ad}$, hence canonically corresponds to an $\operatorname{ad}(P)$-valued 2-form on the base.

## Examples
1. **Curvature descends to the base.**  
   If $\Theta$ is a principal connection on $P$ with curvature $F_\Theta\in\Omega^2(P;\mathfrak g)$, then $F_\Theta$ is horizontal and $\operatorname{Ad}$-equivariant. The theorem identifies $F_\Theta$ with a unique element of $\Omega^2(M;\operatorname{ad}(P))$.

2. **Trivial bundle case.**  
   On the {{< knowl id="trivial-principal-bundle-mgm" text="trivial principal bundle" >}} $P=M\times G$, the adjoint bundle is canonically isomorphic to $M\times\mathfrak g$. Under this identification, a tensorial $\omega$ corresponds to an ordinary $\mathfrak g$-valued form on $M$ (written in a chosen global section), and the correspondence is given by pullback along the section and associated-bundle identification.

3. **Scalar “basic” forms as a special case.**  
   If one replaces $\mathfrak g$ by a trivial $G$-representation (so equivariance becomes $G$-invariance), then horizontal $G$-invariant forms on $P$ correspond exactly to ordinary differential forms on $M$ via pullback along $\pi$.
