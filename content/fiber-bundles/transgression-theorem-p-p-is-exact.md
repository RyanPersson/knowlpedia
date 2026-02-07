---
title: "Transgression theorem (Chern–Simons)"
description: "The difference of Chern–Weil forms for two connections is exact, with an explicit transgression form."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}. Let $\omega_0,\omega_1$ be two {{< knowl id="principal-connection" text="principal connections" >}} on $P$ with curvatures $\Omega_0,\Omega_1$. Let $P$ be an Ad-invariant homogeneous polynomial of degree $k$ on $\mathfrak g$, and let $\operatorname{cw}_P(\omega_i)$ be the descended Chern–Weil forms on $M$ as in the {{< knowl id="chernweil-theorem-p-is-closed-and-its-de-rham-class-is-independent-of-connection" text="Chern–Weil theorem" >}}.

Write $\eta:=\omega_1-\omega_0$ (a tensorial $\mathfrak g$-valued $1$-form; see {{< knowl id="lemma-difference-of-two-principal-connections-is-tensorial" text="difference is tensorial" >}}), and define a path of connections $\omega_t:=\omega_0+t\eta$ with curvature $\Omega_t$.

**Theorem (Transgression / Chern–Simons).** There exists a $(2k-1)$-form $\mathrm{CS}_P(\omega_0,\omega_1)\in\Omega^{2k-1}(M)$ such that
\[
d\,\mathrm{CS}_P(\omega_0,\omega_1)=\operatorname{cw}_P(\omega_1)-\operatorname{cw}_P(\omega_0),
\]
where $d$ is the {{< knowl id="exterior-derivative" text="exterior derivative" >}}. One explicit choice is the Chern–Simons transgression form
\[
\mathrm{CS}_P(\omega_0,\omega_1)
:= k\int_0^1 P\big(\eta,\Omega_t,\dots,\Omega_t\big)\,dt,
\]
where $P(\eta,\Omega_t,\dots,\Omega_t)$ denotes the $(2k-1)$-form obtained by inserting one $1$-form $\eta$ and $(k-1)$ copies of the $2$-form $\Omega_t$ into the symmetric $k$-linear map $P$ and wedging.

In particular, the de Rham class $[\operatorname{cw}_P(\omega)]$ is independent of $\omega$.

## Examples
1. **Degree 1 (abelian case).** For $k=1$ and $P(X)=X$ (e.g. $G=U(1)$), $\operatorname{cw}_P(\omega)$ is just the curvature $2$-form on the base, and the formula becomes $\operatorname{cw}_P(\omega_1)-\operatorname{cw}_P(\omega_0)=d(A_1-A_0)$ in a local gauge.
2. **Degree 2 (classical 3D Chern–Simons).** For a matrix group and $P(X)=\mathrm{tr}(X^2)$, the transgression gives the usual $3$-form on a trivialization:
   \[
   \mathrm{CS}(A)=\mathrm{tr}\!\left(A\wedge dA+\tfrac23 A\wedge A\wedge A\right),
   \]
   whose exterior derivative is $\mathrm{tr}(F\wedge F)$.
3. **Gauge-equivalent connections.** If $\omega_1$ is obtained from $\omega_0$ by a gauge transformation, then $\operatorname{cw}_P(\omega_1)-\operatorname{cw}_P(\omega_0)$ is exact; the theorem produces an explicit primitive.
