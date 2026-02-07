---
title: "Graded ring"
description: "A ring decomposed into homogeneous pieces compatible with multiplication."
---

A **graded ring** is a {{< knowl id="ring" section="algebra-rings" text="ring" >}} \(R\) together with a direct-sum decomposition of abelian groups
\[
R=\bigoplus_{n\in \mathbb Z} R_n
\]
(sometimes \(n\in\mathbb N\)) such that \(R_nR_m\subseteq R_{n+m}\) for all \(m,n\), and typically \(1\in R_0\). The decomposition is an internal {{< knowl id="direct-sum-modules" text="direct sum" >}} in the category of abelian groups.

Graded rings organize algebra by “degree” and are the ambient objects for {{< knowl id="graded-module" text="graded modules" >}}; a fundamental source is the {{< knowl id="associated-graded-ring" text="associated graded ring" >}} of a filtration.

**Examples:**
- The {{< knowl id="polynomial-ring" section="algebra-rings" text="polynomial ring" >}} \(k[x_1,\dots,x_n]\) is \(\mathbb N\)-graded by total degree, with \(R_d\) the homogeneous polynomials of degree \(d\).
- If \(R\) has an ideal-adic filtration, the associated graded ring \(\bigoplus_{n\ge 0} I^n/I^{n+1}\) is naturally graded.
