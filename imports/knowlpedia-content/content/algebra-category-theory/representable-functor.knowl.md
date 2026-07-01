+++
id = "algebra-category-theory/representable-functor"
title = "Representable functor"
kind = "knowl"
summary = "A Set-valued functor naturally isomorphic to a Hom functor."
aliases = ["representable-functor", "Representable functor"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/representable-functor.md"
+++

Let \(\mathcal{C}\) be a [[algebra-category-theory/category|category]] such that each hom-class \(\mathrm{Hom}_{\mathcal{C}}(A,B)\) is a [[shared-foundations/set|set]] (i.e. \(\mathcal{C}\) is locally small).

A covariant [[algebra-category-theory/functor|functor]] \(F:\mathcal{C}\to \mathbf{Set}\) is **representable** if there exists an object \(A\in \mathcal{C}\) and a [[algebra-category-theory/natural-isomorphism|natural isomorphism]]
\[
F \;\cong\; \mathrm{Hom}_{\mathcal{C}}(A,-).
\]

A contravariant [[algebra-category-theory/contravariant-functor|functor]] \(F:\mathcal{C}^{op}\to \mathbf{Set}\) is **representable** if there exists an object \(A\in \mathcal{C}\) and a natural isomorphism
\[
F \;\cong\; \mathrm{Hom}_{\mathcal{C}}(-,A),
\]
where \(\mathcal{C}^{op}\) is the [[algebra-category-theory/opposite-category|opposite category]].

The object \(A\) is called a **representing object** for \(F\). If \(F\) is representable, then any two representing objects are uniquely [[algebra-category-theory/isomorphism-category|isomorphic]].

## Yoneda viewpoint
By the [[algebra-category-theory/yoneda-lemma|Yoneda lemma]], natural transformations \(\mathrm{Hom}_{\mathcal{C}}(A,-)\Rightarrow F\) correspond bijectively to elements of \(F(A)\). In particular, a representation \(F\cong \mathrm{Hom}_{\mathcal{C}}(A,-)\) is determined by a “universal element” in \(F(A)\).

## Examples
### Example (Set: the identity functor)
In \(\mathbf{Set}\), the identity functor \(\mathrm{Id}:\mathbf{Set}\to \mathbf{Set}\) is representable by the one-point set \(1\):
\[
\mathrm{Hom}_{\mathbf{Set}}(1,X)\cong X,
\]
since a function \(1\to X\) is determined by the image of the unique element of \(1\). (Here “function” is [[shared-foundations/function|function]].)

### Example (Grp: the forgetful functor)
Let \(U:\mathbf{Grp}\to \mathbf{Set}\) be the forgetful functor sending a group to its underlying set. Then \(U\) is representable by \(\mathbb{Z}\) (the free group on one generator):
\[
\mathrm{Hom}_{\mathbf{Grp}}(\mathbb{Z},G)\cong U(G),
\]
by sending a homomorphism \(\varphi:\mathbb{Z}\to G\) to \(\varphi(1)\).

### Example (\(R\)-Mod: the forgetful functor)
Let \(U:R\text{-}\mathbf{Mod}\to \mathbf{Set}\) be the forgetful functor. Then \(U\) is representable by the regular module \(R\):
\[
\mathrm{Hom}_{R}(R,M)\cong U(M),
\]
via \(\varphi\mapsto \varphi(1)\). This is natural in \(M\).
