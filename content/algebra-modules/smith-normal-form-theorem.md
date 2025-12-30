---
title: "Smith normal form theorem"
description: "A matrix over a PID can be diagonalized with divisibility conditions on the diagonal."
---

**Smith normal form theorem**: Let \(R\) be a {{</* knowl id="pid" text="PID" */>}} and let \(A\) be an \(m\times n\) matrix with entries in \(R\). Then there exist invertible matrices \(U\in \mathrm{GL}_m(R)\) and \(V\in \mathrm{GL}_n(R)\) such that
\[
UAV=\mathrm{diag}(d_1,\dots,d_r,0,\dots,0),
\]
where \(d_i\neq 0\) for \(1\le i\le r\) and \(d_1\mid d_2\mid \cdots \mid d_r\). The \(d_i\) are determined uniquely up to multiplication by units; they are the Smith invariants (see {{</* knowl id="smith-normal-form-invariants" text="Smith normal form invariants" */>}}).

Interpreting \(A\) as the matrix of a homomorphism between free modules (compare {{</* knowl id="matrix-representation" text="matrix representation" */>}}), Smith normal form yields the invariant factor decomposition in the {{</* knowl id="structure-theorem-pid" text="structure theorem for finitely generated modules over a PID" */>}} by identifying the cokernel as a direct sum of cyclic modules \(R/(d_i)\).

**Proof sketch**: Use elementary row/column operations corresponding to multiplication by invertible matrices to perform a Euclidean-algorithm-style reduction on entries, producing a diagonal form with each diagonal entry dividing the next. The PID property ensures principal generators for ideals arising during the reduction.
