---
title: "Field trace"
description: "For a finite extension L/K, Tr_{L/K}(α) is the trace of multiplication-by-α as a K-linear map."
---

**Definition.** Let \(L/K\) be a finite {{</* knowl id="field-extension" text="field extension" */>}} with \(n=[L:K]\). For \(\alpha\in L\), define the \(K\)-linear map
\[
m_\alpha : L \to L,\qquad x \mapsto \alpha x.
\]
The **trace** of \(\alpha\) from \(L\) to \(K\) is
\[
\mathrm{Tr}_{L/K}(\alpha) \;=\; \mathrm{tr}(m_\alpha)\in K,
\]
the ordinary {{</* knowl id="trace" text="trace" */>}} of this linear operator.

The trace is \(K\)-linear and interacts with towers via {{</* knowl id="trace-norm-towers" text="trace in towers" */>}}.

**See also.** {{</* knowl id="norm-field" text="field norm" */>}}, {{</* knowl id="degree-of-extension" text="degree of extension" */>}}.

**Examples.**
1. In \(L=\mathbb{Q}(\sqrt d)\) with \(\mathrm{char}(K)\neq 2\), \(\mathrm{Tr}_{L/\mathbb{Q}}(a+b\sqrt d)=2a\).
2. In \(\mathbb{C}/\mathbb{R}\), \(\mathrm{Tr}_{\mathbb{C}/\mathbb{R}}(a+bi)=2a\).
3. For \(L=\mathbb{F}_{q^n}\) over \(\mathbb{F}_q\), \(\mathrm{Tr}_{L/\mathbb{F}_q}(\alpha)=\alpha+\alpha^q+\cdots+\alpha^{q^{n-1}}\).
