---
title: "Full Subcategory"
description: "A subcategory that contains every morphism of the ambient category between its objects."
---

Let \(\mathcal C\) be a {{< knowl id="category" text="category" >}} and \(\mathcal D\) a {{< knowl id="subcategory" text="subcategory" >}} of \(\mathcal C\).

The subcategory \(\mathcal D\) is **full** if for every pair of objects \(A,B\in \mathrm{Ob}(\mathcal D)\),
\[
\mathrm{Hom}_{\mathcal D}(A,B) \;=\; \mathrm{Hom}_{\mathcal C}(A,B).
\]
In words: once you decide which objects to keep, you keep **all** {{< knowl id="morphism" text="morphisms" >}} between them.

Equivalently, the inclusion \(\mathcal D\hookrightarrow \mathcal C\) is a {{< knowl id="functor" text="functor" >}} that is “full on hom-sets” (it induces surjections on each hom-set).

## Examples
1. **\(\mathbf{Ab}\subseteq \mathbf{Grp}\):** The category of abelian groups is a full subcategory of the category of all groups: between abelian groups, the morphisms are exactly the same group homomorphisms as in \(\mathbf{Grp}\).

2. **Hausdorff spaces inside \(\mathbf{Top}\):** The category of Hausdorff spaces (objects: Hausdorff spaces, morphisms: continuous maps) is a full subcategory of \(\mathbf{Top}\).

3. **Full subcategory “spanned by” chosen objects:** If \(S\subseteq \mathrm{Ob}(\mathcal C)\) is any collection of objects, there is a full subcategory \(\mathcal C|_S\) whose objects are exactly \(S\) and whose morphisms are
\[
\mathrm{Hom}_{\mathcal C|_S}(A,B)=\mathrm{Hom}_{\mathcal C}(A,B)\quad (A,B\in S).
\]
For example, inside \(\mathbf{Set}\) one can take \(S=\{\emptyset,\{*\},\{0,1\}\}\) and obtain the full subcategory on those three sets.
