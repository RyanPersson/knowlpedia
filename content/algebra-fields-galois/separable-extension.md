---
title: "Separable extension"
description: "An algebraic extension in which every element is separable over the base field."
---

Let \(K/F\) be an algebraic {{< knowl id="field-extension" text="field extension" >}}.

**Definition (separable extension).** The extension \(K/F\) is *separable* if every element \(\alpha\in K\) is a {{< knowl id="separable-element" text="separable element" >}} over \(F\).

When \(K/F\) is finite, separability admits useful equivalent formulations. For example, if \(\overline F\) is an {{< knowl id="algebraic-closure" text="algebraic closure" >}} of \(F\), then \(K/F\) is separable iff there are exactly \([K:F]\) distinct \(F\)-{{< knowl id="field-embedding" text="embeddings" >}} \(K\hookrightarrow \overline F\). Separability behaves well in towers, as summarized in {{< knowl id="separability-towers" text="separability in towers" >}}.

**Examples.**
1. Every algebraic extension of a characteristic \(0\) field is separable. In particular, \(\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q}\) is separable (even though it is not {{< knowl id="normal-extension" text="normal" >}}).
2. For finite fields, \(\mathbb{F}_{p^n}/\mathbb{F}_p\) is separable; in fact it is {{< knowl id="galois-extension" text="Galois" >}}.
3. The extension \(\mathbb{F}_p(t^{1/p})/\mathbb{F}_p(t)\) is not separable: the element \(t^{1/p}\) is not separable over \(\mathbb{F}_p(t)\).
