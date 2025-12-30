---
title: "Field norm"
description: "For a finite extension L/K, N_{L/K}(α) is the determinant of multiplication-by-α as a K-linear map."
---

**Definition.** Let \(L/K\) be a finite {{</* knowl id="field-extension" text="field extension" */>}} with \(n=[L:K]\). For \(\alpha\in L\), let \(m_\alpha(x)=\alpha x\) be multiplication by \(\alpha\). The **norm** of \(\alpha\) from \(L\) to \(K\) is
\[
\mathrm{N}_{L/K}(\alpha) \;=\; \det(m_\alpha)\in K,
\]
the usual {{</* knowl id="determinant" text="determinant" */>}} of this \(K\)-linear operator.

The norm is multiplicative: \(\mathrm{N}(\alpha\beta)=\mathrm{N}(\alpha)\mathrm{N}(\beta)\), and is compatible with towers (see {{</* knowl id="trace-norm-towers" text="norm in towers" */>}}).

**See also.** {{</* knowl id="trace-field" text="field trace" */>}}, {{</* knowl id="group-of-units" text="units" */>}} (the norm sends \(L^\times\to K^\times\)).

**Examples.**
1. In \(L=\mathbb{Q}(\sqrt d)\) (char \(\neq 2\)), \(\mathrm{N}_{L/\mathbb{Q}}(a+b\sqrt d)=a^2-d b^2\).
2. In \(\mathbb{C}/\mathbb{R}\), \(\mathrm{N}_{\mathbb{C}/\mathbb{R}}(a+bi)=a^2+b^2\).
3. For \(L=\mathbb{F}_{q^n}\) over \(\mathbb{F}_q\), \(\mathrm{N}_{L/\mathbb{F}_q}(\alpha)=\alpha^{(q^n-1)/(q-1)}\).
