---
title: "Axioms for an abelian category"
description: "A convenient list of axioms characterizing abelian categories."
---

An **{{< knowl id="abelian-category" text="abelian category" >}}** is most often defined as an {{< knowl id="additive-category" text="additive category" >}} in which kernels/cokernels exist and monomorphisms/epimorphisms are “normal.” One standard axiom list is:

## Axiom list

Let \(\mathcal A\) be a {{< knowl id="category" text="category" >}}.

1. **Preadditivity.** For all objects \(A,B\), the hom-set \(\mathrm{Hom}_{\mathcal A}(A,B)\) is an abelian group, and composition is bilinear in each variable.

2. **Zero object.** \(\mathcal A\) has a zero object \(0\) (both initial and terminal). Equivalently, for all \(A,B\) there are distinguished zero morphisms \(0_{A,B}:A\to B\).

3. **Finite biproducts.** \(\mathcal A\) has finite {{< knowl id="categorical-product" text="products" >}} and finite {{< knowl id="coproduct" text="coproducts" >}}, and for each finite family they coincide (so one can write \(A\oplus B\) as both product and coproduct).

4. **Kernels and cokernels.** Every morphism \(f:A\to B\) has a {{< knowl id="kernel-categorical" text="kernel" >}} \(\ker(f)\to A\) and a {{< knowl id="cokernel-categorical" text="cokernel" >}} \(B\to \mathrm{coker}(f)\).

5. **Normal monos.** Every {{< knowl id="monomorphism-category" text="monomorphism" >}} \(m:A\to B\) is a kernel of some morphism; equivalently,
   \[
   m \cong \ker(\mathrm{coker}(m)).
   \]

6. **Normal epis.** Every {{< knowl id="epimorphism-category" text="epimorphism" >}} \(e:A\to B\) is a cokernel of some morphism; equivalently,
   \[
   e \cong \mathrm{coker}(\ker(e)).
   \]

A category satisfying (1)–(6) is abelian. Conversely, any abelian category satisfies these properties.

## Why these axioms matter

They guarantee that exactness behaves “like modules,” so one can define and use {{< knowl id="exact-sequence-categorical" text="exact sequences" >}}, images/coimages, and homological algebra in \(\mathcal A\).

## Examples and non-examples

- **Example: \(\mathbf{Ab}\).** The category of abelian groups is abelian: kernels/cokernels are the usual subgroup kernel and quotient cokernel.

- **Example: \(R\text{-}\mathbf{Mod}\).** The category of left \(R\)-modules is abelian for any ring \(R\).

- **Example: \(\mathrm{Ch}(R)\).** The category of chain complexes of \(R\)-modules is abelian (kernels/cokernels are taken degreewise).

- **Non-example: \(\mathbf{Set}\).** Not additive: \(\mathrm{Hom}(A,B)\) has no natural abelian group structure in general.

- **Non-example: \(\mathbf{Grp}\).** Not abelian: cokernels exist, but kernels/cokernels do not interact in the way required by (5)–(6).
