---
title: "Rational canonical form theorem"
description: "Every linear operator is similar to a block diagonal companion-matrix form determined by invariant factors."
---

**Rational canonical form theorem**: Let \(T\) be a {{< knowl id="linear-map" section="linear-algebra" text="linear map" >}} on a finite-dimensional {{< knowl id="vector-space" section="linear-algebra" text="vector space" >}} \(V\) over a field \(k\). Then there exists a {{< knowl id="basis-module" text="basis" >}} of \(V\) such that the {{< knowl id="matrix-representation" text="matrix representation" >}} of \(T\) is block diagonal with blocks equal to companion matrices \(C(f_1),\dots,C(f_s)\) of monic polynomials \(f_1,\dots,f_s\in k[x]\) satisfying
\[
f_1 \mid f_2 \mid \cdots \mid f_s.
\]
The polynomials \(f_i\) (the invariant factors) are uniquely determined by \(T\). Moreover, \(f_s\) is the {{< knowl id="minimal-polynomial" section="linear-algebra" text="minimal polynomial" >}} of \(T\), and \(\prod_i f_i\) is the {{< knowl id="characteristic-polynomial" section="linear-algebra" text="characteristic polynomial" >}} of \(T\).

Conceptually, one views \(V\) as a module over the {{< knowl id="polynomial-ring" section="algebra-rings" text="polynomial ring" >}} \(k[x]\) via \(x\cdot v := T(v)\) and applies the {{< knowl id="structure-theorem-pid" text="structure theorem over a PID" >}} (since \(k[x]\) is a PID). The companion blocks encode the cyclic summands in the resulting module decomposition.
