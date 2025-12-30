---
title: "Dual module"
description: "The Hom module Hom_R(M,R) for a module over a commutative ring."
---

A **dual module** of an \(R\)-module \(M\) (for a commutative ring \(R\)) is
\[
M^\vee := \mathrm{Hom}_R(M,R),
\]
viewed as an \(R\)-module via the standard structure on the {{</* knowl id="hom-module" text="Hom module" */>}} when \(R\) is a {{</* knowl id="commutative-ring" text="commutative ring" */>}}.

Duality is contravariant and interacts tightly with tensors via the {{</* knowl id="tensor-hom-adjunction" text="tensor–Hom adjunction" */>}}; it packages bilinear pairings \(M\times N\to R\) as linear maps \(M\to N^\vee\). For {{</* knowl id="free-module" text="free modules" */>}} of finite rank, duality is well-behaved and compatible with the notion of a {{</* knowl id="basis-module" text="basis" */>}}, producing a dual basis.

**Examples:**
- If \(M\cong R^n\) is free with basis \(e_1,\dots,e_n\), then \(M^\vee\cong R^n\) with dual basis \(e_1^\vee,\dots,e_n^\vee\) characterized by \(e_i^\vee(e_j)=\delta_{ij}\).
- If \(V\) is a finite-dimensional vector space over a {{</* knowl id="field" text="field" */>}}, then \(V^\vee\) is the usual linear dual space.
