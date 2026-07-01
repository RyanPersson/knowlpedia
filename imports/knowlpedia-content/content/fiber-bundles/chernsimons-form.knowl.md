+++
id = "fiber-bundles/chernsimons-form"
title = "Chern–Simons form"
kind = "knowl"
summary = "A differential form whose exterior derivative is the difference of two Chern Weil forms."
aliases = ["chernsimons-form", "Chern–Simons form"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/chernsimons-form.md"
+++

Chern–Simons forms are transgression forms that measure how [[fiber-bundles/chernweil-form|Chern–Weil forms]] change when the connection changes. They are a central tool in geometry and gauge theory, and they are instances of the general [[fiber-bundles/transgression-form|transgression form]] mechanism.

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]]. Let $\omega_0$ and $\omega_1$ be two [[fiber-bundles/principal-connection|principal connections]] on $P$, with curvatures $\Omega_0$ and $\Omega_1$.

Fix an $\mathrm{Ad}$-invariant symmetric polynomial $P$ of degree $k$ on $\mathfrak{g}$ (as in the definition of a [[fiber-bundles/chernweil-form|Chern–Weil form]]).

## Definition (relative Chern–Simons form)
Define a path of connections
\[
\omega_t := \omega_0 + t(\omega_1-\omega_0), \qquad t\in[0,1],
\]
and let $\Omega_t$ be its curvature. The **Chern–Simons form** associated to $P$ and the pair $(\omega_0,\omega_1)$ is the $(2k-1)$-form on $P$
\[
\mathrm{CS}_P(\omega_0,\omega_1)
:= k\int_0^1 P\!\bigl(\omega_1-\omega_0,\ \underbrace{\Omega_t,\dots,\Omega_t}_{k-1\text{ times}}\bigr)\,dt.
\]

## Fundamental transgression identity
The Chern–Simons form satisfies
\[
d\,\mathrm{CS}_P(\omega_0,\omega_1) = P(\Omega_1)-P(\Omega_0).
\]
This is a concrete case of [[fiber-bundles/transgression-theorem-p-p-is-exact|the transgression theorem]].

Because $P(\Omega_1)$ and $P(\Omega_0)$ are basic (see [[fiber-bundles/lemma-chernweil-forms-are-basic|Chern–Weil forms are basic]]), their difference descends to the base $M$, and the identity implies that the difference of the corresponding base forms is exact.

## A common special case
If one takes $\omega_0$ to be a fixed reference connection (often chosen locally or globally if available), then $\mathrm{CS}_P(\omega_0,\omega_1)$ is a primitive for the difference of Chern–Weil forms. In gauge theory language, it is a secondary characteristic form whose behavior under [[fiber-bundles/gauge-transformation|gauge transformations]] is subtle; see [[fiber-bundles/chernsimons-gauge-transformation-behavior|Chern–Simons gauge transformation behavior]].

## Examples
1. **Degree 1 (abelian case)**
   Take $G=U(1)$ and the degree-1 invariant polynomial $P(X)=\frac{i}{2\pi}X$. Then $P(\Omega)$ is (a multiple of) the curvature 2-form, and the Chern–Simons form for $(\omega_0,\omega_1)$ simplifies to a multiple of the difference of connection 1-forms:
   \[
   \mathrm{CS}_P(\omega_0,\omega_1)=\frac{i}{2\pi}\,(\omega_1-\omega_0),
   \qquad
   d\,\mathrm{CS}_P(\omega_0,\omega_1)=\frac{i}{2\pi}(\Omega_1-\Omega_0).
   \]

2. **The classical 3-dimensional Chern–Simons form**
   For a matrix Lie group (such as $SU(n)$), take $k=2$ and $P(X,Y)=\mathrm{tr}(XY)$. On a local trivialization, write the local connection 1-form as $A$ and local curvature as $F$ (compare [[fiber-bundles/local-connection-1-form|local connection 1-form]] and [[fiber-bundles/local-curvature-2-form|local curvature 2-form]]). Then a standard representative of the Chern–Simons 3-form is
   \[
   \mathrm{CS}_3(A)=\mathrm{tr}\!\Bigl(A\wedge dA+\frac{2}{3}A\wedge A\wedge A\Bigr),
   \]
   and it satisfies
   \[
   d\,\mathrm{CS}_3(A)=\mathrm{tr}(F\wedge F).
   \]
   This uses the local curvature convention fixed in [[fiber-bundles/convention-local-curvature-convention-f-da-aa|the convention F = dA + A wedge A]].

3. **Comparing two connections on the same bundle**
   If $\omega_0$ and $\omega_1$ are two different principal connections on the same principal bundle, then the transgression identity shows that the two Chern–Weil forms $P(\Omega_0)$ and $P(\Omega_1)$ represent the same de Rham cohomology class on $M$, because their difference is exact. The explicit primitive is the Chern–Simons form $\mathrm{CS}_P(\omega_0,\omega_1)$.
