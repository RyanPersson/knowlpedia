+++
id = "algebra-modules/graded-ring"
title = "Graded ring"
kind = "knowl"
summary = "A ring decomposed into homogeneous pieces compatible with multiplication."
aliases = ["graded-ring", "Graded ring"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/graded-ring.md"
+++

A **graded ring** is a [[algebra-rings/ring|ring]] \(R\) together with a direct-sum decomposition of abelian groups
\[
R=\bigoplus_{n\in \mathbb Z} R_n
\]
(sometimes \(n\in\mathbb N\)) such that \(R_nR_m\subseteq R_{n+m}\) for all \(m,n\), and typically \(1\in R_0\). The decomposition is an internal [[algebra-modules/direct-sum-modules|direct sum]] in the category of abelian groups.

Graded rings organize algebra by “degree” and are the ambient objects for [[algebra-modules/graded-module|graded modules]]; a fundamental source is the [[algebra-modules/associated-graded-ring|associated graded ring]] of a filtration.

**Examples:**
- The [[algebra-rings/polynomial-ring|polynomial ring]] \(k[x_1,\dots,x_n]\) is \(\mathbb N\)-graded by total degree, with \(R_d\) the homogeneous polynomials of degree \(d\).
- If \(R\) has an ideal-adic filtration, the associated graded ring \(\bigoplus_{n\ge 0} I^n/I^{n+1}\) is naturally graded.
