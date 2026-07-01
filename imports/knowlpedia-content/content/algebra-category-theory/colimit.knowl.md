+++
id = "algebra-category-theory/colimit"
title = "Colimit"
kind = "knowl"
summary = "A universal cocone from a diagram, generalizing coproducts, pushouts, and coequalizers."
aliases = ["colimit"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/colimit.md"
+++

Let \(\mathcal{C}\) be a [[algebra-category-theory/category|category]] and let \(J\) be an indexing category. A **diagram of shape \(J\)** in \(\mathcal{C}\) is a [[algebra-category-theory/functor|functor]]
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
(using [[algebra-category-theory/composition-category|composition]]).

A **colimit** of \(D\) is a cocone \((\mathrm{colim}\,D,\kappa_j)\) such that for every other cocone \((N,\nu_j)\) from \(D\), there exists a unique morphism \(m:\mathrm{colim}\,D \to N\) with
\[
m\circ \kappa_j = \nu_j\quad\text{for all }j.
\]

One writes \(\mathrm{colim}\,D\) (or \(\varinjlim D\)). If a colimit exists, it is unique up to unique [[algebra-category-theory/isomorphism-category|isomorphism]].

## Relationship to other constructions
- The dual notion is the [[algebra-category-theory/limit|limit]].
- Equivalently, \(\mathrm{colim}_{\mathcal{C}} D\) is \(\lim_{\mathcal{C}^{op}} D^{op}\) in the [[algebra-category-theory/opposite-category|opposite category]].

## Examples
### Example (Coproduct)
If \(J\) is the discrete category on two objects and \(D\) picks out objects \(X\) and \(Y\), then \(\mathrm{colim}\,D\) is the [[algebra-category-theory/coproduct|coproduct]] \(X\amalg Y\).

In \(\mathbf{Set}\), this is the disjoint union of sets.

### Example (Coequalizer)
If \(J\) is the “parallel pair” shape \(A \rightrightarrows B\), then \(\mathrm{colim}\,D\) is the [[algebra-category-theory/coequalizer|coequalizer]] of the two morphisms.

In \(\mathbf{Set}\), this is a quotient \(B/{\sim}\) identifying \(f(a)\sim g(a)\).

### Example (Pushout)
If \(J\) is the span shape \(X \leftarrow Z \rightarrow Y\), then \(\mathrm{colim}\,D\) is the [[algebra-category-theory/pushout|pushout]] \(X\amalg_Z Y\).

In \(\mathbf{Top}\), this is the usual gluing construction obtained as a quotient of \(X\amalg Y\) by identifying \(f(z)\) with \(g(z)\).
