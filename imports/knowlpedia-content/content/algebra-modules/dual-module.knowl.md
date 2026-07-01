+++
id = "algebra-modules/dual-module"
title = "Dual module"
kind = "knowl"
summary = "The Hom module Hom_R(M,R) for a module over a commutative ring."
aliases = ["dual-module", "Dual module"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/dual-module.md"
+++

A **dual module** of an \(R\)-module \(M\) (for a commutative ring \(R\)) is
\[
M^\vee := \mathrm{Hom}_R(M,R),
\]
viewed as an \(R\)-module via the standard structure on the [[algebra-modules/hom-module|Hom module]] when \(R\) is a [[algebra-rings/commutative-ring|commutative ring]].

Duality is contravariant and interacts tightly with tensors via the [[algebra-modules/tensor-hom-adjunction|tensor–Hom adjunction]]; it packages bilinear pairings \(M\times N\to R\) as linear maps \(M\to N^\vee\). For [[algebra-modules/free-module|free modules]] of finite rank, duality is well-behaved and compatible with the notion of a [[algebra-modules/basis-module|basis]], producing a dual basis.

**Examples:**
- If \(M\cong R^n\) is free with basis \(e_1,\dots,e_n\), then \(M^\vee\cong R^n\) with dual basis \(e_1^\vee,\dots,e_n^\vee\) characterized by \(e_i^\vee(e_j)=\delta_{ij}\).
- If \(V\) is a finite-dimensional vector space over a [[algebra-rings/field|field]], then \(V^\vee\) is the usual linear dual space.
