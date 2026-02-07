---
title: "Difference of two principal connections is tensorial"
description: "The difference of two principal connection 1-forms is a tensorial one-form with values in the Lie algebra."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with Lie group $G$ and Lie algebra $\mathfrak g$ (see {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra of a Lie group" section="lie-groups">}}). Let $\omega,\omega'\in \Omega^1(P;\mathfrak g)$ be connection $1$-forms of two {{< knowl id="principal-connection" text="principal connections" >}} (see {{< knowl id="connection-1-form-on-a-principal-bundle" text="connection 1-form on a principal bundle" >}}).

Define their difference
\[
a := \omega' - \omega \in \Omega^1(P;\mathfrak g).
\]

## Lemma
The $1$-form $a$ is **tensorial of type $\mathrm{Ad}$**, meaning:
1. (**Horizontal**) $a_p(v)=0$ for every vertical vector $v\in V_pP$ (equivalently $\iota_{X^\#}a=0$ for all fundamental vertical fields $X^\#$).
2. (**$\mathrm{Ad}$-equivariant**) $(R_g)^*a = \mathrm{Ad}(g^{-1})\,a$ for all $g\in G$ (see {{< knowl id="adjoint-action-of-a-lie-group" text="adjoint action" section="lie-groups">}}).

Consequently, $a$ descends to a well-defined $1$-form on the base with values in the adjoint bundle:
\[
a \ \longleftrightarrow\ \widetilde a \in \Omega^1\!\big(M;\mathrm{ad}(P)\big),
\]
where $\mathrm{ad}(P)=P\times_{\mathrm{Ad}}\mathfrak g$ is the {{< knowl id="adjoint-bundle-p-g-g-with-conjugation-action" text="adjoint bundle" >}} (compare {{< knowl id="construction-adjoint-lie-algebra-bundle-ad" text="construction of the adjoint Lie algebra bundle" >}} and {{< knowl id="section-of-ad" text="sections of ad(P)" >}}).

This tensoriality fact underlies many standard constructions, including transgression formulas (see {{< knowl id="transgression-form" text="transgression forms" >}}) and the description of the affine space of connections (compare {{< knowl id="bundle-of-connections" text="bundle of connections" >}}).

## Examples
1. **Trivial bundle: local gauge potentials differ by a basic form.**  
   On the trivial principal bundle $P=M\times G$ (see {{< knowl id="trivial-principal-bundle-mgm" text="trivial principal bundle" >}}), a principal connection corresponds to a $\mathfrak g$-valued $1$-form $A\in\Omega^1(M;\mathfrak g)$ via a global section. If $\omega,\omega'$ correspond to $A,A'$, then
   \[
   a=\omega'-\omega \quad \text{corresponds to} \quad A'-A\in\Omega^1(M;\mathfrak g),
   \]
   which is a genuine $1$-form on $M$ (hence automatically horizontal/basic after pullback to $P$).

2. **U(1) bundles: two connections differ by an ordinary real 1-form.**  
   For $G=U(1)$, the adjoint action is trivial, so $\mathrm{ad}(P)\cong M\times i\mathbb R$. Thus the difference of two $U(1)$-connections is simply an $i\mathbb R$-valued $1$-form on $M$. Concretely, if $A$ and $A'$ are local connection $1$-forms (see {{< knowl id="local-connection-1-form" text="local connection 1-form" >}}), then $A'-A$ patches globally as an $i\mathbb R$-valued form.

3. **Frame bundle: change of linear connection is tensorial.**  
   Let $E\to M$ be a rank-$n$ vector bundle and let $P=\mathrm{Fr}(E)$ be its frame bundle (see {{< knowl id="frame-bundle-frame-bundle-of-a-rank-n-vector-bundle" text="frame bundle of a vector bundle" >}}). Two vector bundle connections on $E$ correspond to two principal connections on $P$ (compare {{< knowl id="tfae-vector-bundle-connections-via-frame-bundles-rank-n-vector-bundle-em" text="connections via frame bundles" >}}). Their difference is a tensorial $1$-form on $P$, which corresponds to a $1$-form on $M$ with values in $\mathrm{End}(E)$, i.e. the usual “difference tensor” between linear connections.
