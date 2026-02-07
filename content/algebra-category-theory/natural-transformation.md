---
title: "Natural transformation"
description: "A morphism between functors given by components that commute with all structure maps."
---

Let \(\mathcal C,\mathcal D\) be {{< knowl id="category" text="categories" >}}, and let \(F,G:\mathcal C\to\mathcal D\) be {{< knowl id="functor" text="functors" >}}.

A **natural transformation** \(\eta:F\Rightarrow G\) assigns to every {{< knowl id="object" text="object" >}} \(X\in\mathcal C\) a {{< knowl id="morphism" text="morphism" >}}
\[
\eta_X:F(X)\to G(X)
\]
in \(\mathcal D\), such that for every morphism \(f:X\to Y\) in \(\mathcal C\), the **naturality condition**
\[
G(f)\circ \eta_X \;=\; \eta_Y\circ F(f)
\]
holds (composition in \(\mathcal D\); see {{< knowl id="composition-category" text="composition" >}}).

Equivalently, for each \(f:X\to Y\) the square commutes:
\[
\begin{CD}
F(X) @>\eta_X>> G(X)\\
@V F(f) VV @VV G(f) V\\
F(Y) @>>\eta_Y> G(Y).
\end{CD}
\]

The components \(\eta_X\) are called the **components** of \(\eta\).

## Examples
1. **Singleton map \(X\to\mathcal P(X)\) (Set)**.  
   Let \(\mathbf{Set}\) be the category of {{< knowl id="set" section="shared-foundations" text="sets" >}}.  
   Define the covariant “power set” functor \(P:\mathbf{Set}\to\mathbf{Set}\) by \(P(X)=\mathcal P(X)\) and, for a {{< knowl id="function" section="shared-foundations" text="function" >}} \(f:X\to Y\), let \(P(f):\mathcal P(X)\to\mathcal P(Y)\) be the {{< knowl id="image" section="shared-foundations" text="image" >}} map \(S\mapsto f(S)\).  
   Then the family \(\eta_X:X\to\mathcal P(X)\), \(x\mapsto\{x\}\), defines a natural transformation
   \[
   \eta:\mathrm{Id}_{\mathbf{Set}}\Rightarrow P,
   \]
   since \(P(f)(\{x\})=\{f(x)\}\).

2. **Postcomposition induces a natural transformation on representables**.  
   In any \(\mathcal C\), fix a morphism \(h:A\to B\). Consider the contravariant hom-functors
   \(\mathrm{Hom}_{\mathcal C}(-,A)\) and \(\mathrm{Hom}_{\mathcal C}(-,B)\) (see {{< knowl id="contravariant-functor" text="contravariant functor" >}}).  
   Define, for each \(X\),
   \[
   \eta_X:\mathrm{Hom}_{\mathcal C}(X,A)\to \mathrm{Hom}_{\mathcal C}(X,B),\quad f\mapsto h\circ f.
   \]
   Naturality follows from associativity of composition.

3. **The evaluation map into the double dual (Vect\(_k\))**.  
   In the category of \(k\)-vector spaces, there is a natural transformation
   \[
   \mathrm{ev}:\mathrm{Id}\Rightarrow (-)^{\ast\ast}
   \]
   whose component at \(V\) is the canonical linear map \(V\to V^{\ast\ast}\), \(v\mapsto(\varphi\mapsto\varphi(v))\).  
   For finite-dimensional \(V\) this component is an isomorphism, so \(\mathrm{ev}\) becomes a {{< knowl id="natural-isomorphism" text="natural isomorphism" >}} on the full subcategory of finite-dimensional spaces.
