+++
id = "algebra-modules/bilinear-map"
title = "Bilinear map"
kind = "knowl"
summary = "A map that is linear in each variable (and balanced over a ring when needed)."
aliases = ["bilinear-map", "Bilinear map"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/bilinear-map.md"
+++

A **bilinear map** between \(R\)-modules (for a [[algebra-rings/commutative-ring|commutative ring]] \(R\)) is a function \(\beta\colon M\times N\to P\) from a [[shared-foundations/cartesian-product|cartesian product]] of \(R\)-modules such that, for each fixed argument, the resulting map is \(R\)-linear in the other:
\[
\beta(m+m',n)=\beta(m,n)+\beta(m',n),\quad \beta(m,n+n')=\beta(m,n)+\beta(m,n'),
\]
\[
\beta(rm,n)=r\,\beta(m,n),\quad \beta(m,rn)=r\,\beta(m,n).
\]
For a noncommutative ring \(R\), if \(M\) is a right \(R\)-module and \(N\) is a left \(R\)-module, one usually requires \(\beta\) to be **\(R\)-balanced**, meaning additionally \(\beta(mr,n)=\beta(m,rn)\).

Balanced bilinear maps are exactly the maps represented by the [[algebra-modules/tensor-product-universal-property|universal property of the tensor product]]: they correspond uniquely to homomorphisms out of \(M\otimes_R N\) in the category of [[algebra-modules/module|modules]]/abelian groups.

**Examples:**
- Multiplication \(\mu\colon R\times R\to R\) is bilinear for any [[algebra-rings/ring|ring]] \(R\).
- For a commutative ring \(R\) and an \(R\)-module \(M\), the evaluation pairing \(M^\vee\times M\to R\) is bilinear, where \(M^\vee\) is the [[algebra-modules/dual-module|dual module]].
