---
title: "Field trace"
description: "For a finite extension L/K, the trace Tr_{L/K}(α) is the trace of multiplication-by-α as a K-linear map."
---

Let \(L/K\) be a finite {{< knowl id="field-extension" text="field extension" >}} of degree \(n=[L:K]\) (see {{< knowl id="degree-of-extension" text="degree of an extension" >}}). For \(\alpha\in L\), let
\[
m_\alpha: L\to L,\qquad x\mapsto \alpha x,
\]
viewed as a \(K\)-linear endomorphism of the \(K\)-vector space \(L\). The **(field) trace** of \(\alpha\) from \(L\) to \(K\) is
\[
\mathrm{Tr}_{L/K}(\alpha) := \mathrm{trace}(m_\alpha)\in K.
\]

Equivalently, if \(\Omega\) is a field containing \(L\) and the extension is separable (see {{< knowl id="separable-extension" text="separable extension" >}}), then
\[
\mathrm{Tr}_{L/K}(\alpha)=\sum_{\sigma} \sigma(\alpha),
\]
where the sum runs over all \(K\)-{{< knowl id="field-embedding" text="embeddings" >}} \(\sigma:L\hookrightarrow \Omega\) (counted without repetition). In particular, \(\mathrm{Tr}_{L/K}\) is \(K\)-linear and satisfies the tower property in {{< knowl id="trace-norm-towers" text="trace/norm in towers" >}} for a {{< knowl id="tower-of-fields" text="tower of fields" >}} \(K\subseteq M\subseteq L\).

### Examples
1. **Quadratic extension.** Let \(L=K(\sqrt{d})\) with \(\mathrm{char}(K)\neq 2\). For \(\alpha=a+b\sqrt{d}\),
\[
\mathrm{Tr}_{L/K}(\alpha)=(a+b\sqrt{d})+(a-b\sqrt{d})=2a.
\]

2. **Purely inseparable behavior (contrast).** If \(\mathrm{char}(K)=p\) and \(L=K(t)\) with \(t^p\in K\) (an {{< knowl id="inseparable-extension" text="inseparable extension" >}} of degree \(p\)), then \(\mathrm{Tr}_{L/K}(t)=0\); many traces vanish in purely inseparable situations.

3. **Finite fields.** For \(L=\mathbb{F}_{q^n}\) over \(K=\mathbb{F}_q\) (a {{< knowl id="finite-field" text="finite field" >}} extension), one has
\[
\mathrm{Tr}_{L/K}(\alpha)=\alpha+\alpha^{q}+\alpha^{q^2}+\cdots+\alpha^{q^{n-1}},
\]
where \(x\mapsto x^q\) is a power of the {{< knowl id="frobenius-endomorphism" text="Frobenius" >}}.
