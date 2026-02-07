---
title: "Chern–Weil form"
description: "A differential form built from the curvature of a principal connection using an invariant polynomial."
---

Chern–Weil theory associates closed differential forms to a principal connection by applying invariant polynomials to its curvature. These are the differential-form representatives of {{< knowl id="characteristic-class" text="characteristic classes" >}}.

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} and let $\omega\in\Omega^1(P;\mathfrak{g})$ be a {{< knowl id="principal-connection" text="principal connection" >}} with curvature $\Omega\in\Omega^2(P;\mathfrak{g})$ (see {{< knowl id="curvature-2-form-of-a-principal-connection" text="curvature 2-form of a principal connection" >}}).

Let $P$ (unfortunately the same letter is standard) also denote an $\mathrm{Ad}$-invariant symmetric multilinear polynomial of degree $k$ on the Lie algebra $\mathfrak{g}$, i.e. an element of $(\mathrm{Sym}^k\mathfrak{g}^*)^G$.

The **Chern–Weil form** associated to the invariant polynomial $P$ and the connection $\omega$ is the $(2k)$-form on $P$
\[
P(\Omega)\;:=\;P(\underbrace{\Omega,\dots,\Omega}_{k\text{ times}})\in\Omega^{2k}(P),
\]
where the wedge product of the $\mathfrak{g}$-valued 2-forms is understood in the standard multilinear way.

A fundamental point is that $P(\Omega)$ is a **basic** form on $P$ (see {{< knowl id="lemma-chernweil-forms-are-basic" text="the lemma that Chern–Weil forms are basic" >}}), hence there exists a unique form $\mathrm{cw}_P(\omega)\in\Omega^{2k}(M)$ such that
\[
\pi^*\,\mathrm{cw}_P(\omega)=P(\Omega).
\]
By abuse of language, $\mathrm{cw}_P(\omega)$ is also called the Chern–Weil form on $M$.

## What Chern–Weil theory guarantees
- The form $\mathrm{cw}_P(\omega)$ is closed, and its de Rham cohomology class does not depend on the choice of connection; this is the content of {{< knowl id="chernweil-theorem-p-is-closed-and-its-de-rham-class-is-independent-of-connection" text="the Chern–Weil theorem" >}}.
- Consequently the class $[\mathrm{cw}_P(\omega)]\in H^{2k}_{\mathrm{dR}}(M)$ is an invariant of the underlying principal bundle (see {{< knowl id="corollary-chernweil-characteristic-classes-are-invariants-of-the-principal-bundle" text="Chern–Weil characteristic classes are bundle invariants" >}}).

## Examples
1. **First Chern form for a unitary bundle**
   Let $E\to M$ be a complex vector bundle with a Hermitian metric (see {{< knowl id="hermitian-metric" text="Hermitian metric" >}}) and a unitary connection. The associated principal $U(n)$-bundle of unitary frames yields a curvature matrix $F\in\Omega^2(M;\mathfrak{u}(n))$. Taking the invariant polynomial $P(X)=\frac{i}{2\pi}\mathrm{tr}(X)$ gives the 2-form
   \[
   c_1(\nabla)=\frac{i}{2\pi}\,\mathrm{tr}(F),
   \]
   representing the first Chern class in de Rham cohomology (see {{< knowl id="chern-class" text="Chern class" >}} and {{< knowl id="integrality-of-chern-classes" text="integrality of Chern classes" >}}).

2. **First Pontryagin form**
   For a real vector bundle with structure group reduced to $SO(n)$ and a compatible connection, the curvature $F\in\Omega^2(M;\mathfrak{so}(n))$ defines the 4-form
   \[
   p_1(\nabla)= -\frac{1}{8\pi^2}\,\mathrm{tr}(F\wedge F),
   \]
   which represents the first Pontryagin class (see {{< knowl id="pontryagin-class" text="Pontryagin class" >}}).

3. **Euler form via the Pfaffian**
   For an oriented rank-$2m$ real bundle with an $SO(2m)$-connection, the invariant polynomial given by the Pfaffian produces a $2m$-form representative of the Euler class (see {{< knowl id="euler-class" text="Euler class" >}}).
