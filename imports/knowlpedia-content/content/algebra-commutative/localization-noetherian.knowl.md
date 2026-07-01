+++
id = "algebra-commutative/localization-noetherian"
title = "Localization preserves Noetherian rings"
kind = "knowl"
summary = "If a ring is Noetherian, then any localization at a multiplicative set is again Noetherian."
aliases = ["localization-noetherian", "Localization preserves Noetherian rings"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/localization-noetherian.md"
+++

Localization is a “local” operation, but it does not destroy finiteness properties: in particular, Noetherianity survives. This is indispensable when passing from global to local statements, for example by [[algebra-commutative/localization-at-prime|localizing at a prime]].

## Theorem

Let $R$ be a [[algebra-commutative/noetherian-ring|Noetherian ring]] and let $S$ be a [[algebra-commutative/multiplicative-set|multiplicative set]] in $R$. Then the localized ring
\[
S^{-1}R
\]
is Noetherian.

More generally, if $M$ is a Noetherian $R$-module, then $S^{-1}M$ is a Noetherian $S^{-1}R$-module.

This result is often paired with [[algebra-commutative/localization-exact|exactness of localization]], since many Noetherian arguments proceed by short exact sequences and localization.

## Examples

1. **Localizing $\mathbb Z$.**
   The ring $\mathbb Z$ is Noetherian, so any localization is Noetherian. For instance, the local ring $\mathbb Z_{(p)}$ (obtained by [[algebra-commutative/localization-at-prime|localizing at the prime $(p)$]]) is Noetherian.

2. **Localizing a polynomial ring.**
   Let $R=k[x,y]$, which is Noetherian. Localizing at $S=\{1,x,x^2,\dots\}$ gives $R_x=k[x,y]_x$, which is still Noetherian. Geometrically, this corresponds to restricting from affine space to the principal open set where $x\neq 0$ in [[algebra-commutative/prime-spectrum|Spec]] with its [[algebra-commutative/zariski-topology|Zariski topology]].

3. **Non-Noetherian rings can stay non-Noetherian after localization.**
   Let $R=k[x_1,x_2,\dots]$, which is not Noetherian. Localizing at many natural multiplicative sets (for example, inverting one variable) typically does not repair this: $R_{x_1}$ still contains an infinite strictly ascending chain of ideals $(x_2)\subsetneq(x_2,x_3)\subsetneq\cdots$. This illustrates that the theorem is one-way: localization preserves Noetherianity, but does not create it.

When applying the theorem in practice, a common pattern is: start with a Noetherian ring, localize at a prime to get a Noetherian [[algebra-commutative/local-ring|local ring]], then analyze invariants (dimension, depth, primary decomposition, and so on) locally.
