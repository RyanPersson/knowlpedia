---
title: "Coproduct"
description: "An object A ⊔ B with injections, universal among cocones from A and B."
---

Let \(\mathcal C\) be a {{< knowl id="category" text="category" >}} and let \(A,B\) be {{< knowl id="object" text="objects" >}} of \(\mathcal C\).

A **(binary) coproduct** of \(A\) and \(B\) is a triple \((A\sqcup B,\iota_1,\iota_2)\) consisting of an object \(A\sqcup B\) and morphisms
\[
\iota_1:A\to A\sqcup B,\qquad \iota_2:B\to A\sqcup B
\]
such that for every object \(X\) and every pair of morphisms \(f:A\to X\), \(g:B\to X\), there exists a **unique** morphism
\[
[f,g]:A\sqcup B\to X
\]
making
\[
[f,g]\circ \iota_1=f,\qquad [f,g]\circ \iota_2=g
\]
hold (see {{< knowl id="composition-category" text="composition" >}}).

Coproducts are unique up to unique {{< knowl id="isomorphism-category" text="isomorphism" >}}.

Coproduct is the dual notion to {{< knowl id="categorical-product" text="product" >}}: a coproduct in \(\mathcal C\) is a product in the {{< knowl id="opposite-category" text="opposite category" >}} \(\mathcal C^{\mathrm{op}}\). It is a special case of a {{< knowl id="colimit" text="colimit" >}}.

## Examples
1. **\(\mathbf{Set}\)**.  
   The coproduct is the disjoint union \(A\sqcup B\), with injections \(A\hookrightarrow A\sqcup B\) and \(B\hookrightarrow A\sqcup B\).

2. **\(\mathbf{Grp}\)**.  
   The coproduct of groups \(G,H\) is the free product \(G\ast H\). A homomorphism \(G\ast H\to X\) is uniquely determined by its restrictions \(G\to X\) and \(H\to X\).

3. **\(\mathbf{Ab}\) and \(R\)-Mod**.  
   The coproduct is the direct sum \(A\oplus B\). In these additive settings, finite coproducts and finite products coincide (biproducts), a key feature of an {{< knowl id="additive-category" text="additive category" >}}.
