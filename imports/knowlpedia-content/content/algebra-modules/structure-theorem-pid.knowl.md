+++
id = "algebra-modules/structure-theorem-pid"
title = "Structure theorem for finitely generated modules over a PID"
kind = "knowl"
summary = "A finitely generated module over a PID splits as a free part plus cyclic torsion factors."
aliases = ["structure-theorem-pid", "Structure theorem for finitely generated modules over a PID"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/structure-theorem-pid.md"
+++

**Structure theorem (f.g. modules over a PID)**: Let \(R\) be a [[algebra-rings/pid|principal ideal domain]] and let \(M\) be a [[algebra-modules/finitely-generated-module|finitely generated module]] over \(R\). Then there exist an integer \(r\ge 0\) and nonzero elements \(d_1,\dots,d_t\in R\) with \(d_1\mid d_2\mid \cdots \mid d_t\) such that
\[
M \;\cong\; R^{\,r}\;\oplus\;\bigoplus_{i=1}^t R/(d_i),
\]
a decomposition as a [[algebra-modules/direct-sum-modules|direct sum]] of a free part and cyclic torsion factors. The integer \(r\) and the invariant factors \(d_i\) are unique up to multiplication by units in \(R\). In particular, the torsion submodule of \(M\) is a [[algebra-modules/torsion-module|torsion module]] and the free summand is a [[algebra-modules/free-module|free module]] of rank \(r\).

This theorem is the module-theoretic engine behind the classification of finitely generated abelian groups (the case \(R=\mathbb Z\)); see [[algebra-modules/classification-fg-abelian-groups|classification of finitely generated abelian groups]]. It is closely tied to [[algebra-modules/smith-normal-form-theorem|Smith normal form]], and it admits an equivalent primary decomposition form (see the [[algebra-modules/elementary-divisor-theorem|elementary divisor theorem]]).
