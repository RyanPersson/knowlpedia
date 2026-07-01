+++
id = "fiber-bundles/closed-differential-form"
title = "Closed differential form"
kind = "knowl"
summary = "A differential form with vanishing exterior derivative: =0."
aliases = ["closed-differential-form", "Closed differential form"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/closed-differential-form.md"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]] and let \(\omega\) be a [[fiber-bundles/differential-k-form|differential \\(k\\)-form]] on \(M\). The notion of “closedness” is defined using the [[fiber-bundles/exterior-derivative|exterior derivative]].

A form \(\omega\in\Omega^k(M)\) is **closed** if
\[
d\omega = 0.
\]
The vector space of closed \(k\)-forms is
\[
Z^k(M) \coloneqq \ker\!\bigl(d:\Omega^k(M)\to\Omega^{k+1}(M)\bigr).
\]

Closed forms are the “cocycles” in the complex \((\Omega^\ast(M),d)\); passing to cohomology by quotienting out [[fiber-bundles/exact-differential-form|exact forms]] yields the [[fiber-bundles/de-rham-cohomology-group|de Rham cohomology groups]].

## Basic facts
- Every [[fiber-bundles/exact-differential-form|exact form]] is closed: if \(\omega=d\eta\), then \(d\omega=d(d\eta)=0\) because \(d^2=0\).
- Closedness is preserved by pullback: if \(F:M\to N\) is a [[fiber-bundles/smooth-map|smooth map]] and \(\omega\) is closed on \(N\), then the [[fiber-bundles/pullback-of-differential-forms|pullback]] \(F^*\omega\) is closed on \(M\).

## Examples
1. **Constant 1-forms on \(\mathbb{R}^n\).**
   In standard coordinates, each \(dx^i\) is closed because \(d(dx^i)=0\). Any constant-coefficient 1-form \(\sum_i a_i\,dx^i\) is also closed.

2. **Standard symplectic form on \(\mathbb{R}^{2n}\).**
   With coordinates \((x_1,y_1,\dots,x_n,y_n)\), the 2-form
   \[
   \omega_0=\sum_{i=1}^n dx_i\wedge dy_i
   \]
   is closed since \(d(dx_i)=d(dy_i)=0\) and \(d\) satisfies the graded Leibniz rule.

3. **A closed but not exact 1-form on \(\mathbb{R}^2\setminus\{0\}\).**
   On \(U=\mathbb{R}^2\setminus\{0\}\) with coordinates \((x,y)\), the 1-form
   \[
   \omega=\frac{-y\,dx + x\,dy}{x^2+y^2}
   \]
   is closed (it is the “angular” form). It is not exact on \(U\), which can be detected by integrating \(\omega\) around the unit circle: the integral is nonzero, so \(\omega\) cannot be \(d\eta\) globally on \(U\).
