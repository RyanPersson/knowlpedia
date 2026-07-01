+++
id = "algebra-modules/rational-canonical-form-theorem"
title = "Rational canonical form theorem"
kind = "knowl"
summary = "Every linear operator is similar to a block diagonal companion-matrix form determined by invariant factors."
aliases = ["rational-canonical-form-theorem", "Rational canonical form theorem"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/rational-canonical-form-theorem.md"
+++

**Rational canonical form theorem**: Let \(T\) be a [[linear-algebra/linear-map|linear map]] on a finite-dimensional [[linear-algebra/vector-space|vector space]] \(V\) over a field \(k\). Then there exists a [[algebra-modules/basis-module|basis]] of \(V\) such that the [[algebra-modules/matrix-representation|matrix representation]] of \(T\) is block diagonal with blocks equal to companion matrices \(C(f_1),\dots,C(f_s)\) of monic polynomials \(f_1,\dots,f_s\in k[x]\) satisfying
\[
f_1 \mid f_2 \mid \cdots \mid f_s.
\]
The polynomials \(f_i\) (the invariant factors) are uniquely determined by \(T\). Moreover, \(f_s\) is the [[linear-algebra/minimal-polynomial|minimal polynomial]] of \(T\), and \(\prod_i f_i\) is the [[linear-algebra/characteristic-polynomial|characteristic polynomial]] of \(T\).

Conceptually, one views \(V\) as a module over the [[algebra-rings/polynomial-ring|polynomial ring]] \(k[x]\) via \(x\cdot v := T(v)\) and applies the [[algebra-modules/structure-theorem-pid|structure theorem over a PID]] (since \(k[x]\) is a PID). The companion blocks encode the cyclic summands in the resulting module decomposition.
