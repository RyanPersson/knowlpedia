+++
id = "algebra-category-theory/subcategory"
title = "Subcategory"
kind = "knowl"
summary = "A category obtained by restricting the objects and morphisms of a given category."
aliases = ["subcategory"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/subcategory.md"
+++

Let \(\mathcal C\) be a [[algebra-category-theory/category|category]].

A **subcategory** \(\mathcal D\) of \(\mathcal C\) consists of:
- a collection of [[algebra-category-theory/object|objects]] \(\mathrm{Ob}(\mathcal D)\subseteq \mathrm{Ob}(\mathcal C)\),
- for every \(A,B\in \mathrm{Ob}(\mathcal D)\), a subset of [[algebra-category-theory/morphism|morphisms]]
  \[
  \mathrm{Hom}_{\mathcal D}(A,B)\subseteq \mathrm{Hom}_{\mathcal C}(A,B),
  \]
such that:
1. (**identities**) for each \(A\in\mathrm{Ob}(\mathcal D)\), the [[algebra-category-theory/identity-morphism|identity morphism]] \(\mathrm{id}_A\) lies in \(\mathrm{Hom}_{\mathcal D}(A,A)\);
2. (**closure under composition**) if \(f\in\mathrm{Hom}_{\mathcal D}(A,B)\) and \(g\in\mathrm{Hom}_{\mathcal D}(B,C)\), then their [[algebra-category-theory/composition-category|composite]] \(g\circ f\) (computed in \(\mathcal C\)) lies in \(\mathrm{Hom}_{\mathcal D}(A,C)\).

In this situation, \(\mathcal D\) is itself a [[algebra-category-theory/category|category]], with composition and identities inherited from \(\mathcal C\).

A particularly important case is a [[algebra-category-theory/full-subcategory|full subcategory]], where \(\mathcal D\) contains *all* morphisms in \(\mathcal C\) between its objects.

## Examples
1. **Injective maps inside \(\mathbf{Set}\):** Let \(\mathcal C=\mathbf{Set}\).
   Define \(\mathcal D\) to have the same objects as \(\mathbf{Set}\), but only [[shared-foundations/injective-function|injective functions]] as morphisms.
   This is a subcategory of \(\mathbf{Set}\) (closed under composition and contains identities), but it is **not** full.

2. **\(\mathbf{Ab}\) inside \(\mathbf{Grp}\):** The category \(\mathbf{Ab}\) of abelian groups is a subcategory of \(\mathbf{Grp}\) by restricting to those objects that happen to be abelian.
   Moreover, it is a [[algebra-category-theory/full-subcategory|full subcategory]]: between two abelian groups, a group homomorphism is the same morphism whether viewed in \(\mathbf{Ab}\) or in \(\mathbf{Grp}\).

3. **Hausdorff spaces inside \(\mathbf{Top}\):** Let \(\mathcal D\) be the category whose objects are Hausdorff spaces and whose morphisms are continuous maps.
   Then \(\mathcal D\) is a subcategory of \(\mathbf{Top}\), and in fact it is full (all continuous maps between Hausdorff spaces are included).
