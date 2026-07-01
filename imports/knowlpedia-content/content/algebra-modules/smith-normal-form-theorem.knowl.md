+++
id = "algebra-modules/smith-normal-form-theorem"
title = "Smith normal form theorem"
kind = "knowl"
summary = "A matrix over a PID can be diagonalized with divisibility conditions on the diagonal."
aliases = ["smith-normal-form-theorem", "Smith normal form theorem"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/smith-normal-form-theorem.md"
+++

**Smith normal form theorem**: Let \(R\) be a [[algebra-rings/pid|PID]] and let \(A\) be an \(m\times n\) matrix with entries in \(R\). Then there exist invertible matrices \(U\in \mathrm{GL}_m(R)\) and \(V\in \mathrm{GL}_n(R)\) such that
\[
UAV=\mathrm{diag}(d_1,\dots,d_r,0,\dots,0),
\]
where \(d_i\neq 0\) for \(1\le i\le r\) and \(d_1\mid d_2\mid \cdots \mid d_r\). The \(d_i\) are determined uniquely up to multiplication by units; they are the Smith invariants (see [[algebra-modules/smith-normal-form-invariants|Smith normal form invariants]]).

Interpreting \(A\) as the matrix of a homomorphism between free modules (compare [[algebra-modules/matrix-representation|matrix representation]]), Smith normal form yields the invariant factor decomposition in the [[algebra-modules/structure-theorem-pid|structure theorem for finitely generated modules over a PID]] by identifying the cokernel as a direct sum of cyclic modules \(R/(d_i)\).
