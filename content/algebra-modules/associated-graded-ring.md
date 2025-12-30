---
title: "Associated graded ring"
description: "The graded ring gr_F(R)=⊕ F_nR/F_{n-1}R attached to a filtered ring."
---

Given a {{< knowl id="filtered-ring" text="filtered ring" >}} \((R,F_\bullet)\) with \(F_{n-1}R\subseteq F_nR\), the **associated graded ring** is
\[
\mathrm{gr}_F(R) \;:=\; \bigoplus_{n} F_nR/F_{n-1}R,
\]
with multiplication induced from \(R\): if \(x\in F_nR\) and \(y\in F_mR\), then the product of their classes in the quotients defines an element of \(F_{n+m}R/F_{n+m-1}R\). Each summand is a {{< knowl id="quotient-ring" section="algebra-rings" text="quotient" >}} of additive groups, and the direct sum is an internal {{< knowl id="direct-sum-modules" text="direct sum" >}}.

The ring \(\mathrm{gr}_F(R)\) is naturally a {{< knowl id="graded-ring" text="graded ring" >}}; it captures the leading-order behavior of elements of \(R\) and often has simpler algebraic structure.

**Examples:**
- For the \(I\)-adic filtration, \(\mathrm{gr}_I(R)=\bigoplus_{n\ge 0} I^n/I^{n+1}\).
- If the filtration is already split by degree (as in a graded ring viewed with \(F_n=\bigoplus_{i\le n}R_i\)), then \(\mathrm{gr}_F(R)\cong R\) as graded rings.
