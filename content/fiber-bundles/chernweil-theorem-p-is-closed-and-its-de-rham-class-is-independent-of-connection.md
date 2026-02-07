---
title: "Chern–Weil theorem"
description: "Invariant polynomials in curvature yield closed forms whose cohomology class does not depend on the connection."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure group $G$ and Lie algebra $\mathfrak g$. Let $\omega$ be a {{< knowl id="principal-connection" text="principal connection" >}} with {{< knowl id="curvature" text="curvature" >}} $\Omega\in\Omega^2(P;\mathfrak g)$.

Let $P$ be an Ad-invariant homogeneous polynomial of degree $k$ on $\mathfrak g$, equivalently a symmetric $k$-linear map
\[
P:\underbrace{\mathfrak g\times\cdots\times\mathfrak g}_{k\ \text{times}}\to \mathbb R
\quad\text{satisfying}\quad
P(\mathrm{Ad}(g)X_1,\dots,\mathrm{Ad}(g)X_k)=P(X_1,\dots,X_k).
\]
Define the $2k$-form on $P$ by inserting $\Omega$ into $P$ and wedging:
\[
P(\Omega)\in\Omega^{2k}(P),\qquad
P(\Omega):=P(\Omega,\dots,\Omega),
\]
with the usual graded antisymmetrization convention.

**Theorem (Chern–Weil).**
1. The form $P(\Omega)$ is **closed**, i.e. $d\,P(\Omega)=0$.
2. The form $P(\Omega)$ is **basic** (see {{< knowl id="lemma-chernweil-forms-are-basic" text="Chern–Weil forms are basic" >}}), hence by the {{< knowl id="basic-forms-theorem" text="basic forms theorem" >}} there is a unique closed form $\operatorname{cw}_P(\omega)\in\Omega^{2k}(M)$ with
   \[
   \pi^*\operatorname{cw}_P(\omega)=P(\Omega).
   \]
3. The de Rham cohomology class $[\operatorname{cw}_P(\omega)]\in H^{2k}_{\mathrm{dR}}(M)$ is independent of the choice of connection $\omega$; equivalently, changing $\omega$ changes $\operatorname{cw}_P(\omega)$ by an exact form (see the {{< knowl id="transgression-theorem-p-p-is-exact" text="transgression theorem" >}}).

A standard route to (1) is to combine the {{< knowl id="bianchi-identity" text="Bianchi identity" >}} with Ad-invariance of $P$.

## Examples
1. **First Chern form for U(1).** For $G=U(1)$ and $P(X)=\frac{i}{2\pi}X$ (viewing $\mathfrak u(1)\cong i\mathbb R$), $\operatorname{cw}_P(\omega)=\frac{i}{2\pi}F$ is the usual curvature representative of the first Chern class.
2. **Second Chern character piece.** For a matrix group such as $G=SU(n)$ and $P(X)=\mathrm{tr}(X^2)$, the descended form $\mathrm{tr}(F\wedge F)$ is closed and defines a characteristic class independent of the connection.
3. **Pontryagin-type forms.** For $G=SO(n)$, Ad-invariant polynomials built from traces of even powers (e.g. $\mathrm{tr}(X^{2j})$ in the defining representation) produce the usual Pontryagin form representatives on the base.
