+++
id = "fiber-bundles/chernweil-form"
title = "Chern–Weil form"
kind = "knowl"
summary = "A differential form built from the curvature of a principal connection using an invariant polynomial."
aliases = ["chernweil-form", "Chern–Weil form"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/chernweil-form.md"
+++

Chern–Weil theory associates closed differential forms to a principal connection by applying invariant polynomials to its curvature. These are the differential-form representatives of [[fiber-bundles/characteristic-class|characteristic classes]].

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] and let $\omega\in\Omega^1(P;\mathfrak{g})$ be a [[fiber-bundles/principal-connection|principal connection]] with curvature $\Omega\in\Omega^2(P;\mathfrak{g})$ (see [[fiber-bundles/curvature-2-form-of-a-principal-connection|curvature 2-form of a principal connection]]).

Let $P$ (unfortunately the same letter is standard) also denote an $\mathrm{Ad}$-invariant symmetric multilinear polynomial of degree $k$ on the Lie algebra $\mathfrak{g}$, i.e. an element of $(\mathrm{Sym}^k\mathfrak{g}^*)^G$.

The **Chern–Weil form** associated to the invariant polynomial $P$ and the connection $\omega$ is the $(2k)$-form on $P$
\[
P(\Omega)\;:=\;P(\underbrace{\Omega,\dots,\Omega}_{k\text{ times}})\in\Omega^{2k}(P),
\]
where the wedge product of the $\mathfrak{g}$-valued 2-forms is understood in the standard multilinear way.

A fundamental point is that $P(\Omega)$ is a **basic** form on $P$ (see [[fiber-bundles/lemma-chernweil-forms-are-basic|the lemma that Chern–Weil forms are basic]]), hence there exists a unique form $\mathrm{cw}_P(\omega)\in\Omega^{2k}(M)$ such that
\[
\pi^*\,\mathrm{cw}_P(\omega)=P(\Omega).
\]
By abuse of language, $\mathrm{cw}_P(\omega)$ is also called the Chern–Weil form on $M$.

## What Chern–Weil theory guarantees
- The form $\mathrm{cw}_P(\omega)$ is closed, and its de Rham cohomology class does not depend on the choice of connection; this is the content of [[fiber-bundles/chernweil-theorem-p-is-closed-and-its-de-rham-class-is-independent-of-connection|the Chern–Weil theorem]].
- Consequently the class $[\mathrm{cw}_P(\omega)]\in H^{2k}_{\mathrm{dR}}(M)$ is an invariant of the underlying principal bundle (see [[fiber-bundles/corollary-chernweil-characteristic-classes-are-invariants-of-the-principal-bundle|Chern–Weil characteristic classes are bundle invariants]]).

## Examples
1. **First Chern form for a unitary bundle**
   Let $E\to M$ be a complex vector bundle with a Hermitian metric (see [[fiber-bundles/hermitian-metric|Hermitian metric]]) and a unitary connection. The associated principal $U(n)$-bundle of unitary frames yields a curvature matrix $F\in\Omega^2(M;\mathfrak{u}(n))$. Taking the invariant polynomial $P(X)=\frac{i}{2\pi}\mathrm{tr}(X)$ gives the 2-form
   \[
   c_1(\nabla)=\frac{i}{2\pi}\,\mathrm{tr}(F),
   \]
   representing the first Chern class in de Rham cohomology (see [[fiber-bundles/chern-class|Chern class]] and [[fiber-bundles/integrality-of-chern-classes|integrality of Chern classes]]).

2. **First Pontryagin form**
   For a real vector bundle with structure group reduced to $SO(n)$ and a compatible connection, the curvature $F\in\Omega^2(M;\mathfrak{so}(n))$ defines the 4-form
   \[
   p_1(\nabla)= -\frac{1}{8\pi^2}\,\mathrm{tr}(F\wedge F),
   \]
   which represents the first Pontryagin class (see [[fiber-bundles/pontryagin-class|Pontryagin class]]).

3. **Euler form via the Pfaffian**
   For an oriented rank-$2m$ real bundle with an $SO(2m)$-connection, the invariant polynomial given by the Pfaffian produces a $2m$-form representative of the Euler class (see [[fiber-bundles/euler-class|Euler class]]).
