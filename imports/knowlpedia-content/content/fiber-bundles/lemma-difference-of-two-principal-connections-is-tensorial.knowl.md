+++
id = "fiber-bundles/lemma-difference-of-two-principal-connections-is-tensorial"
title = "Difference of two principal connections is tensorial"
kind = "knowl"
summary = "The difference of two principal connection 1-forms is a tensorial one-form with values in the Lie algebra."
aliases = ["lemma-difference-of-two-principal-connections-is-tensorial", "Difference of two principal connections is tensorial"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/lemma-difference-of-two-principal-connections-is-tensorial.md"
+++

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with Lie group $G$ and Lie algebra $\mathfrak g$ (see [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra of a Lie group]]). Let $\omega,\omega'\in \Omega^1(P;\mathfrak g)$ be connection $1$-forms of two [[fiber-bundles/principal-connection|principal connections]] (see [[fiber-bundles/connection-1-form-on-a-principal-bundle|connection 1-form on a principal bundle]]).

Define their difference
\[
a := \omega' - \omega \in \Omega^1(P;\mathfrak g).
\]

## Lemma
The $1$-form $a$ is **tensorial of type $\mathrm{Ad}$**, meaning:
1. (**Horizontal**) $a_p(v)=0$ for every vertical vector $v\in V_pP$ (equivalently $\iota_{X^\#}a=0$ for all fundamental vertical fields $X^\#$).
2. (**$\mathrm{Ad}$-equivariant**) $(R_g)^*a = \mathrm{Ad}(g^{-1})\,a$ for all $g\in G$ (see [[lie-groups/adjoint-action-of-a-lie-group|adjoint action]]).

Consequently, $a$ descends to a well-defined $1$-form on the base with values in the adjoint bundle:
\[
a \ \longleftrightarrow\ \widetilde a \in \Omega^1\!\big(M;\mathrm{ad}(P)\big),
\]
where $\mathrm{ad}(P)=P\times_{\mathrm{Ad}}\mathfrak g$ is the [[fiber-bundles/adjoint-bundle-p-g-g-with-conjugation-action|adjoint bundle]] (compare [[fiber-bundles/construction-adjoint-lie-algebra-bundle-ad|construction of the adjoint Lie algebra bundle]] and [[fiber-bundles/section-of-ad|sections of ad(P)]]).

This tensoriality fact underlies many standard constructions, including transgression formulas (see [[fiber-bundles/transgression-form|transgression forms]]) and the description of the affine space of connections (compare [[fiber-bundles/bundle-of-connections|bundle of connections]]).

## Examples
1. **Trivial bundle: local gauge potentials differ by a basic form.**
   On the trivial principal bundle $P=M\times G$ (see [[fiber-bundles/trivial-principal-bundle-mgm|trivial principal bundle]]), a principal connection corresponds to a $\mathfrak g$-valued $1$-form $A\in\Omega^1(M;\mathfrak g)$ via a global section. If $\omega,\omega'$ correspond to $A,A'$, then
   \[
   a=\omega'-\omega \quad \text{corresponds to} \quad A'-A\in\Omega^1(M;\mathfrak g),
   \]
   which is a genuine $1$-form on $M$ (hence automatically horizontal/basic after pullback to $P$).

2. **U(1) bundles: two connections differ by an ordinary real 1-form.**
   For $G=U(1)$, the adjoint action is trivial, so $\mathrm{ad}(P)\cong M\times i\mathbb R$. Thus the difference of two $U(1)$-connections is simply an $i\mathbb R$-valued $1$-form on $M$. Concretely, if $A$ and $A'$ are local connection $1$-forms (see [[fiber-bundles/local-connection-1-form|local connection 1-form]]), then $A'-A$ patches globally as an $i\mathbb R$-valued form.

3. **Frame bundle: change of linear connection is tensorial.**
   Let $E\to M$ be a rank-$n$ vector bundle and let $P=\mathrm{Fr}(E)$ be its frame bundle (see [[fiber-bundles/frame-bundle-frame-bundle-of-a-rank-n-vector-bundle|frame bundle of a vector bundle]]). Two vector bundle connections on $E$ correspond to two principal connections on $P$ (compare [[fiber-bundles/tfae-vector-bundle-connections-via-frame-bundles-rank-n-vector-bundle-em|connections via frame bundles]]). Their difference is a tensorial $1$-form on $P$, which corresponds to a $1$-form on $M$ with values in $\mathrm{End}(E)$, i.e. the usual “difference tensor” between linear connections.
