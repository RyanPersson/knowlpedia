---
title: "Yoneda lemma"
description: "Natural transformations from a representable functor correspond to elements of the target functor."
---

Let \(\mathcal C\) be a {{< knowl id="category" text="category" >}} such that each hom-class \(\mathrm{Hom}_{\mathcal C}(A,B)\) is a set (i.e. \(\mathcal C\) is *locally small*). Fix an {{< knowl id="object" text="object" >}} \(A\in\mathcal C\) and a {{< knowl id="functor" text="functor" >}} \(F:\mathcal C\to \mathbf{Set}\).

Write the representable functor
\[
h^A := \mathrm{Hom}_{\mathcal C}(A,-):\mathcal C\to \mathbf{Set},
\]
which is a {{< knowl id="representable-functor" text="representable functor" >}}.

## Statement (covariant Yoneda)

There is a natural bijection
\[
\mathrm{Nat}(h^A,\,F)\;\cong\;F(A),
\]
natural in both \(A\) and \(F\), where \(\mathrm{Nat}(-,-)\) denotes the set of {{< knowl id="natural-transformation" text="natural transformations" >}}.

### Explicit correspondence

- Given \(\eta\in \mathrm{Nat}(h^A,F)\), the corresponding element of \(F(A)\) is
  \[
  \eta_A(\mathrm{id}_A)\in F(A),
  \]
  where \(\mathrm{id}_A\) is the {{< knowl id="identity-morphism" text="identity morphism" >}} of \(A\).

- Given \(x\in F(A)\), define a natural transformation \(\eta^x:h^A\Rightarrow F\) by, for each object \(X\),
  \[
  \eta^x_X:\mathrm{Hom}_{\mathcal C}(A,X)\to F(X),\quad
  f \mapsto F(f)(x).
  \]
  Naturality follows from functoriality of \(F\) and {{< knowl id="composition-category" text="composition" >}} in \(\mathcal C\).

This bijection is in fact a {{< knowl id="natural-isomorphism" text="natural isomorphism" >}} between functors in \(A\) and \(F\).

## Contravariant form

For a functor \(G:\mathcal C^{\mathrm{op}}\to \mathbf{Set}\), there is a natural bijection
\[
\mathrm{Nat}(\mathrm{Hom}_{\mathcal C}(-,A),\,G)\;\cong\;G(A).
\]
(Here \(\mathrm{Hom}_{\mathcal C}(-,A)\) is the usual contravariant representable.)

## Examples

1. **Subsets via the power set functor.** Take \(\mathcal C=\mathbf{Set}\), let \(A\) be a set, and let \(F=\mathcal P\) be the power set functor \(X\mapsto \mathcal P(X)\).
   The Yoneda lemma gives a bijection
   \[
   \mathrm{Nat}(\mathrm{Hom}(A,-),\mathcal P)\cong \mathcal P(A),
   \]
   so natural transformations correspond exactly to subsets \(S\subseteq A\).
   Concretely, \(S\subseteq A\) yields \(\eta^S_X(f)=f(S)\subseteq X\).

2. **Picking an element of a group naturally.** Take \(\mathcal C=\mathbf{Grp}\), let \(A=G\) be a group, and let \(F=U:\mathbf{Grp}\to\mathbf{Set}\) be the underlying-set functor.
   Then
   \[
   \mathrm{Nat}(\mathrm{Hom}_{\mathbf{Grp}}(G,-),U)\cong U(G),
   \]
   i.e. natural transformations correspond to elements \(g\in G\).
   The corresponding \(\eta^g_H:\mathrm{Hom}(G,H)\to U(H)\) sends a homomorphism \(\varphi:G\to H\) to \(\varphi(g)\in H\).

3. **Recovering maps into a fixed module.** Let \(\mathcal C=R\text{-}\mathbf{Mod}\) and take \(F(X)=\mathrm{Hom}_R(M,X)\) viewed as a set-valued functor (forgetting the abelian group structure).
   Yoneda yields
   \[
   \mathrm{Nat}(\mathrm{Hom}_R(A,-),\,\mathrm{Hom}_R(M,-))\cong \mathrm{Hom}_R(M,A),
   \]
   so a natural way to turn maps \(A\to X\) into maps \(M\to X\) is the same as choosing a map \(M\to A\).

