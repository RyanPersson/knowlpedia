+++
id = "lie-groups/lie-algebra-homomorphism"
title = "Lie algebra homomorphism"
kind = "knowl"
summary = "A linear map between Lie algebras that preserves the Lie bracket."
aliases = ["lie-algebra-homomorphism", "Lie algebra homomorphism"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/lie-algebra-homomorphism.md"
+++

Let $\mathfrak g,\mathfrak h$ be [[lie-groups/lie-algebra|Lie algebras]] over a field $\Bbbk$ (typically $\Bbb R$ or $\Bbb C$), with [[fiber-bundles/lie-bracket|Lie brackets]] $[\ ,\ ]_{\mathfrak g}$ and $[\ ,\ ]_{\mathfrak h}$.

A **Lie algebra homomorphism** is a $\Bbbk$-linear map $\varphi:\mathfrak g\to\mathfrak h$ such that for all $X,Y\in\mathfrak g$,
$$
\varphi([X,Y]_{\mathfrak g})=[\varphi(X),\varphi(Y)]_{\mathfrak h}.
$$

Equivalently, $\varphi$ is a morphism in the category of Lie algebras: it intertwines the brackets.

## Basic consequences
- The kernel $\ker(\varphi)$ is an [[lie-groups/ideal-lie-algebra|ideal]] in $\mathfrak g$.
- The image $\operatorname{im}(\varphi)$ is a [[lie-groups/lie-subalgebra|Lie subalgebra]] of $\mathfrak h$.
- There is an induced injective homomorphism $\overline\varphi:\mathfrak g/\ker(\varphi)\to \operatorname{im}(\varphi)$, giving an isomorphism of Lie algebras
  $$
  \mathfrak g/\ker(\varphi)\cong \operatorname{im}(\varphi)
  $$
  (an instance of the first isomorphism theorem, formulated using [[lie-groups/quotient-lie-algebra|quotients of Lie algebras]]).

## Context
If $f:G\to H$ is a [[lie-groups/lie-group-homomorphism|Lie group homomorphism]], then its differential at the identity,
$df_e:\operatorname{Lie}(G)\to \operatorname{Lie}(H)$, is a Lie algebra homomorphism (see [[lie-groups/differential-is-lie-algebra-homomorphism|the differential–bracket compatibility]]). This is the bridge between global group structure and infinitesimal algebra structure.
