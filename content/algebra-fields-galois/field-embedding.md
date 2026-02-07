---
title: "Field embedding"
description: "An injective field homomorphism, often required to fix a base field in extension theory."
---

Let \(K\) and \(L\) be {{< knowl id="field" section="algebra-rings" text="fields" >}}. A **field embedding** \(\sigma:K\hookrightarrow L\) is a ring homomorphism \(\sigma:K\to L\) such that \(\sigma(1)=1\) and \(\sigma\) is injective.

More generally, given a {{< knowl id="field-extension" text="field extension" >}} \(L/K\) and a field \(\Omega\) containing \(K\), a **\(K\)-embedding** of \(L\) into \(\Omega\) is a field embedding \(\sigma:L\hookrightarrow \Omega\) whose restriction to \(K\) is the identity map. In this setting, \(\sigma\) is also called a **\(K\)-homomorphism**. If \(\sigma\) is bijective, it is a {{< knowl id="field-automorphism" text="field automorphism" >}} of \(L\) (and if it fixes \(K\), a \(K\)-automorphism).

Field embeddings are the basic inputs for expressing the {{< knowl id="trace-field" text="trace" >}} and {{< knowl id="norm-field" text="norm" >}} as sums/products of conjugates when the extension is finite and separable.

### Examples
1. **Inclusion map.** If \(K\subseteq L\) (so \(L/K\) is a {{< knowl id="field-extension" text="field extension" >}}), the inclusion \(K\hookrightarrow L\) is a field embedding.

2. **Two \(\mathbb{Q}\)-embeddings of a quadratic field.** Let \(L=\mathbb{Q}(\sqrt{d})\) with \(d\) squarefree. Then there are two \(\mathbb{Q}\)-embeddings \(L\hookrightarrow \mathbb{C}\): one sends \(\sqrt{d}\mapsto \sqrt{d}\), the other sends \(\sqrt{d}\mapsto -\sqrt{d}\).

3. **Embeddings of a simple extension from roots.** Let \(L=\mathbb{Q}(\alpha)\) be a {{< knowl id="simple-extension" text="simple extension" >}} with \(\alpha\) algebraic, and let \(m_\alpha(x)\in\mathbb{Q}[x]\) be the minimal polynomial. Any \(\mathbb{Q}\)-embedding \(\sigma:L\hookrightarrow \mathbb{C}\) is determined by the choice of a root \(\beta\) of \(m_\alpha\), via \(\sigma(\alpha)=\beta\).
