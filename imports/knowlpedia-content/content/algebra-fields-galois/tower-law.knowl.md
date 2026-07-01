+++
id = "algebra-fields-galois/tower-law"
title = "Tower law"
kind = "knowl"
summary = "In a finite tower K ⊂ L ⊂ M, degrees multiply: [M:K]=[M:L][L:K]."
aliases = ["tower-law", "Tower law"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/tower-law.md"
+++

Let \(K \subseteq L \subseteq M\) be a [[algebra-fields-galois/tower-of-fields|tower of fields]], so \(L\) is an [[algebra-fields-galois/intermediate-field|intermediate field]] of the [[algebra-fields-galois/field-extension|field extension]] \(M/K\). Assume the extensions \(L/K\) and \(M/L\) are finite, i.e. have finite [[algebra-fields-galois/degree-of-extension|degree]].

**Theorem (Tower law).** If \([L:K]<\infty\) and \([M:L]<\infty\), then \([M:K]<\infty\) and
\[
[M:K]=[M:L]\,[L:K].
\]
Equivalently, if \([M:K]<\infty\) then \([M:L]\) and \([L:K]\) are finite and the same formula holds.

A standard proof uses bases: if \(\{\ell_1,\dots,\ell_r\}\) is a \(K\)-basis of \(L\) and \(\{m_1,\dots,m_s\}\) is an \(L\)-basis of \(M\), then \(\{m_i\ell_j : 1\le i\le s,\ 1\le j\le r\}\) is a \(K\)-basis of \(M\).

### Examples
1. \(\mathbb{Q}\subset \mathbb{Q}(\sqrt2)\subset \mathbb{Q}(\sqrt2,\sqrt3)\).
   Here \([\mathbb{Q}(\sqrt2):\mathbb{Q}]=2\) and \([\mathbb{Q}(\sqrt2,\sqrt3):\mathbb{Q}(\sqrt2)]=2\), so the tower law gives
   \[
   [\mathbb{Q}(\sqrt2,\sqrt3):\mathbb{Q}]=2\cdot 2=4.
   \]

2. Finite fields: \(\mathbb{F}_p \subset \mathbb{F}_{p^2} \subset \mathbb{F}_{p^6}\).
   Then \([\mathbb{F}_{p^2}:\mathbb{F}_p]=2\) and \([\mathbb{F}_{p^6}:\mathbb{F}_{p^2}]=3\), hence
   \[
   [\mathbb{F}_{p^6}:\mathbb{F}_p]=3\cdot 2=6.
   \]

3. Cyclotomic example: \(\mathbb{Q}\subset \mathbb{Q}(\zeta_3)\subset \mathbb{Q}(\zeta_9)\), where \(\zeta_n\) is a [[algebra-fields-galois/primitive-root-of-unity|primitive n-th root of unity]].
   One has \([\mathbb{Q}(\zeta_3):\mathbb{Q}]=2\) and \([\mathbb{Q}(\zeta_9):\mathbb{Q}(\zeta_3)]=3\), so \([\mathbb{Q}(\zeta_9):\mathbb{Q}]=6\).
