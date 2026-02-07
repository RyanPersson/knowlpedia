---
title: "Subcategory"
description: "A category obtained by restricting the objects and morphisms of a given category."
---

Let \(\mathcal C\) be a {{< knowl id="category" text="category" >}}.

A **subcategory** \(\mathcal D\) of \(\mathcal C\) consists of:
- a collection of {{< knowl id="object" text="objects" >}} \(\mathrm{Ob}(\mathcal D)\subseteq \mathrm{Ob}(\mathcal C)\),
- for every \(A,B\in \mathrm{Ob}(\mathcal D)\), a subset of {{< knowl id="morphism" text="morphisms" >}}
  \[
  \mathrm{Hom}_{\mathcal D}(A,B)\subseteq \mathrm{Hom}_{\mathcal C}(A,B),
  \]
such that:
1. (**identities**) for each \(A\in\mathrm{Ob}(\mathcal D)\), the {{< knowl id="identity-morphism" text="identity morphism" >}} \(\mathrm{id}_A\) lies in \(\mathrm{Hom}_{\mathcal D}(A,A)\);
2. (**closure under composition**) if \(f\in\mathrm{Hom}_{\mathcal D}(A,B)\) and \(g\in\mathrm{Hom}_{\mathcal D}(B,C)\), then their {{< knowl id="composition-category" text="composite" >}} \(g\circ f\) (computed in \(\mathcal C\)) lies in \(\mathrm{Hom}_{\mathcal D}(A,C)\).

In this situation, \(\mathcal D\) is itself a {{< knowl id="category" text="category" >}}, with composition and identities inherited from \(\mathcal C\).

A particularly important case is a {{< knowl id="full-subcategory" text="full subcategory" >}}, where \(\mathcal D\) contains *all* morphisms in \(\mathcal C\) between its objects.

## Examples
1. **Injective maps inside \(\mathbf{Set}\):** Let \(\mathcal C=\mathbf{Set}\).  
   Define \(\mathcal D\) to have the same objects as \(\mathbf{Set}\), but only {{< knowl id="injective-function" section="shared-foundations" text="injective functions" >}} as morphisms.  
   This is a subcategory of \(\mathbf{Set}\) (closed under composition and contains identities), but it is **not** full.

2. **\(\mathbf{Ab}\) inside \(\mathbf{Grp}\):** The category \(\mathbf{Ab}\) of abelian groups is a subcategory of \(\mathbf{Grp}\) by restricting to those objects that happen to be abelian.  
   Moreover, it is a {{< knowl id="full-subcategory" text="full subcategory" >}}: between two abelian groups, a group homomorphism is the same morphism whether viewed in \(\mathbf{Ab}\) or in \(\mathbf{Grp}\).

3. **Hausdorff spaces inside \(\mathbf{Top}\):** Let \(\mathcal D\) be the category whose objects are Hausdorff spaces and whose morphisms are continuous maps.  
   Then \(\mathcal D\) is a subcategory of \(\mathbf{Top}\), and in fact it is full (all continuous maps between Hausdorff spaces are included).
