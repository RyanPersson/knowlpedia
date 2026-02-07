---
title: "Equalizer"
description: "A universal solution E → A making two parallel morphisms A ⇉ B equal after composition."
---

Let \(\mathcal C\) be a {{< knowl id="category" text="category" >}} and let \(f,g:A\to B\) be parallel {{< knowl id="morphism" text="morphisms" >}} in \(\mathcal C\).

An **equalizer** of \(f\) and \(g\) is a morphism \(e:E\to A\) such that:
1. (**Equalizing condition**) \(f\circ e = g\circ e\),
2. (**Universal property**) for any morphism \(h:X\to A\) with \(f\circ h=g\circ h\), there exists a unique morphism \(u:X\to E\) such that
   \[
   e\circ u = h.
   \]

Equivalently, \(e:E\to A\) is universal among arrows into \(A\) on which \(f\) and \(g\) agree:
\[
\begin{CD}
X @>u>> E @>e>> A @>{f,g}>> B \\
@V h VV @. @. @. \\
A @. @. @.
\end{CD}
\qquad\text{with } f\circ e=g\circ e,\;\; f\circ h=g\circ h.
\]

An equalizer (when it exists) is a special case of a {{< knowl id="limit" text="limit" >}}.

## Basic properties
- The equalizer morphism \(e:E\to A\) is always a {{< knowl id="monomorphism-category" text="monomorphism" >}}: it is “injective” in the categorical sense.
- In an {{< knowl id="abelian-category" text="abelian category" >}}, the equalizer of \(f,g\) can be identified with a {{< knowl id="kernel-categorical" text="kernel" >}}:
  \[
  \mathrm{Eq}(f,g)\;\cong\;\ker(f-g).
  \]

## Examples
1. **\(\mathbf{Set}\)**.  
   If \(f,g:A\to B\) are functions, the equalizer is the subset
   \[
   E=\{a\in A \mid f(a)=g(a)\}\subseteq A,
   \]
   with \(e:E\hookrightarrow A\) the inclusion.

2. **\(\mathbf{Grp}\)**.  
   For homomorphisms \(f,g:G\to H\), the equalizer is the subgroup
   \[
   E=\{x\in G \mid f(x)=g(x)\}\le G,
   \]
   included into \(G\).

3. **\(\mathbf{Ab}\) (or \(R\)-Mod)**.  
   For module homomorphisms \(f,g:M\to N\), the equalizer is the submodule
   \[
   E=\ker(f-g)\subseteq M,
   \]
   with the inclusion \(E\hookrightarrow M\).
