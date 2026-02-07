---
title: "Degree Equals Galois Group Order"
description: "For a finite Galois extension L/K, the degree [L:K] equals the size of Gal(L/K)."
---

Let $L/K$ be a finite {{< knowl id="field-extension" text="field extension" >}}. Its {{< knowl id="galois-group" text="Galois group" >}} is
\[
\mathrm{Gal}(L/K)=\{\sigma:L\to L \text{ a field automorphism with }\sigma|_K=\mathrm{id}_K\},
\]
i.e. the group of $K$-{{< knowl id="field-automorphism" text="automorphisms" >}} of $L$.

**Theorem (degree = group order for finite Galois extensions).**  
If $L/K$ is a finite {{< knowl id="galois-extension" text="Galois extension" >}}, then
\[
|\mathrm{Gal}(L/K)| = [L:K],
\]
where $[L:K]$ is the {{< knowl id="degree-of-extension" text="degree of the extension" >}}.

A useful companion fact is the inequality valid for any finite extension:
\[
|\mathrm{Aut}_K(L)| \le [L:K],
\]
with equality if and only if $L/K$ is Galois (equivalently: finite, {{< knowl id="separable-extension" text="separable" >}}, and {{< knowl id="normal-extension" text="normal" >}}; see {{< knowl id="separable-normal-galois" text="separable + normal = Galois" >}}).

### Examples
1. **Quadratic extensions.**  
   For $L=\mathbb{Q}(\sqrt2)$ over $K=\mathbb{Q}$, we have $[L:K]=2$. The two $K$-automorphisms are
   \[
   \sqrt2\mapsto \sqrt2 \quad\text{and}\quad \sqrt2\mapsto -\sqrt2,
   \]
   so $|\mathrm{Gal}(L/K)|=2=[L:K]$.

2. **A Galois splitting field of degree 6.**  
   Let $L$ be the {{< knowl id="splitting-field" text="splitting field" >}} over $\mathbb{Q}$ of $x^3-2$. Then $L=\mathbb{Q}(\sqrt[3]{2},\zeta_3)$ is finite Galois over $\mathbb{Q}$, and one finds
   \[
   [L:\mathbb{Q}]=6 \quad\text{and}\quad \mathrm{Gal}(L/\mathbb{Q})\cong S_3,
   \]
   so $|\mathrm{Gal}(L/\mathbb{Q})|=6=[L:\mathbb{Q}]$.

3. **Contrast: a non-Galois finite extension.**  
   The simple extension $L=\mathbb{Q}(\sqrt[3]{2})$ has $[L:\mathbb{Q}]=3$, but it is not {{< knowl id="normal-extension" text="normal" >}} (it does not contain the other complex cube roots), so it is not Galois. In fact, any $\mathbb{Q}$-automorphism must send $\sqrt[3]{2}$ to another root of its minimal polynomial; only the real root lies in $L$, so $\mathrm{Aut}_{\mathbb{Q}}(L)$ is trivial and $|\mathrm{Aut}_{\mathbb{Q}}(L)|=1<3$.
