---
title: "Uniqueness of Splitting Fields"
description: "Any two splitting fields of the same polynomial over K are K-isomorphic."
---

**Theorem (Uniqueness).**  
Let \(f\in K[x]\) be a nonzero polynomial and let \(L\) and \(L'\) be splitting fields of \(f\) over \(K\). Then there exists a \(K\)-isomorphism
\[
\phi: L \xrightarrow{\ \sim\ } L'
\]
(i.e., an isomorphism fixing \(K\) pointwise). The isomorphism is generally not unique.

This is the uniqueness part of {{</* knowl id="splitting-field-existence-uniqueness" text="splitting field existence/uniqueness" */>}}.

**Examples.**
1. If \(L=\mathbb{Q}(\sqrt2)\) and \(L'=\mathbb{Q}(\alpha)\) where \(\alpha^2=2\), then \(\alpha=\pm\sqrt2\) and the map \(\sqrt2\mapsto \alpha\) gives a \(\mathbb{Q}\)-isomorphism \(L\cong_{\mathbb{Q}} L'\).
2. For \(f=x^2+x+1\) over \(\mathbb{F}_2\), any two splitting fields are isomorphic to \(\mathbb{F}_4\).
3. For separable irreducible \(f\), the splitting field is characterized (up to \(K\)-isomorphism) by “adjoin all roots.”

**Related.** {{</* knowl id="field-isomorphism" text="field isomorphisms" */>}}, {{</* knowl id="normality-splitting-field" text="splitting fields and normality" */>}}.
