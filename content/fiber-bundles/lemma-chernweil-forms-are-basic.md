---
title: "Lemma: Chern–Weil forms are basic"
description: "Applying an invariant polynomial to the curvature of a principal connection produces a basic differential form."
---

This lemma explains why the Chern–Weil construction produces differential forms on the base manifold from data on the total space.

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}, let $\omega$ be a {{< knowl id="principal-connection" text="principal connection" >}} on $P$, and let $\Omega\in\Omega^2(P;\mathfrak{g})$ be its {{< knowl id="curvature-2-form-of-a-principal-connection" text="curvature 2-form" >}}.

Let $P$ denote an $\mathrm{Ad}$-invariant symmetric multilinear polynomial of degree $k$ on $\mathfrak{g}$, so that the {{< knowl id="chernweil-form" text="Chern–Weil form" >}} on the total space is
\[
P(\Omega)=P(\underbrace{\Omega,\dots,\Omega}_{k\text{ times}})\in\Omega^{2k}(P).
\]

## Statement
The form $P(\Omega)$ is **basic** on $P$ in the sense of {{< knowl id="basic-differential-form-on-a-principal-bundle" text="basic differential forms on a principal bundle" >}}. Concretely:

1. **Horizontality:** for every fundamental vertical vector field $X^\#$ on $P$ (see {{< knowl id="convention-fundamental-vector-field-x-is-defined-using-the-right-action" text="fundamental vector field convention" >}}),
   \[
   \iota_{X^\#}\,P(\Omega)=0.
   \]
   Equivalently, $P(\Omega)$ vanishes whenever any argument is vertical, so it is a {{< knowl id="horizontal-differential-form-on-a-principal-bundle" text="horizontal form" >}}.

2. **$G$-invariance:** for every $g\in G$,
   \[
   R_g^*\,P(\Omega)=P(\Omega),
   \]
   so it is an {{< knowl id="invariant-differential-form" text="invariant differential form" >}}.

Therefore there exists a unique form $\alpha\in\Omega^{2k}(M)$ such that $\pi^*\alpha=P(\Omega)$; this $\alpha$ is the Chern–Weil form on the base.

## Examples
1. **Abelian case: $U(1)$**
   For $G=U(1)$, the adjoint action is trivial, and $P$ can be taken to be the identity on $\mathfrak{u}(1)\cong i\mathbb{R}$. Then the Chern–Weil form is simply $P(\Omega)=\Omega$, and the lemma says $\Omega$ is basic, hence descends to a 2-form on $M$. This is exactly what happens in the {{< knowl id="dirac-monopole-connection-on-the-hopf-bundle" text="Dirac monopole" >}} example on the Hopf bundle.

2. **Unitary bundles**
   For a principal $U(n)$-bundle, take $P(X)=\mathrm{tr}(X)$ or $P(X)=\mathrm{tr}(X^k)$. The lemma guarantees that $\mathrm{tr}(\Omega)$ and $\mathrm{tr}(\Omega^k)$ are basic forms on $P$, so they correspond to well-defined differential forms on $M$ representing Chern classes (see {{< knowl id="chern-class" text="Chern class" >}}).

3. **Orthogonal bundles and Pontryagin forms**
   For $G=SO(n)$, invariant polynomials such as $P(X)=\mathrm{tr}(X^2)$ produce Pontryagin forms (see {{< knowl id="pontryagin-class" text="Pontryagin class" >}}). The lemma ensures these forms are basic and hence live on the base manifold, not just on the total space of frames.
