+++
id = "algebra-category-theory/abelian-category"
title = "Abelian category"
kind = "knowl"
summary = "An additive category with kernels and cokernels where exactness behaves like in module categories."
aliases = ["abelian-category", "Abelian category"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/abelian-category.md"
+++

An **abelian category** is a [[algebra-category-theory/category|category]] \(\mathcal A\) in which one can do “linear algebra + exact sequences” abstractly.


A category \(\mathcal A\) is **abelian** if:

1. \(\mathcal A\) is an [[algebra-category-theory/additive-category|additive category]] (in particular, hom-sets are abelian groups and finite biproducts exist);
2. every morphism has a [[algebra-category-theory/kernel-categorical|kernel]] and a [[algebra-category-theory/cokernel-categorical|cokernel]];
3. every [[algebra-category-theory/monomorphism-category|monomorphism]] is a kernel of its cokernel, and every [[algebra-category-theory/epimorphism-category|epimorphism]] is a cokernel of its kernel.

Equivalently, \(\mathcal A\) satisfies the standard **[[algebra-category-theory/abelian-category-axioms|abelian category axioms]]**.

## Consequences (often used as “working facts”)

In an abelian category:

- one can define [[algebra-category-theory/exact-sequence-categorical|exact sequences]] and do homological algebra;
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
