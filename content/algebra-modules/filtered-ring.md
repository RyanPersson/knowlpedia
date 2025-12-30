---
title: "Filtered ring"
description: "A ring equipped with an increasing multiplicative filtration."
---

A **filtered ring** is a {{</* knowl id="ring" text="ring" */>}} \(R\) together with an increasing family of additive subgroups \(\{F_nR\}_{n\in\mathbb Z}\) (often \(n\in\mathbb N\)) such that:
- \(F_nR\subseteq F_{n+1}R\) for all \(n\),
- \(1\in F_0R\),
- \(F_nR\cdot F_mR \subseteq F_{n+m}R\) for all \(m,n\),
- typically \(\bigcup_n F_nR = R\) (exhaustive filtration).

Filtrations measure “order” or “size” of elements and produce graded approximations via the {{</* knowl id="associated-graded-ring" text="associated graded ring" */>}}; many structural arguments pass from \(R\) to its graded shadow.

**Examples:**
- For an {{</* knowl id="ideal" text="ideal" */>}} \(I\subseteq R\), the \(I\)-adic filtration \(F_nR=I^n\) (for \(n\ge 0\)) is multiplicative.
- The degree filtration on \(k[x_1,\dots,x_n]\) given by \(F_d=\{\text{polynomials of degree}\le d\}\) is multiplicative.
