---
title: "Degree of a field extension"
description: "The dimension [L:K] of L as a K-vector space."
---

**Definition.** Let \(L/K\) be a {{< knowl id="field-extension" text="field extension" >}}. The **degree** of the extension is
\[
[L:K] \;=\; \dim_K(L),
\]
the dimension of \(L\) as a {{< knowl id="vector-space" section="shared-linear-algebra" text="vector space" >}} over \(K\).  
If this dimension is finite, \(L/K\) is a **finite extension**; otherwise \([L:K]=\infty\).

In a tower \(K\subseteq F\subseteq L\) with finite degrees, the {{< knowl id="tower-law" text="tower law" >}} says \([L:K]=[L:F]\,[F:K]\).

**See also.** {{< knowl id="tower-of-fields" text="tower of fields" >}}, {{< knowl id="simple-extension" text="simple extension" >}}.

**Examples.**
1. \([\mathbb{C}:\mathbb{R}]=2\) with basis \(\{1,i\}\).
2. \([\mathbb{Q}(\sqrt2):\mathbb{Q}]=2\) with basis \(\{1,\sqrt2\}\).
3. If \(q=p^n\), then \([\mathbb{F}_{q}:\mathbb{F}_p]=n\) (see {{< knowl id="finite-field" text="finite fields" >}}).
