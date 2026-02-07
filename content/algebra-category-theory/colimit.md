---
title: "Colimit"
description: "A universal cocone from a diagram, generalizing coproducts, pushouts, and coequalizers."
---

Let \(\mathcal{C}\) be a {{< knowl id="category" text="category" >}} and let \(J\) be an indexing category. A **diagram of shape \(J\)** in \(\mathcal{C}\) is a {{< knowl id="functor" text="functor" >}}
\[
D:J\to \mathcal{C}.
\]

A **cocone** from \(D\) consists of an object \(C\) of \(\mathcal{C}\) together with morphisms
\[
\kappa_j: D(j) \to C\quad (j\in \mathrm{Ob}(J))
\]
such that for every morphism \(\alpha:j\to k\) in \(J\),
\[
\kappa_k\circ D(\alpha) = \kappa_j
\]
(using {{< knowl id="composition-category" text="composition" >}}).

A **colimit** of \(D\) is a cocone \((\mathrm{colim}\,D,\kappa_j)\) such that for every other cocone \((N,\nu_j)\) from \(D\), there exists a unique morphism \(m:\mathrm{colim}\,D \to N\) with
\[
m\circ \kappa_j = \nu_j\quad\text{for all }j.
\]

One writes \(\mathrm{colim}\,D\) (or \(\varinjlim D\)). If a colimit exists, it is unique up to unique {{< knowl id="isomorphism-category" text="isomorphism" >}}.

## Relationship to other constructions
- The dual notion is the {{< knowl id="limit" text="limit" >}}.
- Equivalently, \(\mathrm{colim}_{\mathcal{C}} D\) is \(\lim_{\mathcal{C}^{op}} D^{op}\) in the {{< knowl id="opposite-category" text="opposite category" >}}.

## Examples
### Example (Coproduct)
If \(J\) is the discrete category on two objects and \(D\) picks out objects \(X\) and \(Y\), then \(\mathrm{colim}\,D\) is the {{< knowl id="coproduct" text="coproduct" >}} \(X\amalg Y\).

In \(\mathbf{Set}\), this is the disjoint union of sets.

### Example (Coequalizer)
If \(J\) is the “parallel pair” shape \(A \rightrightarrows B\), then \(\mathrm{colim}\,D\) is the {{< knowl id="coequalizer" text="coequalizer" >}} of the two morphisms.

In \(\mathbf{Set}\), this is a quotient \(B/{\sim}\) identifying \(f(a)\sim g(a)\).

### Example (Pushout)
If \(J\) is the span shape \(X \leftarrow Z \rightarrow Y\), then \(\mathrm{colim}\,D\) is the {{< knowl id="pushout" text="pushout" >}} \(X\amalg_Z Y\).

In \(\mathbf{Top}\), this is the usual gluing construction obtained as a quotient of \(X\amalg Y\) by identifying \(f(z)\) with \(g(z)\).
