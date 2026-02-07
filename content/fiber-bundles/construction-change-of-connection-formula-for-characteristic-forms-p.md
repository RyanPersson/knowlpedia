---
title: "Change of connection formula for Chern Weil characteristic forms"
description: "Exact formula relating characteristic forms computed from two different principal connections"
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}, and let $\omega_0,\omega_1$ be two {{< knowl id="principal-connection" text="principal connections" >}} on $P$ with connection 1-forms (also denoted) $\omega_0,\omega_1\in \Omega^1(P;\mathfrak g)$ as in {{< knowl id="connection-1-form-on-a-principal-bundle" text="connection 1-forms on principal bundles" >}}. Write their curvature 2-forms as $\Omega_0,\Omega_1\in \Omega^2(P;\mathfrak g)$ (see {{< knowl id="curvature-2-form-of-a-principal-connection" text="curvature 2-forms of principal connections" >}}).

Let $p\in \operatorname{Sym}^k(\mathfrak g^*)^G$ be an $\operatorname{Ad}$-invariant homogeneous polynomial of degree $k$, so that the associated {{< knowl id="chernweil-form" text="Chern Weil form" >}} $p(\Omega)$ is a closed $2k$-form on $M$ (via basicness on $P$), as in {{< knowl id="chernweil-theorem-p-is-closed-and-its-de-rham-class-is-independent-of-connection" text="the Chern Weil theorem" >}}.

Define the difference
\[
\eta := \omega_1-\omega_0 \in \Omega^1(P;\mathfrak g).
\]
By {{< knowl id="lemma-difference-of-two-principal-connections-is-tensorial" text="tensoriality of differences of principal connections" >}}, $\eta$ is horizontal and equivariant (hence “tensorial”), so it corresponds to an $\operatorname{ad}(P)$-valued 1-form on $M$.

Consider the straight-line path of connections
\[
\omega_t := \omega_0 + t\,\eta,\qquad t\in[0,1],
\]
with curvature
\[
\Omega_t := d\omega_t + \tfrac12[\omega_t\wedge \omega_t]
\]
(compare {{< knowl id="cartans-second-structure-equation" text="Cartan's second structure equation" >}}).

### Change-of-connection (transgression) formula
Define the transgression form
\[
T_p(\omega_0,\omega_1)
:= k \int_0^1 p\bigl(\eta \wedge \Omega_t^{k-1}\bigr)\,dt,
\]
a $(2k-1)$-form on $P$ which is basic and therefore descends to a $(2k-1)$-form on $M$ (often also denoted $T_p(\omega_0,\omega_1)$).

Then the characteristic forms satisfy
\[
p(\Omega_1) - p(\Omega_0) \;=\; d\,T_p(\omega_0,\omega_1),
\]
so the two forms differ by an exact form on $M$. In particular, the de Rham class of $p(\Omega)$ does not depend on the chosen connection, which is the mechanism behind {{< knowl id="corollary-chernweil-characteristic-classes-are-invariants-of-the-principal-bundle" text="Chern Weil characteristic classes being invariants of the principal bundle" >}}.

This construction is the standard transgression mechanism (see {{< knowl id="transgression-form" text="transgression forms" >}} and {{< knowl id="transgression-theorem-p-p-is-exact" text="the transgression theorem" >}}), and in low degrees it produces the usual {{< knowl id="chernsimons-form" text="Chern Simons forms" >}}.

## Examples
1. **Degree 1 (abelian-style) case.**  
   If $k=1$ and $p:\mathfrak g\to\mathbb R$ is an $\operatorname{Ad}$-invariant linear functional, then
   \[
   T_p(\omega_0,\omega_1)=p(\eta),\qquad p(\Omega_1)-p(\Omega_0)=d\,p(\eta).
   \]
   For $G=U(1)$ this recovers the familiar fact that changing a connection 1-form changes the curvature 2-form by an exact 2-form (compare the local picture in {{< knowl id="local-connection-1-form" text="local connection 1-forms" >}}).

2. **Degree 2 and the Chern Simons 3-form.**  
   For $k=2$ and an invariant quadratic polynomial $p$ (for instance a suitably normalized trace form on a matrix Lie algebra), the transgression is a 3-form
   \[
   T_p(\omega_0,\omega_1) = 2\int_0^1 p(\eta\wedge \Omega_t)\,dt,
   \]
   and the formula says $p(\Omega_1)-p(\Omega_0)$ is exact with this primitive. On a trivial bundle, taking $\omega_0=0$ and $\omega_1=A$ yields the usual Chern Simons expression in terms of $A$ and $dA$, matching the standard {{< knowl id="chernsimons-form" text="Chern Simons form" >}} on a chart.

3. **Pontryagin forms from different connections.**  
   Let $E\to M$ be a real vector bundle with two {{< knowl id="connection-on-a-vector-bundle" text="vector bundle connections" >}} $\nabla^0,\nabla^1$. Using the induced connections on the {{< knowl id="frame-bundle-frame-bundle-of-a-rank-n-vector-bundle" text="frame bundle" >}} (via {{< knowl id="construction-connection-on-fr-induced-by-a-vector-bundle-connection" text="the induced principal connection construction" >}}), the change-of-connection formula implies that the associated Pontryagin forms differ by an exact form. Hence the resulting {{< knowl id="pontryagin-class" text="Pontryagin classes" >}} are independent of the chosen connection.
