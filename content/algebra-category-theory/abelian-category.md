---
title: "Abelian category"
description: "An additive category with kernels and cokernels where exactness behaves like in module categories."
---

An **abelian category** is a {{< knowl id="category" text="category" >}} \(\mathcal A\) in which one can do “linear algebra + exact sequences” abstractly.


A category \(\mathcal A\) is **abelian** if:

1. \(\mathcal A\) is an {{< knowl id="additive-category" text="additive category" >}} (in particular, hom-sets are abelian groups and finite biproducts exist);
2. every morphism has a {{< knowl id="kernel-categorical" text="kernel" >}} and a {{< knowl id="cokernel-categorical" text="cokernel" >}};
3. every {{< knowl id="monomorphism-category" text="monomorphism" >}} is a kernel of its cokernel, and every {{< knowl id="epimorphism-category" text="epimorphism" >}} is a cokernel of its kernel.

Equivalently, \(\mathcal A\) satisfies the standard **{{< knowl id="abelian-category-axioms" text="abelian category axioms" >}}**.

## Consequences (often used as “working facts”)

In an abelian category:

- one can define {{< knowl id="exact-sequence-categorical" text="exact sequences" >}} and do homological algebra;
- every morphism \(f\) admits an “image–coimage” comparison, and the canonical map \(\mathrm{coim}(f)\to \mathrm{im}(f)\) is an isomorphism;
- kernels are monomorphisms and cokernels are epimorphisms, mirroring the familiar situation in \(\mathbf{Ab}\) and \(R\)-modules.

## Examples

1. **\(\mathbf{Ab}\).** The category of abelian groups is abelian.

2. **\(R\text{-}\mathbf{Mod}\).** The category of left modules over a ring \(R\) is abelian.

3. **\(\mathrm{Ch}(R)\).** The category of chain complexes of \(R\)-modules is abelian (kernels and cokernels are computed degreewise).

## Non-examples (useful to remember)

- **\(\mathbf{Set}\)** is not abelian (not additive).
- **\(\mathbf{Grp}\)** is not abelian (kernels exist, but cokernels and exactness do not satisfy the abelian axioms).
- **\(\mathbf{Top}\)** is not abelian (again, not additive).
