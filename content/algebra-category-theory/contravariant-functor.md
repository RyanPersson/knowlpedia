---
title: "Contravariant functor"
description: "A functor that reverses the direction of morphisms; equivalently a functor C^op → D."
---

Let \(\mathcal C,\mathcal D\) be {{< knowl id="category" text="categories" >}}.

A **contravariant functor** \(F:\mathcal C\to\mathcal D\) consists of:
- an assignment on {{< knowl id="object" text="objects" >}} \(X\mapsto F(X)\),
- for every {{< knowl id="morphism" text="morphism" >}} \(f:X\to Y\) in \(\mathcal C\), a morphism
  \[
  F(f):F(Y)\to F(X)
  \]
  in \(\mathcal D\),

such that:
1. (**Identities**) \(F(\mathrm{id}_X)=\mathrm{id}_{F(X)}\) for every \(X\) (see {{< knowl id="identity-morphism" text="identity morphism" >}}),
2. (**Reversed composition**) for composable \(X\xrightarrow{f}Y\xrightarrow{g}Z\),
   \[
   F(g\circ f)=F(f)\circ F(g)
   \]
   (see {{< knowl id="composition-category" text="composition" >}}).

Equivalently, a contravariant functor \(F:\mathcal C\to\mathcal D\) is the same thing as an ordinary (covariant) {{< knowl id="functor" text="functor" >}}
\[
\mathcal C^{\mathrm{op}}\longrightarrow \mathcal D,
\]
where \(\mathcal C^{\mathrm{op}}\) is the {{< knowl id="opposite-category" text="opposite category" >}} of \(\mathcal C\).

## Examples
1. **Inverse-image on power sets (Set)**.  
   Let \(\mathbf{Set}\) be the category of {{< knowl id="set" section="shared-foundations" text="sets" >}} and {{< knowl id="function" section="shared-foundations" text="functions" >}}.  
   Define \(F:\mathbf{Set}^{\mathrm{op}}\to \mathbf{Set}\) by
   - \(F(X)=\mathcal P(X)\) (the set of subsets of \(X\)),
   - for \(f:X\to Y\), \(F(f)=f^{-1}:\mathcal P(Y)\to\mathcal P(X)\), the {{< knowl id="preimage" section="shared-foundations" text="preimage" >}} map.  
   Then \(f^{-1}(\mathrm{id})=\mathrm{id}\) and \((g\circ f)^{-1}=f^{-1}\circ g^{-1}\), so this is contravariant.

2. **Representable hom-functor** \(\mathrm{Hom}_{\mathcal C}(-,A)\).  
   Fix an object \(A\in\mathcal C\). The assignment
   \[
   X\longmapsto \mathrm{Hom}_{\mathcal C}(X,A)
   \]
   extends to a contravariant functor \(\mathcal C\to\mathbf{Set}\) (equivalently \(\mathcal C^{\mathrm{op}}\to\mathbf{Set}\)) by sending \(f:X\to Y\) to precomposition:
   \[
   \mathrm{Hom}_{\mathcal C}(Y,A)\to \mathrm{Hom}_{\mathcal C}(X,A),\quad (h:Y\to A)\mapsto h\circ f.
   \]
   This is a basic instance of a {{< knowl id="representable-functor" text="representable functor" >}}.

3. **Linear dual (Vect\(_k\) or \(R\)-Mod)**.  
   In the category of vector spaces over a field \(k\) (or modules over a ring), define
   \[
   V\mapsto V^\ast=\mathrm{Hom}_k(V,k).
   \]
   A linear map \(f:V\to W\) induces \(f^\ast:W^\ast\to V^\ast\) by \(f^\ast(\varphi)=\varphi\circ f\).  
   The direction reverses, and \((g\circ f)^\ast=f^\ast\circ g^\ast\), so \((-)^\ast\) is contravariant.
