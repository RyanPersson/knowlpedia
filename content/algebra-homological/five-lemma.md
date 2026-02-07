---
title: "Five lemma"
description: "In a morphism of exact sequences, if four vertical maps are isomorphisms (with mild extra hypotheses), then so is the middle map."
---

The five lemma is a standard diagram-chase tool in \(R\)-modules and, more generally, in any {{< knowl id="abelian-category" section="algebra-category-theory" text="abelian category" >}}. It strengthens the injectivity/surjectivity conclusions of the {{< knowl id="four-lemma" text="four lemma" >}} and is often used alongside the {{< knowl id="snake-lemma" text="snake lemma" >}}.

## Theorem (Five lemma)

Consider a commutative diagram with exact rows
\[
\begin{array}{ccccccccc}
A_1 &\to& A_2 &\to& A_3 &\to& A_4 &\to& A_5\\
\downarrow f_1 && \downarrow f_2 && \downarrow f_3 && \downarrow f_4 && \downarrow f_5\\
B_1 &\to& B_2 &\to& B_3 &\to& B_4 &\to& B_5
\end{array}
\]
Assume:
- \(f_1, f_2, f_4, f_5\) are isomorphisms,
- \(f_2\) is an epimorphism and \(f_4\) is a monomorphism (in module terms: \(f_2\) is surjective and \(f_4\) is injective).

Then \(f_3\) is an isomorphism.

(There are common variants with slightly different hypotheses; a frequent special case is when the sequences begin and end with \(0\), so surjectivity/injectivity assumptions are automatic.)

See also {{< knowl id="five-lemma-corollary" text="five lemma corollary" >}} for standard “short exact sequence” consequences.

## Examples

1. **Two-out-of-three for quasi-isomorphisms in a short exact sequence of complexes.**  
   Suppose
   \[
   0\to C'_\bullet \to C_\bullet \to C''_\bullet \to 0
   \quad\text{and}\quad
   0\to D'_\bullet \to D_\bullet \to D''_\bullet \to 0
   \]
   are short exact sequences of {{< knowl id="chain-complex" text="chain complexes" >}}, and we have a morphism between them inducing a commutative diagram of long exact sequences in {{< knowl id="homology-module" text="homology" >}}.  
   If the induced maps \(H_n(C'_\bullet)\to H_n(D'_\bullet)\) and \(H_n(C''_\bullet)\to H_n(D''_\bullet)\) are isomorphisms for all \(n\), then the induced maps \(H_n(C_\bullet)\to H_n(D_\bullet)\) are isomorphisms for all \(n\), by applying the five lemma degree-by-degree to the long exact homology sequences.

2. **Comparing Tor groups via a map of short exact sequences.**  
   Given a morphism between short exact sequences
   \[
   \begin{array}{ccccccccc}
   0 &\to& A' &\to& A &\to& A'' &\to& 0\\
    && \downarrow && \downarrow && \downarrow &&\\
   0 &\to& B' &\to& B &\to& B'' &\to& 0
   \end{array}
   \]
   and a fixed module \(M\), naturality of the {{< knowl id="long-exact-sequence-tor" text="long exact Tor sequence" >}} gives a morphism of long exact sequences
   \[
   \cdots \to \operatorname{Tor}_n(A'',M)\to \operatorname{Tor}_{n-1}(A',M)\to \cdots
   \]
   If the induced maps \(\operatorname{Tor}_n(A',M)\to \operatorname{Tor}_n(B',M)\) and \(\operatorname{Tor}_n(A'',M)\to \operatorname{Tor}_n(B'',M)\) are isomorphisms for all relevant neighboring terms (for instance, if \(A'\to B'\) and \(A''\to B''\) are isomorphisms), then the five lemma implies \(\operatorname{Tor}_n(A,M)\to \operatorname{Tor}_n(B,M)\) is an isomorphism as well.

3. **Comparing Ext groups (same pattern).**  
   With the same setup, applying the {{< knowl id="long-exact-sequence-ext" text="long exact Ext sequence" >}} and using the five lemma shows that if the induced maps on the surrounding \(\operatorname{Hom}\) and \(\operatorname{Ext}\) terms are isomorphisms, then the middle \(\operatorname{Ext}\)-map is an isomorphism. This is a standard way to propagate isomorphisms through long exact sequences.
