+++
id = "algebra-category-theory/limit"
title = "Limit"
kind = "knowl"
summary = "A universal cone to a diagram, generalizing products, pullbacks, and equalizers."
aliases = ["limit"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/limit.md"
+++

Let \(\mathcal{C}\) be a [[algebra-category-theory/category|category]] and let \(J\) be an indexing category. A **diagram of shape \(J\)** in \(\mathcal{C}\) is a [[algebra-category-theory/functor|functor]]
\[
D:J\to \mathcal{C}.
\]

A **cone** to \(D\) consists of an object \(L\) of \(\mathcal{C}\) together with morphisms
\[
\lambda_j: L \to D(j)\quad (j\in \mathrm{Ob}(J))
\]
such that for every morphism \(\alpha:j\to k\) in \(J\),
\[
D(\alpha)\circ \lambda_j = \lambda_k
\]
(using [[algebra-category-theory/composition-category|composition]]).

A **limit** of \(D\) is a cone \((L,\lambda_j)\) such that for every other cone \((N,\nu_j)\) to \(D\), there exists a unique morphism \(m:N\to L\) with
\[
\lambda_j\circ m = \nu_j\quad\text{for all }j.
\]

One writes \(L = \varprojlim D\) (or \(\lim D\)). If a limit exists, it is unique up to unique [[algebra-category-theory/isomorphism-category|isomorphism]].

## Relationship to other constructions
- The dual notion is the [[algebra-category-theory/colimit|colimit]].
- Many familiar constructions are special limits (see examples below).

## Examples
### Example (Categorical product)
If \(J\) is the discrete category on two objects and \(D\) picks out objects \(X\) and \(Y\), then \(\lim D\) is the [[algebra-category-theory/categorical-product|categorical product]] \(X\times Y\).

In \(\mathbf{Set}\), this recovers the usual [[shared-foundations/cartesian-product|cartesian product]] of sets.

### Example (Equalizer)
If \(J\) is the “parallel pair” shape \(A \rightrightarrows B\), then \(\lim D\) is the [[algebra-category-theory/equalizer|equalizer]] of the two morphisms.

In \(\mathbf{Set}\), for functions \(f,g:A\to B\), the equalizer is the subset \(\{a\in A\mid f(a)=g(a)\}\).

### Example (Pullback)
If \(J\) is the cospan shape \(X\to Z \leftarrow Y\), then \(\lim D\) is the [[algebra-category-theory/pullback|pullback]] \(X\times_Z Y\).

In \(\mathbf{Set}\), this is the fiber product \(\{(x,y)\in X\times Y \mid f(x)=g(y)\}\).
