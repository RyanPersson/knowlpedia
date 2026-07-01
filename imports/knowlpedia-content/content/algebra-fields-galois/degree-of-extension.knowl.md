+++
id = "algebra-fields-galois/degree-of-extension"
title = "Degree of a field extension"
kind = "knowl"
summary = "The dimension [E:F] of E as a vector space over F (finite or infinite)."
aliases = ["degree-of-extension", "Degree of a field extension"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/degree-of-extension.md"
+++

Let \(E/F\) be a [[algebra-fields-galois/field-extension|field extension]]. The **degree** of \(E/F\), denoted \([E:F]\), is the dimension of \(E\) as a vector space over \(F\).

Concretely, a subset \(B\subseteq E\) is an **\(F\)-basis** of \(E\) if every \(x\in E\) can be written uniquely as a finite sum
\[
x=\sum_{b\in B} c_b\, b \quad \text{with } c_b\in F \text{ and all but finitely many } c_b=0.
\]
The cardinality of a basis is independent of the choice of basis; this cardinal is \([E:F]\). The extension is called **finite** if \([E:F]<\infty\).

If \(F\subseteq K\subseteq E\) is a [[algebra-fields-galois/tower-of-fields|tower of fields]] and the degrees are finite, then the [[algebra-fields-galois/tower-law|tower law]] states
\[
[E:F]=[E:K]\,[K:F].
\]

### Examples
1. \([\mathbb{Q}(\sqrt2):\mathbb{Q}]=2\), with basis \(\{1,\sqrt2\}\) over \(\mathbb{Q}\).
2. \([\mathbb{C}:\mathbb{R}]=2\), with basis \(\{1,i\}\) over \(\mathbb{R}\).
3. For a prime \(p\) and \(n\ge 1\), \([\mathbb{F}_{p^n}:\mathbb{F}_p]=n\).
   (In particular, \(\mathbb{F}_{p^n}/\mathbb{F}_p\) is finite of degree \(n\).)
