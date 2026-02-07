---
title: "Discriminant (of a field basis)"
description: "For a finite extension L/K, the discriminant of a K-basis is det(Tr_{L/K}(b_i b_j))."
---

Let \(L/K\) be a finite {{< knowl id="field-extension" text="field extension" >}} of degree \(n\), and let \(\mathrm{Tr}_{L/K}\) be the {{< knowl id="trace-field" text="field trace" >}}. For an \(n\)-tuple \(\mathbf{b}=(b_1,\dots,b_n)\) in \(L\) that is a \(K\)-basis of \(L\), the **discriminant** of \(\mathbf{b}\) (relative to \(L/K\)) is
\[
\mathrm{disc}_{L/K}(\mathbf{b}) \;:=\; \det\!\big(\mathrm{Tr}_{L/K}(b_i b_j)\big)_{1\le i,j\le n}\in K.
\]

If \(L/K\) is separable (see {{< knowl id="separable-extension" text="separable extension" >}}), then \(\mathrm{disc}_{L/K}(\mathbf{b})\neq 0\), and one can also express it using \(K\)-{{< knowl id="field-embedding" text="embeddings" >}} \(\sigma_1,\dots,\sigma_n:L\hookrightarrow \Omega\) into a common overfield \(\Omega\):
\[
\mathrm{disc}_{L/K}(\mathbf{b}) \;=\; \det(\sigma_i(b_j))_{i,j}^2.
\]
This shows how the discriminant measures “linear independence of conjugates” and links naturally to separability (compare {{< knowl id="separable-distinct-roots" text="separable elements have distinct conjugates" >}}).

### Examples
1. **Quadratic basis.** Let \(L=K(\sqrt{d})\) with \(\mathrm{char}(K)\neq 2\) and basis \((1,\sqrt{d})\). Using \(\mathrm{Tr}_{L/K}(1)=2\), \(\mathrm{Tr}_{L/K}(\sqrt{d})=0\), \(\mathrm{Tr}_{L/K}(d)=2d\),
\[
\mathrm{disc}_{L/K}(1,\sqrt{d})=\det\begin{pmatrix}2&0\\0&2d\end{pmatrix}=4d.
\]

2. **Power basis in a simple extension.** If \(L=K(\alpha)\) with \([L:K]=n\), the “power basis” \((1,\alpha,\dots,\alpha^{n-1})\) has discriminant
\(\mathrm{disc}_{L/K}(1,\alpha,\dots,\alpha^{n-1})=\det(\mathrm{Tr}_{L/K}(\alpha^{i+j}))_{0\le i,j\le n-1}\),
which can be computed from the minimal polynomial of \(\alpha\) in concrete cases.

3. **Finite fields: always zero over the prime field when inseparable is absent?** For \(L=\mathbb{F}_{q^n}\) over \(K=\mathbb{F}_q\), the extension is separable because finite fields are {{< knowl id="finite-fields-perfect" text="perfect" >}}, so discriminants of \(K\)-bases are nonzero. For example, if \(n=2\) and \(L=K(\alpha)\) with \(\alpha^2-\alpha-\beta=0\) irreducible over \(K\), then for the basis \((1,\alpha)\),
\[
\mathrm{disc}_{L/K}(1,\alpha)=\det\begin{pmatrix}
\mathrm{Tr}(1) & \mathrm{Tr}(\alpha)\\
\mathrm{Tr}(\alpha) & \mathrm{Tr}(\alpha^2)
\end{pmatrix}\in K^\times.
\]
