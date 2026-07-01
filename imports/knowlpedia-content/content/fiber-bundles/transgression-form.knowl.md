+++
id = "fiber-bundles/transgression-form"
title = "Transgression form"
kind = "knowl"
summary = "A differential form whose exterior derivative is the difference of two characteristic forms coming from different connections"
aliases = ["transgression-form", "Transgression form"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/transgression-form.md"
+++

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with Lie algebra $\mathfrak g$, and let $\omega_0,\omega_1$ be two [[fiber-bundles/principal-connection|principal connections]] on $P$ with corresponding [[fiber-bundles/curvature-2-form-of-a-principal-connection|curvature 2-forms]] $\Omega_0,\Omega_1\in\Omega^2(P;\mathfrak g)$.

Fix an $\operatorname{Ad}$-invariant symmetric multilinear map
\[
p:\underbrace{\mathfrak g\times\cdots\times\mathfrak g}_{n\ \text{factors}}\longrightarrow \mathbb R,
\]
i.e. an invariant polynomial datum as used to build a [[fiber-bundles/chernweil-form|Chern--Weil form]]. Define the affine path of connections
\[
\omega_t := \omega_0 + t(\omega_1-\omega_0),\qquad t\in[0,1],
\]
and set $\eta:=\omega_1-\omega_0\in\Omega^1(P;\mathfrak g)$. (By [[fiber-bundles/lemma-difference-of-two-principal-connections-is-tensorial|tensoriality of the difference of two connections]], $\eta$ is horizontal and $\operatorname{Ad}$-equivariant.) Let $\Omega_t$ be the curvature of $\omega_t$.

## Definition (transgression form)
The **transgression form** associated to $p$ and the pair $(\omega_0,\omega_1)$ is the $(2n-1)$-form $T_p(\omega_0,\omega_1)$ on $M$ uniquely characterized by the requirement that its pullback to $P$ is
\[
\pi^*T_p(\omega_0,\omega_1)
\;=\;
n\int_0^1 p\!\big(\eta\wedge \Omega_t^{\,n-1}\big)\,dt,
\]
where $\Omega_t^{\,n-1}$ denotes the wedge product of $(n-1)$ copies of $\Omega_t$ and $p(\eta\wedge \Omega_t^{n-1})$ means the $\mathbb R$-valued form obtained by feeding the $\mathfrak g$-valued factors into $p$.

Because the integrand is basic (horizontal and $G$-invariant), $T_p(\omega_0,\omega_1)$ is well-defined on the base. It is designed so that the difference of the corresponding Chern--Weil forms is exact:
\[
d\,T_p(\omega_0,\omega_1)=p(\Omega_1)-p(\Omega_0)
\quad\text{on }M,
\]
which is the content of the [[fiber-bundles/transgression-theorem-p-p-is-exact|transgression theorem]]. Specializing $\omega_0$ to a reference connection produces the usual [[fiber-bundles/chernsimons-form|Chern--Simons transgression form]].

## Examples
1. **Degree 1 (linear invariant polynomial).**
   For $n=1$ and an $\operatorname{Ad}$-invariant linear functional $p:\mathfrak g\to\mathbb R$, the formula reduces to
   \[
   T_p(\omega_0,\omega_1)=p(\omega_1-\omega_0),
   \qquad
   dT_p = p(\Omega_1)-p(\Omega_0).
   \]

2. **Degree 2 on a trivial bundle (the usual Chern--Simons 3-form).**
   On a trivial bundle and in a global gauge, a connection is represented by a $\mathfrak g$-valued 1-form $A$ (see [[fiber-bundles/local-connection-1-form|local connection 1-form]]). For $p(X,Y)=\operatorname{tr}(XY)$ (degree $2$), taking $\omega_0=0$ gives the standard 3-form
   \[
   \operatorname{CS}(A)=\operatorname{tr}\!\Big(A\wedge dA+\frac{2}{3}A\wedge A\wedge A\Big),
   \]
   with $d\,\operatorname{CS}(A)=\operatorname{tr}(F\wedge F)$, where $F=dA+A\wedge A$ is the [[fiber-bundles/local-curvature-formula-f-da-aa|local curvature]].

3. **Abelian case.**
   If $G$ is abelian (e.g. $U(1)$), then $\operatorname{Ad}$ is trivial and $A\wedge A=0$. For a degree 1 invariant polynomial, the transgression between two $U(1)$-connections $A_0,A_1$ is simply $T(A_0,A_1)=A_1-A_0$, and $dT = dA_1-dA_0$.
