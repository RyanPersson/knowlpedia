+++
id = "algebra-modules/flat-module"
title = "Flat module"
kind = "knowl"
summary = "A module whose tensor product functor preserves exactness."
aliases = ["flat-module", "Flat module"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/flat-module.md"
+++

A **flat module** is a left \(R\)-module \(M\) over a ring \(R\) such that tensoring with \(M\) preserves exactness: for every [[algebra-modules/short-exact-sequence|short exact sequence]] of right \(R\)-modules
\[
0\to A\to B\to C\to 0,
\]
the sequence
\[
0\to A\otimes_R M\to B\otimes_R M\to C\otimes_R M\to 0
\]
is exact, where \(\otimes_R\) is the [[algebra-modules/tensor-product|tensor product]]. Equivalently, the functor \(-\otimes_R M\) is exact (it is always right-exact, so flatness is precisely left-exactness).

Flatness is weaker than projectivity: every [[algebra-modules/projective-module|projective module]] is flat (see [[algebra-modules/projective-implies-flat|projective implies flat]]), and every [[algebra-modules/free-module|free module]] is flat. Over a [[algebra-rings/commutative-ring|commutative ring]], flatness controls base change and localization.

**Examples:**
- Any free \(R\)-module is flat.
- If \(R\) is commutative and \(S\subseteq R\) is multiplicative, then the localization \(S^{-1}R\) is flat as an \(R\)-module.
- Over a [[algebra-rings/pid|PID]], every [[algebra-modules/torsion-free-module|torsion-free module]] is flat.
