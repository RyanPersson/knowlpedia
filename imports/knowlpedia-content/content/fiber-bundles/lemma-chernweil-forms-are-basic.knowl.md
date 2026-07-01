+++
id = "fiber-bundles/lemma-chernweil-forms-are-basic"
title = "Lemma: Chern–Weil forms are basic"
kind = "knowl"
summary = "Applying an invariant polynomial to the curvature of a principal connection produces a basic differential form."
aliases = ["lemma-chernweil-forms-are-basic", "Lemma: Chern–Weil forms are basic"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/lemma-chernweil-forms-are-basic.md"
+++

This lemma explains why the Chern–Weil construction produces differential forms on the base manifold from data on the total space.

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]], let $\omega$ be a [[fiber-bundles/principal-connection|principal connection]] on $P$, and let $\Omega\in\Omega^2(P;\mathfrak{g})$ be its [[fiber-bundles/curvature-2-form-of-a-principal-connection|curvature 2-form]].

Let $P$ denote an $\mathrm{Ad}$-invariant symmetric multilinear polynomial of degree $k$ on $\mathfrak{g}$, so that the [[fiber-bundles/chernweil-form|Chern–Weil form]] on the total space is
\[
P(\Omega)=P(\underbrace{\Omega,\dots,\Omega}_{k\text{ times}})\in\Omega^{2k}(P).
\]

## Statement
The form $P(\Omega)$ is **basic** on $P$ in the sense of [[fiber-bundles/basic-differential-form-on-a-principal-bundle|basic differential forms on a principal bundle]]. Concretely:

1. **Horizontality:** for every fundamental vertical vector field $X^\#$ on $P$ (see [[fiber-bundles/convention-fundamental-vector-field-x-is-defined-using-the-right-action|fundamental vector field convention]]),
   \[
   \iota_{X^\#}\,P(\Omega)=0.
   \]
   Equivalently, $P(\Omega)$ vanishes whenever any argument is vertical, so it is a [[fiber-bundles/horizontal-differential-form-on-a-principal-bundle|horizontal form]].

2. **$G$-invariance:** for every $g\in G$,
   \[
   R_g^*\,P(\Omega)=P(\Omega),
   \]
   so it is an [[fiber-bundles/invariant-differential-form|invariant differential form]].

Therefore there exists a unique form $\alpha\in\Omega^{2k}(M)$ such that $\pi^*\alpha=P(\Omega)$; this $\alpha$ is the Chern–Weil form on the base.

## Examples
1. **Abelian case: $U(1)$**
   For $G=U(1)$, the adjoint action is trivial, and $P$ can be taken to be the identity on $\mathfrak{u}(1)\cong i\mathbb{R}$. Then the Chern–Weil form is simply $P(\Omega)=\Omega$, and the lemma says $\Omega$ is basic, hence descends to a 2-form on $M$. This is exactly what happens in the [[fiber-bundles/dirac-monopole-connection-on-the-hopf-bundle|Dirac monopole]] example on the Hopf bundle.

2. **Unitary bundles**
   For a principal $U(n)$-bundle, take $P(X)=\mathrm{tr}(X)$ or $P(X)=\mathrm{tr}(X^k)$. The lemma guarantees that $\mathrm{tr}(\Omega)$ and $\mathrm{tr}(\Omega^k)$ are basic forms on $P$, so they correspond to well-defined differential forms on $M$ representing Chern classes (see [[fiber-bundles/chern-class|Chern class]]).

3. **Orthogonal bundles and Pontryagin forms**
   For $G=SO(n)$, invariant polynomials such as $P(X)=\mathrm{tr}(X^2)$ produce Pontryagin forms (see [[fiber-bundles/pontryagin-class|Pontryagin class]]). The lemma ensures these forms are basic and hence live on the base manifold, not just on the total space of frames.
