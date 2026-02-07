---
title: "Degree of a field extension"
description: "The dimension [E:F] of E as a vector space over F (finite or infinite)."
---

Let \(E/F\) be a {{< knowl id="field-extension" text="field extension" >}}. The **degree** of \(E/F\), denoted \([E:F]\), is the dimension of \(E\) as a vector space over \(F\).

Concretely, a subset \(B\subseteq E\) is an **\(F\)-basis** of \(E\) if every \(x\in E\) can be written uniquely as a finite sum
\[
x=\sum_{b\in B} c_b\, b \quad \text{with } c_b\in F \text{ and all but finitely many } c_b=0.
\]
The cardinality of a basis is independent of the choice of basis; this cardinal is \([E:F]\). The extension is called **finite** if \([E:F]<\infty\).

If \(F\subseteq K\subseteq E\) is a {{< knowl id="tower-of-fields" text="tower of fields" >}} and the degrees are finite, then the {{< knowl id="tower-law" text="tower law" >}} states
\[
[E:F]=[E:K]\,[K:F].
\]

### Examples
1. \([\mathbb{Q}(\sqrt2):\mathbb{Q}]=2\), with basis \(\{1,\sqrt2\}\) over \(\mathbb{Q}\).
2. \([\mathbb{C}:\mathbb{R}]=2\), with basis \(\{1,i\}\) over \(\mathbb{R}\).
3. For a prime \(p\) and \(n\ge 1\), \([\mathbb{F}_{p^n}:\mathbb{F}_p]=n\).
   (In particular, \(\mathbb{F}_{p^n}/\mathbb{F}_p\) is finite of degree \(n\).)
