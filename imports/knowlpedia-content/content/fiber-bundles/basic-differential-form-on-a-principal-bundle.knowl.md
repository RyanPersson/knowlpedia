+++
id = "fiber-bundles/basic-differential-form-on-a-principal-bundle"
title = "Basic differential form on a principal bundle"
kind = "knowl"
summary = "A differential form on a principal bundle that is horizontal and invariant, hence the pullback of a unique form on the base."
aliases = ["basic-differential-form-on-a-principal-bundle", "Basic differential form on a principal bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/basic-differential-form-on-a-principal-bundle.md"
+++

Let $\pi:P\to M$ be a principal $G$-bundle with right action $R_g$.

A differential form $\omega\in\Omega^k(P)$ is **basic** if it is both:

1. [[fiber-bundles/horizontal-differential-form-on-a-principal-bundle|horizontal]], and
2. [[fiber-bundles/invariant-differential-form|G-invariant]], meaning $(R_g)^*\omega=\omega$ for all $g\in G$.

## Theorem (descent to the base)
A form $\omega\in\Omega^k(P)$ is basic if and only if there exists a unique $\eta\in\Omega^k(M)$ such that
\[
\pi^*\eta = \omega.
\]
In particular, the pullback map $\pi^*:\Omega^k(M)\to \Omega^k(P)$ identifies $\Omega^k(M)$ with the subspace of basic forms on $P$, and [[fiber-bundles/exterior-derivative|d]] preserves basic forms.

## Examples
1. **Pullbacks are basic.** For any $\eta\in\Omega^k(M)$, the form $\pi^*\eta$ is basic by construction.
2. **Trivial bundle.** For $P=M\times G$, a form is basic exactly when it has no components along the $G$-factor and is independent of the $G$-coordinate; equivalently, it is pulled back from $M$.
3. **Hopf fibration.** In the Hopf bundle $S^3\to S^2$, the pullback of the area form on $S^2$ is a basic 2-form on $S^3$.
