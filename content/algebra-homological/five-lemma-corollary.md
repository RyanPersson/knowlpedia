---
title: "Corollary of the five lemma: the short five lemma"
description: "In a morphism of short exact sequences, isomorphisms on the ends force an isomorphism in the middle."
---

## Statement (short five lemma)
In any abelian setting (in particular for modules), consider a commutative diagram with exact rows
\[
\begin{array}{ccccccccc}
0 &\to& A' &\to& A &\to& A'' &\to& 0 \\
  && \downarrow && \downarrow && \downarrow \\
0 &\to& B' &\to& B &\to& B'' &\to& 0 \, .
\end{array}
\]
If \(A'\to B'\) and \(A''\to B''\) are isomorphisms, then \(A\to B\) is an isomorphism.

This is an immediate corollary of the {{< knowl id="five-lemma" text="five lemma" >}}: apply it to the corresponding length-5 exact sequences
\[
0 \to A' \to A \to A'' \to 0,\qquad 0 \to B' \to B \to B'' \to 0.
\]

Cross-links: {{< knowl id="five-lemma" text="five lemma" >}}, {{< knowl id="exact-sequence-modules" section="algebra-modules" text="exact sequences" >}}, {{< knowl id="short-exact-sequence" section="algebra-modules" text="short exact sequences" >}}.

## Examples

### Example 1: Multiplication-by-2 identifies \(\mathbb Z \cong 2\mathbb Z\)
Consider the short exact sequences of abelian groups
\[
0 \to 2\mathbb Z \to \mathbb Z \to \mathbb Z/2\mathbb Z \to 0
\]
and
\[
0 \to 4\mathbb Z \to 2\mathbb Z \to \mathbb Z/2\mathbb Z \to 0,
\]
where the quotient map \(2\mathbb Z \to \mathbb Z/2\mathbb Z\) is the identification \(2\mathbb Z/4\mathbb Z \cong \mathbb Z/2\mathbb Z\).

Define a morphism of short exact sequences by:
- left vertical map \(2\mathbb Z \to 4\mathbb Z\), \(x\mapsto 2x\) (an isomorphism),
- middle vertical map \(\mathbb Z \to 2\mathbb Z\), \(x\mapsto 2x\),
- right vertical map \(\mathbb Z/2\mathbb Z \to \mathbb Z/2\mathbb Z\), identity.

The ends are isomorphisms, so the short five lemma implies \(\mathbb Z \xrightarrow{\cdot 2} 2\mathbb Z\) is an isomorphism.

### Example 2: Linear algebra version
Let \(k\) be a field and let \(U\subset V\) and \(U'\subset W\) be subspaces. Given a commutative diagram of short exact sequences
\[
0\to U\to V\to V/U\to 0
\qquad\longrightarrow\qquad
0\to U'\to W\to W/U'\to 0
\]
where the induced maps \(U\to U'\) and \(V/U\to W/U'\) are isomorphisms, the short five lemma forces \(V\to W\) to be an isomorphism.

### Example 3: “If a map is an isomorphism on submodule and quotient, it is an isomorphism”
Let \(f:M\to N\) be a module map, and suppose there are submodules \(K\subseteq M\), \(L\subseteq N\) such that \(f(K)\subseteq L\), and \(f\) induces isomorphisms \(K\xrightarrow{\sim} L\) and \(M/K \xrightarrow{\sim} N/L\). Applying the short five lemma to
\[
0\to K\to M\to M/K\to 0,\qquad 0\to L\to N\to N/L\to 0
\]
shows \(f:M\to N\) is an isomorphism.
