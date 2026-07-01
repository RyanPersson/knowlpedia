+++
id = "algebra-modules/associated-graded-ring"
title = "Associated graded ring"
kind = "knowl"
summary = "The graded ring gr_F(R)=⊕ F_nR/F_{n-1}R attached to a filtered ring."
aliases = ["associated-graded-ring", "Associated graded ring"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/associated-graded-ring.md"
+++

Given a [[algebra-modules/filtered-ring|filtered ring]] \((R,F_\bullet)\) with \(F_{n-1}R\subseteq F_nR\), the **associated graded ring** is
\[
\mathrm{gr}_F(R) \;:=\; \bigoplus_{n} F_nR/F_{n-1}R,
\]
with multiplication induced from \(R\): if \(x\in F_nR\) and \(y\in F_mR\), then the product of their classes in the quotients defines an element of \(F_{n+m}R/F_{n+m-1}R\). Each summand is a [[algebra-rings/quotient-ring|quotient]] of additive groups, and the direct sum is an internal [[algebra-modules/direct-sum-modules|direct sum]].

The ring \(\mathrm{gr}_F(R)\) is naturally a [[algebra-modules/graded-ring|graded ring]]; it captures the leading-order behavior of elements of \(R\) and often has simpler algebraic structure.

**Examples:**
- For the \(I\)-adic filtration, \(\mathrm{gr}_I(R)=\bigoplus_{n\ge 0} I^n/I^{n+1}\).
- If the filtration is already split by degree (as in a graded ring viewed with \(F_n=\bigoplus_{i\le n}R_i\)), then \(\mathrm{gr}_F(R)\cong R\) as graded rings.
