---
title: "Separable element"
description: "An algebraic element whose minimal polynomial has distinct roots in a splitting field."
---

Let \(K/F\) be a {{< knowl id="field-extension" text="field extension" >}} and let \(\alpha\in K\) be an {{< knowl id="algebraic-element" text="algebraic element" >}} over \(F\). Let \(m_{\alpha,F}(x)\in F[x]\) be the minimal polynomial of \(\alpha\) over \(F\).

**Definition (separable element).** The element \(\alpha\) is *separable over \(F\)* if the polynomial \(m_{\alpha,F}(x)\) has no repeated roots in a {{< knowl id="splitting-field" text="splitting field" >}} (equivalently, in an {{< knowl id="algebraic-closure" text="algebraic closure" >}} of \(F\)). In other words, \(m_{\alpha,F}(x)\) has \(\deg(m_{\alpha,F})\) distinct roots.

A convenient algebraic criterion is:
\[
\alpha \text{ is separable over } F \quad \Longleftrightarrow \quad \gcd\big(m_{\alpha,F},\, m'_{\alpha,F}\big)=1 \text{ in } F[x],
\]
where \(m'_{\alpha,F}\) is the formal derivative. The link between separability and distinct roots is recorded in {{< knowl id="separable-distinct-roots" text="separable polynomials have distinct roots" >}}.

**Examples.**
1. Over \(F=\mathbb{Q}\), \(\alpha=\sqrt2\) is separable: its minimal polynomial \(x^2-2\) has distinct roots \(\pm\sqrt2\).
2. Over a field of characteristic \(p>0\), separability can fail. In \(K=\mathbb{F}_p(t^{1/p})\) over \(F=\mathbb{F}_p(t)\), the element \(\alpha=t^{1/p}\) has minimal polynomial \(x^p-t\), whose derivative is \(px^{p-1}=0\); the polynomial has a single root of multiplicity \(p\), so \(\alpha\) is not separable over \(F\).
3. In any extension of a {{< knowl id="perfect-field" text="perfect field" >}} (e.g. \(F=\mathbb{F}_p\) or \(F=\mathbb{Q}\)), every algebraic element is separable; in particular, every \(\alpha\in \mathbb{F}_{p^n}\) is separable over \(\mathbb{F}_p\).
