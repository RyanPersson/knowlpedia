---
title: "Representable functor"
description: "A Set-valued functor naturally isomorphic to a Hom functor."
---

Let \(\mathcal{C}\) be a {{< knowl id="category" text="category" >}} such that each hom-class \(\mathrm{Hom}_{\mathcal{C}}(A,B)\) is a {{< knowl id="set" section="shared-foundations" text="set" >}} (i.e. \(\mathcal{C}\) is locally small).

A covariant {{< knowl id="functor" text="functor" >}} \(F:\mathcal{C}\to \mathbf{Set}\) is **representable** if there exists an object \(A\in \mathcal{C}\) and a {{< knowl id="natural-isomorphism" text="natural isomorphism" >}}
\[
F \;\cong\; \mathrm{Hom}_{\mathcal{C}}(A,-).
\]

A contravariant {{< knowl id="contravariant-functor" text="functor" >}} \(F:\mathcal{C}^{op}\to \mathbf{Set}\) is **representable** if there exists an object \(A\in \mathcal{C}\) and a natural isomorphism
\[
F \;\cong\; \mathrm{Hom}_{\mathcal{C}}(-,A),
\]
where \(\mathcal{C}^{op}\) is the {{< knowl id="opposite-category" text="opposite category" >}}.

The object \(A\) is called a **representing object** for \(F\). If \(F\) is representable, then any two representing objects are uniquely {{< knowl id="isomorphism-category" text="isomorphic" >}}.

## Yoneda viewpoint
By the {{< knowl id="yoneda-lemma" text="Yoneda lemma" >}}, natural transformations \(\mathrm{Hom}_{\mathcal{C}}(A,-)\Rightarrow F\) correspond bijectively to elements of \(F(A)\). In particular, a representation \(F\cong \mathrm{Hom}_{\mathcal{C}}(A,-)\) is determined by a “universal element” in \(F(A)\).

## Examples
### Example (Set: the identity functor)
In \(\mathbf{Set}\), the identity functor \(\mathrm{Id}:\mathbf{Set}\to \mathbf{Set}\) is representable by the one-point set \(1\):
\[
\mathrm{Hom}_{\mathbf{Set}}(1,X)\cong X,
\]
since a function \(1\to X\) is determined by the image of the unique element of \(1\). (Here “function” is {{< knowl id="function" section="shared-foundations" text="function" >}}.)

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
