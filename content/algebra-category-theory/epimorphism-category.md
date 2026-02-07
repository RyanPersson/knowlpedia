---
title: "Epimorphism"
description: "A morphism that is right-cancellative; the categorical analogue of a surjection."
---

Let \(\mathcal C\) be a {{< knowl id="category" text="category" >}} and let \(f:A\to B\) be a {{< knowl id="morphism" text="morphism" >}} in \(\mathcal C\).

The morphism \(f\) is an **epimorphism** (or **epi**) if it is *right-cancellative* with respect to {{< knowl id="composition-category" text="composition" >}}: for every object \(C\) of \(\mathcal C\) and all morphisms \(g,h:B\to C\),
\[
g\circ f = h\circ f \quad \Longrightarrow \quad g=h.
\]
Equivalently, postcomposition with \(f\) induces an injective map of hom-sets
\[
\mathrm{Hom}_{\mathcal C}(B,C)\;\longrightarrow\;\mathrm{Hom}_{\mathcal C}(A,C),\qquad g\mapsto g\circ f,
\]
for every object \(C\).

## Basic properties
- Every {{< knowl id="isomorphism-category" text="isomorphism" >}} is an epimorphism.
- Epimorphisms are stable under composition: if \(f:A\to B\) and \(g:B\to C\) are epis, then \(g\circ f\) is an epi.
- **Duality:** \(f\) is an epi in \(\mathcal C\) iff \(f\) is a {{< knowl id="monomorphism-category" text="monomorphism" >}} in the {{< knowl id="opposite-category" text="opposite category" >}} \(\mathcal C^{\mathrm{op}}\).

## Examples
1. **\(\mathbf{Set}\):** A function \(f:A\to B\) is an epimorphism in \(\mathbf{Set}\) iff it is a {{< knowl id="surjective-function" section="shared-foundations" text="surjective function" >}}.

2. **\(\mathbf{Grp}\), \(\mathbf{Ab}\), \(R\mathbf{-Mod}\):** A homomorphism (or \(R\)-linear map) is an epimorphism iff it is surjective on the underlying sets.  
   In particular, the quotient map \(G\to G/N\) and the canonical projection \(M\to M/N\) are epis.

3. **\(\mathbf{Top}\):** A continuous map \(f:X\to Y\) is an epimorphism in \(\mathbf{Top}\) iff it is surjective as a map of underlying sets.

## Remark
Not every category has the property “epis are surjective on underlying sets” (for instance, in some algebraic categories epimorphisms can fail to be surjective). The definition above is the one that makes sense in an arbitrary {{< knowl id="category" text="category" >}}.
